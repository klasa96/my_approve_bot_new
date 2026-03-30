import asyncio
from telegram import Update
from telegram.ext import Application, ContextTypes, ChatJoinRequestHandler

# ВАЖНО: переменные берем из окружения, токен не вшит
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1001234567890   # подставьте свой числовой ID с минусом, без кавычек

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user
    # сравниваем числовые ID каналов
    if join_request.chat.id == CHANNEL_ID:
        try:
            await context.bot.approve_chat_join_request(
                chat_id=CHANNEL_ID, user_id=user.id
            )
            print(f"✅ Одобрена заявка для @{user.username} (ID: {user.id})")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(auto_approve))
    print("🤖 Бот запущен и ждет заявки...")
    app.run_polling()

if __name__ == "__main__":
    main()