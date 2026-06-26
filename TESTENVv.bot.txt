import asyncio
from datetime import datetime
from telethon import TelegramClient

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

client = TelegramClient("sessao", api_id, api_hash)

async def enviar():
    await client.send_message(-5562907846, "Francyne x Julio r6c3")
    print("Mensagem enviada!")

async def main():
    await client.start()

    print("Bot rodando. Aguardando 07:55...")

    enviado_hoje = False

    while True:
        agora = datetime.now()

        if agora.hour == 7 and agora.minute == 55 and not enviado_hoje:
            try:
                await enviar()
                enviado_hoje = True
            except Exception as e:
                print(f"Erro ao enviar: {e}")

        # Reseta o envio quando virar um novo dia
        if agora.hour == 0 and agora.minute == 0:
            enviado_hoje = False

        await asyncio.sleep(1)

asyncio.run(main())