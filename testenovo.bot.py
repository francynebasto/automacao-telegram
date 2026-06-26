from telethon import TelegramClient

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

client = TelegramClient("sessao", api_id, api_hash)

async def main():
    await client.start()

    await client.send_message(-5562907846, "Francyne x Julio r6c3 teste  ")

    print("Mensagem enviada!")

    await client.disconnect()

client.loop.run_until_complete(main())