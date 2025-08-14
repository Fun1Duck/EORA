from context import *


materials = {
    "Нейросеть, которая управляет трансляцией матча": {
        "url": "https://eora.ru/cases/sportrecs-nejroset-operator-sportivnyh-translyacij",
        "description": sportrecs
    },
    "Промышленная безопасность: система для проверки на производствах": {
        "url": "https://eora.ru/cases/promyshlennaya-bezopasnost",
        "description": promyshlennaya_bezopasnost
    },
    "Поиск похожих изображений": {
        "url": "https://eora.ru/cases/lamoda-systema-segmentacii-i-poiska-po-pohozhey-odezhde",
        "description": lamoda
    },
    "Голосовой ассистент в обличье карася": {
        "url": "https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/karas-golosovoy-assistent",
        "description": karas
    },
    "Ассистенты городов. Универсальные помощники для туристов и жителей": {
        "url": "https://eora.ru/cases/assistenty-dlya-gorodov",
        "description": assistenty_dlya_gorodov
    },
    "Система распознавания рукописных химических схем": {
        "url": "https://eora.ru/cases/avtomatizaciya-v-promyshlennosti/chemrar-raspoznovanie-molekul",
        "description": chemrar_raspoznovanie_molekul
    },
    "Интерактивные сказки про Ам Няма для умной приставки от «Сбера»": {
        "url": "https://eora.ru/cases/zeptolab-skazki-pro-amnyama-dlya-sberbox",
        "description": zeptolab
    },
    "Алгоритм для оценки игроков в Counter Strike, Dota и World of Tanks": {
        "url": "https://eora.ru/cases/goosegaming-algoritm-dlya-ocenki-igrokov",
        "description": goosegaming
    },
    "Робот-аналитик отзывов в приложении «Додо Пиццы»": {
        "url": "https://eora.ru/cases/dodo-pizza-robot-analitik-otzyvov",
        "description": robot_analitik_otzyvov
    },
    "Нейросеть, которая определяет вес салата по фото": {
        "url": "https://eora.ru/cases/ifarm-nejroset-dlya-ferm",
        "description": ifarm
    },
    "Навык в Алисе для проверки родинок. Социальный проект.": {
        "url": "https://eora.ru/cases/zhivibezstraha-navyk-dlya-proverki-rodinok",
        "description": zhivibezstraha
    },
    "Чат-бот, помогающий женщинам подобрать подарки для мужчин. Анализ изображений.": {
        "url": "https://eora.ru/cases/avon-chat-bot-dlya-zhenshchin",
        "description": avon
    },
    "Навык для проверки лотерейных билетов. Навык в Алисе.": {
        "url": "https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/navyk-dlya-proverki-loterejnyh-biletov",
        "description": loterejnyh
    },
    "Система обнаружения посторонних предметов на днищах автомобилей с помощью нейросети. Анализ изображений.": {
        "url": "https://eora.ru/cases/computer-vision/iss-analiz-foto-avtomobilej",
        "description": iss
    },
    "Мастер-бот. Универсальный бот для сайтов Purina, которого можно постоянно обучать": {
        "url": "https://eora.ru/cases/purina-master-bot",
        "description": master_bot
    },
    "Модель, позволяющая подобрать оптимальную вероятность выпадения скинов из лутбоксов": {
        "url": "https://eora.ru/cases/skinclub-algoritm-dlya-ocenki-veroyatnostej",
        "description": skinclub
    },
    "Чат-бот, который знакомит инвесторов и резидентов «Сколково»": {
        "url": "https://eora.ru/cases/skolkovo-chat-bot-dlya-startapov-i-investorov",
        "description": skolkovo
    },
    "Чат-бот определяет породу собаки по фото и даёт советы по питанию. Чат-бот «ВКонтакте».": {
        "url": "https://eora.ru/cases/purina-podbor-korma-dlya-sobaki",
        "description": podbor_korma
    },
    "Викторина с вопросами об уходе за кошками.Навык в Алисе.": {
        "url": "https://eora.ru/cases/purina-navyk-viktorina",
        "description": viktorina
    },
    "Бот для телефонии. Пилот по автоматизации контактного центра «ДОДО пиццы».": {
        "url": "https://eora.ru/cases/dodo-pizza-pilot-po-avtomatizacii-kontakt-centra",
        "description": pilot
    },
    "Бот для телефонии. Бот на миллион: как мы автоматизировали контакт-центр «Додо Пиццы».": {
        "url": "https://eora.ru/cases/dodo-pizza-avtomatizaciya-kontakt-centra",
        "description": avtomatizaciya
    },
    "Виджет на сайте. Бот-справочник, суфлирующий операторам контакт-центра.": {
        "url": "https://eora.ru/cases/icl-bot-sufler-dlya-kontakt-centra",
        "description": sufler
    },
    "Навык для Алисы и чат-бот, который подбирает авиабилеты": {
        "url": "https://eora.ru/cases/s7-navyk-dlya-podbora-aviabiletov",
        "description": aviabiletov
    },
    "Бот для бесконтактной покупки питания через WhatsApp.": {
        "url": "https://eora.ru/cases/workeat-whatsapp-bot",
        "description": workeat
    },
    "Навык в Алисе. Навык, помогающий рассчитать страховку.": {
        "url": "https://eora.ru/cases/absolyut-strahovanie-navyk-dlya-raschyota-strahovki",
        "description": strahovanie
    },
    "Поиск по изображениям. Система, позволяющая искать товары по фотографии на сайте интернет-магазина.": {
        "url": "https://eora.ru/cases/kazanexpress-poisk-tovarov-po-foto",
        "description": poisk_tovarov
    },
    "Cистема персональных рекомендаций на сайте KazanExpress.": {
        "url": "https://eora.ru/cases/kazanexpress-sistema-rekomendacij-na-sajte",
        "description": sistema_rekomendacij
    },
    "Поиск похожих изображений. Система, позволяющая быстро проверить логотип на плагиат.": {
        "url": "https://eora.ru/cases/intels-proverka-logotipa-na-plagiat",
        "description": intels
    },
    "Навык в Алисе. Викторина с вопросами про уборку.": {
        "url": "https://eora.ru/cases/karcher-viktorina-s-voprosami-pro-uborku",
        "description": karcher
    },
    "Чат-бот в виджете на промо-сайте и основном сайте Purina. Виджет на сайте.": {
        "url": "https://eora.ru/cases/chat-boty/purina-friskies-chat-bot-na-sajte",
        "description": friskies
    },
    "Нейросеть, которая сегментирует кадры мобильного видео и «ищет»на них человека.": {
        "url": "https://eora.ru/cases/nejroset-segmentaciya-video",
        "description": segmentaciya
    },
    "Анализ и обработка видеопотоков. Нейросеть, которая добавляет в видео анимацию и яркие цвета.": {
        "url": "https://eora.ru/cases/chat-boty/essa-nejroset-dlya-generacii-rolikov",
        "description": essa
    },
    "Анализ данных. Модель, объясняющая аномалии в транзакциях QIWI.": {
        "url": "https://eora.ru/cases/qiwi-poisk-anomalij",
        "description": qiwi
    },
    "Нейросеть для распознавания показаний счетчиков.": {
        "url": "https://eora.ru/cases/frisbi-nejroset-dlya-raspoznavaniya-pokazanij-schetchikov",
        "description": frisbi
    },
    "Навык в Google Assistant. Навык, который читает ребенку сказки перед сном.": {
        "url": "https://eora.ru/cases/skazki-dlya-gugl-assistenta",
        "description": skazki
    },
    "Бот для компании Магнит, который самостоятельно приглашает кандидатов на собеседование.": {
        "url": "https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie",
        "description": sobesedovanie
    }
}
