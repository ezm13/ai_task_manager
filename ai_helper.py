import random

# --- MODO LOCAL AVANZADO (sin conexión a OpenAI) ---
CATEGORIAS = [
    "trabajo",
    "aprendizaje",
    "salud",
    "organización personal",
    "finanzas",
    "entretenimiento",
]

# Memoria local temporal
memoria_usuario = {
    "nombre": None,
    "ultima_categoria": None,
    "ultimas_tareas": [],
    "estado_animo": "neutro",
}

def analizar_tarea(texto):
    """Analiza el texto y devuelve una categoría y confianza simulada."""
    categoria = random.choice(CATEGORIAS)
    confianza = round(random.uniform(70, 95), 2)
    memoria_usuario["ultima_categoria"] = categoria
    memoria_usuario["ultimas_tareas"].append(texto)
    if len(memoria_usuario["ultimas_tareas"]) > 10:
        memoria_usuario["ultimas_tareas"].pop(0)
    return categoria, confianza


def responder_asistente(mensaje):
    """Simula respuestas naturales del asistente en modo local."""
    mensaje = mensaje.lower().strip()

    # --- Capturar nombre ---
    if "me llamo" in mensaje:
        nombre = mensaje.split("me llamo")[-1].strip().capitalize()
        memoria_usuario["nombre"] = nombre
        return f"¡Encantado, {nombre}! 😄 Guardaré tu nombre para futuras sesiones."

    # --- Consultar nombre ---
    if "quién soy" in mensaje:
        if memoria_usuario["nombre"]:
            return f"Eres {memoria_usuario['nombre']} 😎, y hasta ahora has añadido {len(memoria_usuario['ultimas_tareas'])} tareas."
        return "Aún no me has dicho tu nombre. Puedes decirme: 'me llamo Eroz'."

    # --- Estado emocional ---
    if any(x in mensaje for x in ["cansado", "agotado", "estresado"]):
        memoria_usuario["estado_animo"] = "agotado"
        return "💆 Parece que tuviste un día largo. Tómate un descanso o haz algo que disfrutes."

    if any(x in mensaje for x in ["feliz", "motivado", "bien"]):
        memoria_usuario["estado_animo"] = "feliz"
        return "😄 ¡Excelente! Me alegra verte con buena energía."

    # --- Pedir tareas ---
    if "qué tareas tengo" in mensaje:
        if memoria_usuario["ultimas_tareas"]:
            lista = "\n".join(f"• {t}" for t in memoria_usuario["ultimas_tareas"])
            return f"🗓️ Estas son tus últimas tareas:\n{lista}"
        else:
            return "Aún no tienes tareas guardadas."

    # --- Saludo inicial ---
    if mensaje in ["hola", "hey", "buenas", "saludos"]:
        if memoria_usuario["nombre"]:
            return f"👋 ¡Hola {memoria_usuario['nombre']}! ¿Listo para planificar tu día?"
        else:
            return "👋 ¡Hola! Soy tu asistente IA local. ¿Listo para planificar tu día?"

    # --- Agradecimiento ---
    if any(x in mensaje for x in ["gracias", "te agradezco"]):
        return "😊 ¡De nada! Me alegra ayudarte."

    # --- Default: analiza y clasifica ---
    categoria, confianza = analizar_tarea(mensaje)
    return f"📊 Parece relacionado con **{categoria}** ({confianza}%). ¿Quieres que lo agregue como tarea?"
