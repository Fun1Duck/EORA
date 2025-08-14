import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from sentence_transformers import SentenceTransformer
import faiss
from openai import OpenAI
from context import system_prompt
from config import bot_hub_API, BOT_TOKEN
from materials import materials
import json
import numpy as np
import re


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

client_bot_hub = OpenAI(api_key=bot_hub_API,
                base_url='https://bothub.chat/api/v2/openai/v1')

model = SentenceTransformer('deepvk/USER-bge-m3')
index = faiss.IndexFlatIP(1024)
materials_texts = []

def embed_text(text):
    embedding = model.encode(text)
    return np.array(embedding, dtype=np.float32)

def rag(query, top_k=3, threshold=0.4):
    query_embedding = embed_text(query).reshape(1, -1)
    faiss.normalize_L2(query_embedding)
    D, I = index.search(query_embedding, top_k)
    similar_info = [materials_texts[i] for i, dist in zip(I[0], D[0]) if dist > threshold and i < len(materials_texts)]
    return similar_info

for title in materials:
    material_embedding = embed_text(f"{title} {materials[title]['description']}").reshape(1, -1)
    faiss.normalize_L2(material_embedding)
    materials_texts.append(title)
    index.add(material_embedding)


@router.message(Command('start'))
async def start_handler(msg, state: FSMContext, bot):
    await msg.answer(text=f"Здравствуйте, {msg.from_user.first_name}! Я бот-помощник, который дает ответы на вопросы потенциальных клиентов EORA.")


@router.message(F.text)
async def eora(msg, state: FSMContext):
    text_user = msg.text

    data = await state.get_data()
    if "dialog_history" not in data:
        history = []
    else:
        history = data["dialog_history"][-6:]
    history.append({"role": "user", "content": text_user})

    similar_info = rag(text_user)
    if not similar_info:
        context_to_promt = "К сожалению, я не нашёл информации по вашему запросу."
    else:
        context_to_promt = {title: {"url": materials[title]['url'], "description": materials[title]['description']} for title in similar_info}

    messages = [
        {"role": "system", "content": f'{system_prompt} Материалы:\n{json.dumps(context_to_promt, ensure_ascii=False, indent=2)}\n\nПочта: hello@eora.ru\nТелефон: +7 495 414-40-49\nАдрес: Иннополис ул. Университетская, д. 7'},
        *history
    ]

    try:
        response = client_bot_hub.chat.completions.create(
            messages=messages,
            model='deepseek-chat-v3-0324'
        )
        bot_reply = response.choices[0].message.content
        bot_reply = re.sub(r'[*#_~`]', '', bot_reply)
    except Exception as e:
        print(e)
        history.pop()
        await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
        return
    else:
        history.append({"role": "assistant", "content": bot_reply})
        await msg.answer(text=bot_reply, parse_mode='HTML')
        await state.update_data(dialog_history=history)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

