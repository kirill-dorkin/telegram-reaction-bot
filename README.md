# Бот реакций для Telegram

## Описание
Бот автоматически ставит реакции на новые сообщения в канале, группе или чате. Реакции отправляются от имени всех подключённых сессий, при этом аккаунты автоматически подписываются на указанный канал.

## Преимущества
- Автоматическое преобразование каталогов `tdata` в сессии Pyrogram.
- Автоматическое преобразование сессий Telethon в Pyrogram.

## Запуск
1. Создайте пустую папку.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kirill-dorkin/telegram-reaction-bot.git ./
   ```
3. Создайте виртуальное окружение:
   ```bash
   python3 -m venv venv   # или python -m venv venv в Windows
   ```
4. Активируйте окружение:
   ```bash
   source venv/bin/activate   # или .\venv\Scripts\activate в Windows
   ```
5. Установите зависимости:
   ```bash
   pip install -r requirements.txt   # или pip install -r requirements_win.txt в Windows
   ```
6. Укажите имя канала в `config.py`.
7. Если планируете использовать конвертер `tdata`, откройте `converters/tdata_to_telethon.py` и задайте `API_HASH` и `API_ID` (строки 18–19).
8. Создайте папки `sessions` и `tdatas`.
9. Поместите файлы сессий и их конфигурации в `sessions` или каталоги `tdata` в `tdatas` (см. пункт 7).
10. Запустите бота:
    ```bash
    nohup python reactionbot.py &
    ```

### Пример структуры каталога
```
your_dir
├── reactionbot.py
├── sessions
│   ├── 8888888888.ini
│   ├── 8888888888.session
│   ├── 9999999999.ini
│   ├── 9999999999.session
│   ├── 98767242365.json
│   ├── 98767242365.session
│   └── ...
└── tdatas
    └── my_tdata
        ├── key_datas
        └── ...
```

## Ручное создание файла сессии
Создайте файл `my_account.json` (название может быть любым) в каталоге `sessions`:
```json
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number"
}
```
После запуска `python reactionbot.py` пройдите авторизацию в консоли. Файл сессии будет создан и в дальнейшем повторять процедуру не потребуется.

## Где взять `api_id` и `api_hash`
[Ссылка на my.telegram.org](https://my.telegram.org/auth)

## Пример конфигурационного файла
Можно добавить другие параметры, поддерживаемые [Pyrogram](https://github.com/pyrogram/pyrogram).

`sessions/888888888.ini`
```ini
[pyrogram]
api_id = your_api_id
api_hash = your_api_hash
phone_number = 888888888

# необязательные параметры
app_version = '8.8.5'
device_model = 'Vertu IVERTU'
system_version = 'Android'
```

**Или** (выберите подходящий вариант конфигурации)

`sessions/888888888.json`
```json
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number"
}
```

## Подключение папок `tdata`
1. Зарегистрируйте приложение на [my.telegram.org](https://my.telegram.org) и получите `API_ID` и `API_HASH`.
2. В файле `converters/tdata_to_telethon.py` замените значения `API_HASH` и `API_ID` (строки 18–19).
3. Создайте папки `sessions` и `tdatas`, если они ещё не существуют.
4. Поместите все каталоги `tdata` в папку `tdatas`.
5. Запустите `python reactionbot.py`. Каждая папка `tdata` будет автоматически конвертирована в сессию Pyrogram и сохранена в `sessions`. После конвертации бот использует эти аккаунты для выставления реакций и подписки на канал.
