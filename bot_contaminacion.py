import discord  # Importar la biblioteca discord para interactuar con la API de Discord
from discord.ext import commands  # Importar comandos de discord.ext para crear comandos de bot
from settings import settings  # Importar configuraciones desde el archivo settings.py
import random  # Importar el módulo random para generar valores aleatorios

# Definiciones de funciones y datos que estaban en bot_logic.py

# Lista de ideas de manualidades
manualidades = [
    "Haz una maceta usando una botella de plástico.",  # Idea 1
    "Crea un organizador con tubos de PVC.",  # Idea 2
    "Construye un estuche para lápices reutilizando botellas pequeñas.",  # Idea 3
]

# Diccionario para clasificar residuos
clasificacion_residuos = {
    "botella de plástico": "Contenedor amarillo (reciclaje de plásticos).",  # Clasificación para botellas de plástico
    "papel usado": "Contenedor azul (papel).",  # Clasificación para papel usado
    "manzana": "Contenedor de residuos orgánicos.",  # Clasificación para residuos orgánicos
    "pilas": "Punto limpio o tienda de reciclaje especializado.",  # Clasificación para pilas
}

# Diccionario para el tiempo de descomposición de objetos
tiempo_descomposicion = {
    "bolsa de plástico": "500 años.",  # Tiempo de descomposición para bolsas de plástico
    "lata de refresco": "200 años.",  # Tiempo de descomposición para latas
    "papel": "2 a 6 semanas.",  # Tiempo de descomposición para papel
    "vidrio": "4,000 años.",  # Tiempo de descomposición para vidrio
}

# Lista de información sobre energía renovable
energia_renovable = [
    "La energía solar es una fuente de energía renovable que se obtiene del sol.",  # Información sobre energía solar
    "La energía eólica se genera utilizando el viento para producir electricidad.",  # Información sobre energía eólica
    "La energía hidroeléctrica se produce a partir del movimiento del agua.",  # Información sobre energía hidroeléctrica
    "La biomasa es una fuente de energía renovable que se obtiene de materiales orgánicos.",  # Información sobre biomasa
    "La energía geotérmica se obtiene del calor interno de la Tierra.",  # Información sobre energía geotérmica
]

# Función para sugerir una idea de manualidad aleatoria
def sugerir_manualidad():
    return random.choice(manualidades)  # Seleccionar y devolver una idea aleatoria de la lista

# Función para clasificar un residuo
def clasificar_residuo(objeto):
    return clasificacion_residuos.get(objeto.lower(), "No tengo información sobre ese objeto.")  # Buscar la clasificación del residuo

# Función para obtener el tiempo de descomposición de un objeto
def tiempo_descomposicion_objeto(objeto):
    return tiempo_descomposicion.get(objeto.lower(), "No tengo información sobre ese objeto.")  # Buscar el tiempo de descomposición

# Función para obtener información aleatoria sobre energía renovable
def obtener_energia_renovable():
    return random.choice(energia_renovable)  # Seleccionar y devolver información aleatoria de la lista

# Configuración del bot

# Crear un objeto Intents para especificar los permisos del bot
intents = discord.Intents.default()  # Crear un objeto de intents con permisos básicos
intents.message_content = True  # Habilitar el permiso para leer el contenido de los mensajes

# Crear una instancia del bot con el prefijo de comando "$" y los intents especificados
bot = commands.Bot(command_prefix="$", intents=intents)

# Evento que se ejecuta cuando el bot está listo y conectado
@bot.event
async def on_ready():
    print(f"{bot.user} se ha conectado a Discord!")  # Imprimir un mensaje en la consola indicando que el bot está listo

# Comando para sugerir una idea de manualidad
@bot.command('manualidad')
async def manualidad(ctx):
    idea = sugerir_manualidad()  # Obtener una idea de manualidad aleatoria
    await ctx.send(f"🧵 Idea de manualidad: {idea}")  # Enviar la idea al canal de Discord

# Comando para clasificar un residuo
@bot.command('clasificar')
async def clasificar(ctx, *, objeto: str):
    respuesta = clasificar_residuo(objeto)  # Clasificar el residuo proporcionado
    await ctx.send(f"♻️ Clasificación: {respuesta}")  # Enviar la clasificación al canal de Discord

# Comando para obtener el tiempo de descomposición de un objeto
@bot.command('descomposicion')
async def descomposicion(ctx, *, objeto: str):
    tiempo = tiempo_descomposicion_objeto(objeto)  # Obtener el tiempo de descomposición del objeto
    await ctx.send(f"⏳ Tiempo de descomposición: {tiempo}")  # Enviar el tiempo al canal de Discord

# Comando para obtener información sobre energía renovable
@bot.command('energia')
async def energia(ctx):
    info = obtener_energia_renovable()  # Obtener información aleatoria sobre energía renovable
    await ctx.send(f"🔋 Información sobre energía renovable: {info}")  # Enviar la información al canal de Discord

# Función para generar el mensaje de ayuda
def get_help_message():
    help_message = (
        "*Lista de comandos disponibles:*\n"
        "$manualidad - Sugiere una idea de manualidad.\n"
        "$clasificar <objeto> - Clasifica un residuo.\n"
        "$descomposicion <objeto> - Muestra el tiempo de descomposición de un objeto.\n"
        "$energia - Muestra información sobre energía renovable.\n"
        "$idea - Muestra ideas para disminuir la contaminacion hecha por uno.\n"
        "$helpy - Muestra esta lista de comandos.\n"
    )
    return help_message  # Devolver el mensaje de ayuda

# Comando para mostrar la lista de comandos disponibles
@bot.command('helpy')
async def help_command(ctx):
    help_message = get_help_message()  # Generar el mensaje de ayuda
    await ctx.send(help_message)  # Enviar el mensaje de ayuda al canal de Discord

idea_message = [
    "Recicla, encuentra nuevos usos para cosas que ya no uses",
    "Reduce el uso de plásticos (usa bolsas reutilizables y evita productos de un solo uso",
    "Elige productos con menos químicos o con empaques reciclables",
    "Usa el transporte público o camina para reducir las polucion",
    "Informa a otros al compartir consejos ecológicos con amigos, familia o en redes sociales.",
    "Cuida de los animales, los animales tambien son parte del medioambiente"
    ]
def sugerir_idea():
    return random.choice(idea_message)

@bot.command('idea')
async def idea(ctx):
    idea2 = sugerir_idea()  
    await ctx.send(f"{idea2}")


# Iniciar el bot con el token especificado en el archivo de configuración settings.py
bot.run(settings["TOKEN"])  # Ejecutar el bot utilizando el token