import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

client = TelegramClient("sessao", api_id, api_hash)

HORA = 8
MINUTO = 10

async def enviar():
    await client.send_message(-5562907846, "Francyne x Julio r6c3")

async def main():
    await client.start()

    print("Bot iniciado.")

    enviado_hoje = False

    while True:
        agora = datetime.now()

        if agora.hour == HORA and agora.minute == MINUTO and not enviado_hoje:

            print("Horário chegou! Tentando enviar...")

            limite = datetime.now() + timedelta(minutes=6)

            while datetime.now() < limite:
                try:
                    await enviar()
                    print("Mensagem enviada às", datetime.now().strftime("%H:%M:%S"))
                    enviado_hoje = True
                    break

                except Exception as e:
                    print("Ainda não foi possível enviar:", e)
                    await asyncio.sleep(3)

        if agora.hour == 0 and agora.minute == 0:
            enviado_hoje = False

        await asyncio.sleep(1)

asyncio.run(main())