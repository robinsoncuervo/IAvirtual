
#####
import logging
from model import seleccionar_top3_freelancers
from database import SafeFreelancerDataSystem
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,  # Cambiado desde Updater
    CommandHandler,
    ContextTypes,  # Nuevo tipo de contexto
    MessageHandler,
    filters
)
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensaje de bienvenida"""
    user = update.effective_user
    await update.message.reply_text(
        f'Hola {user.first_name}! Soy un el bot de Asistia, puedes encontrar muchos servicios.\n'
        'hola hola\n'
        'Esta es una prueba de un bot de telegram\n'
    )
async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) != 4:
            await update.message.reply_text("Usa el formato:\n/buscar <habilidad> <disponibilidad> <valoracion> <tarifa>")
            return

        habilidad, disponibilidad = args[0], args[1]
        valoracion_deseada = float(args[2])
        tarifa_deseada = float(args[3])

        with SafeFreelancerDataSystem() as sistema:
            data = sistema.get_filtered_freelancers(habilidad, disponibilidad)
            top3 = seleccionar_top3_freelancers(data, tarifa_deseada, valoracion_deseada)

        if not top3:
            await update.message.reply_text("No se encontraron freelancers que coincidan.")
            return

        for f in top3:
            await update.message.reply_text(
                f"👤 Nombre: {f['nombre']}\n"
                f"📍 Ubicación: {f['ubicacion']}\n"
                f"⭐ Valoración: {f['Valoración']}\n"
                f"💰 Tarifa: {f['tarifa']}\n"
                f"🧰 Experiencia: {f['Experiencia']} años\n"
                f"📞 Teléfono: {f['telefono']}"
            )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")






def main():
    # Configuración moderna con ApplicationBuilder
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("buscar", buscar))

    
    print("Bot en ejecución...")
    application.run_polling()

if __name__ == '__main__':
    main()

