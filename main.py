import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from openai import OpenAI
from config import bot_hub_API, BOT_TOKEN
from materials import materials
import json


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

client_bot_hub = OpenAI(api_key=bot_hub_API,
                base_url='https://bothub.chat/api/v2/openai/v1')

@router.message(Command('start'))
async def start_handler(msg, state: FSMContext, bot):
    await msg.answer(text=f"Здравствуйте, {msg.from_user.first_name}! Я бот-помощник, который дает ответы на вопросы потенциальных клиентов EORA.")


@router.message(F.text)
async def ru_native(msg, state: FSMContext):
    text_user = msg.text

    data = await state.get_data()
    if "dialog_history" not in data:
        history = []
    else:
        history = data["dialog_history"][-6:]
    history.append({"role": "user", "content": text_user})

    messages = [
        {"role": "system", "content": f'Ты чат-бот, который дает ответы на вопросы компании EORA и ссылки на используемые файлы, приложив их напрямую к местам в тексте, учитывая материалы с оффициального сайта. Не выдумывай ничего лишнего. Материалы:\n{json.dumps(materials, ensure_ascii=False, indent=2)}\n\nПочта: hello@eora.ru\nТелефон: +7 495 414-40-49\nАдрес: Иннополис ул. Университетская, д. 7'},
        *history
    ]

    response = client_bot_hub.chat.completions.create(
        messages=messages,
        model='deepseek-chat-v3-0324'
    )
    bot_reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": bot_reply})
    await msg.answer(text=bot_reply)
    await state.update_data(dialog_history=history)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())