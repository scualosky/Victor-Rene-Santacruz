import os
import time
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot

# Cargar variables de entorno
load_dotenv()
OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_API_SECRET = os.getenv("OKX_API_SECRET")
OKX_PASSPHRASE = os.getenv("OKX_PASSPHRASE")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

# Variables iniciales
pares_seguidos = set(["RENDER-USDT", "SOL-USDT"])  # Puedes cambiarlos con comandos
ultimos_mensajes = {}

# Simulación de análisis técnico
def analizar_par(par):
    # Aquí iría la lógica real de análisis técnico
    return {
        "par": par,
        "rsi": 45.3,
        "ema_20": 7.80,
        "ema_50": 7.65,
        "ema_200": 6.92,
        "macd": "cruce alcista",
        "soporte": 7.20,
        "resistencia": 8.10,
        "recomendacion": "esperar"
    }

# Enviar mensaje por Telegram
def enviar_mensaje(texto):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=texto)

# Simulación de ciclo de análisis
def ciclo_analisis():
    for par in pares_seguidos:
        datos = analizar_par(par)
        mensaje = f"🔎 Análisis técnico de {datos['par']}
"
        mensaje += f"RSI: {datos['rsi']} | MACD: {datos['macd']}
"
        mensaje += f"EMA 20/50/200: {datos['ema_20']} / {datos['ema_50']} / {datos['ema_200']}
"
        mensaje += f"Soporte: {datos['soporte']} | Resistencia: {datos['resistencia']}
"
        mensaje += f"📈 Recomendación: {datos['recomendacion']}"
        if ultimos_mensajes.get(par) != mensaje:
            enviar_mensaje(mensaje)
            ultimos_mensajes[par] = mensaje

# Loop principal
if __name__ == "__main__":
    enviar_mensaje("✅ Bot de análisis técnico iniciado.")
    while True:
        try:
            ciclo_analisis()
            time.sleep(300)  # 5 minutos
        except Exception as e:
            enviar_mensaje(f"⚠️ Error: {e}")
            time.sleep(60)
