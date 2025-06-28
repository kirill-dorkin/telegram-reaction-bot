# Telegram Reaction Bot

Этот бот автоматически подписывается на указанные каналы и ставит реакции на новые сообщения от имени всех подключённых аккаунтов.

## Быстрый старт
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kirill-dorkin/telegram-reaction-bot.git
   cd telegram-reaction-bot
   ```
2. Укажите каналы в `config.py` и при необходимости добавьте каталоги `tdata` или файлы сессий в папки `tdatas` и `sessions`.
3. Выполните установку зависимостей и подготовку окружения:
   ```bash
   export API_ID=your_api_id
   export API_HASH=your_api_hash
   export PHONE_NUMBER=your_phone
   ./setup.sh
   ```
   Скрипт создаст виртуальное окружение, установит зависимости и сформирует файл `sessions/account.json`.
4. Запустите бота:
   ```bash
   ./start.sh
   ```

Бот проверит подписку для каждого аккаунта и при необходимости подпишется, после чего будет реагировать на все новые посты в каналах из `config.py`.

