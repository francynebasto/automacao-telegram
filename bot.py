from telethon import TelegramClient
import asyncio

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

client = TelegramClient("sessao", api_id, api_hash)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("Sessão inválida")
        return

    await client.send_message(-5562907846, "🔥 TESTE: bot funcionando no Render")

    print("Mensagem enviada com sucesso!")

    await client.disconnect()

asyncio.run(main())