import openai
from flask import current_app

def generar_explicacion(nivel, area, tema):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    prompt = f"Explica el tema {tema} para un alumno de {nivel} en el área de {area} con un lenguaje sencillo y ejemplos concretos."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
