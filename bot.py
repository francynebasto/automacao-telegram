from telethon import TelegramClient
import asyncio

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

client = TelegramClient("sessao", api_id, api_hash)

async def main():
    await client.connect()

    # NÃO pede login se a sessao existir
    if not await client.is_user_authorized():
        print("Sessão não autorizada. Rode no PC primeiro.")
        return

    await client.send_message(-5562907846, "Francyne x Julio r6c3")

    print("Mensagem enviada!")

    await client.disconnect()

asyncio.run(main())