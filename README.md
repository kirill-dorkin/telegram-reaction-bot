## Бот для реакций на посты в Telegram

Бот автоматически ставит реакции на новые сообщения в канале, группе или чате. Реакции отправляются от всех подключённых сессий, а также аккаунты автоматически подписываются на ваш канал.

**Плюсы 👍:**
* Автоматически конвертирует `TDATA` в сессию Pyrogram.
* Автоматически конвертирует сессию Telethon в формат Pyrogram.

## Инструкция по запуску
Проект проверен на **Python 3.11** и более ранних версиях. На новых версиях может не собраться `uvloop` или `cryptg`.

1. Создайте пустую папку.
2. `git clone https://github.com/kanewi11/telegram-reaction-bot.git ./`
3. `python3 -m venv venv` или на Windows `python -m venv venv`
4. `. venv/bin/activate` или на Windows `\venv\Scripts\activate`
5. `pip install -r requirements.txt` или на Windows `pip install -r requirements_win.txt`
6. Укажите название вашего канала в `config.py`
7. **Если планируете использовать конвертер TDATA**, откройте `converters/tdata_to_telethon.py` и вставьте `API_HASH` и `API_ID` (строки 19 и 20)
8. `mkdir sessions` и `mkdir tdatas` (или просто создайте эти две папки)
9. Поместите файлы сессий и их конфигурации в `/sessions` или tdata‑папки в `/tdatas` (см. пункт 7)

Пример структуры:
```
your_dir
└───reactionbot.py
│
└───sessions
│   │   8888888888.ini
│   │   8888888888.session
│   │   9999999999.ini
│   │   9999999999.session
│   │   98767242365.json
│   │   98767242365.session
│   │   ...
│
└───tdatas
│   └─── my_tdata
│   │   │ key_datas
│   │   │ ...
...
```
10. `nohup python reactionbot.py &`

### Подключение множества аккаунтов
Просто добавьте файлы *.session или папки tdata всех ваших аккаунтов в `sessions` или `tdatas`. Бот задействует их все, поэтому можно использовать сотни профилей.

## Создание сессии вручную
Создайте файл `my_account.json` (имя может быть любым) в папке `/sessions`:
```json
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number"
}
```
После запуска `python reactionbot.py` авторизуйтесь в консоли. Файл сессии сохранится, и при следующих запусках входить заново не нужно.

## Где взять `api_id` и `api_hash`?
[🔗 Ссылка.](https://my.telegram.org/auth)

## Пример конфигурационного файла
Можно указать дополнительные параметры, которые поддерживает [pyrogram](https://github.com/pyrogram/pyrogram).

`sessions/888888888.ini`
```
[pyrogram]
api_id = your_api_id
api_hash = your_api_hash
phone_number = 888888888

# необязательные параметры
app_version = '8.8.5'
device_model = 'Vertu IVERTU'
system_version = 'Android'
```

**ИЛИ** (выберите один из вариантов конфигурации)

`sessions/888888888.json`
```json
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number",
    ...
}
```
