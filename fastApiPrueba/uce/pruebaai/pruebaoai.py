# EL TOKEN FUE CREADO POR CORREO PERSONAL DE GMAIL: edwindavid21v@gmail.com

import openai
from pydantic import BaseModel


   class Document(BaseModel):
    prompt:str

 def inference(prompt) -> str:
     openai.organization = 'org-2wJUCGKBvFD1KsyjlmtDw8yo'
     openai.api_key = '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'

    print('PROCESANDO EL PROGRAMA'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres el encargado de contar las vocales, cuentas las vocales de un texto que te pasen
            E.G: hola mundo
            -El texto hola mundo tiene la cantidad de 4 vocales"""},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    #Para la cantidad de tokens que usa
    total_tokens = completion.usage.total_tokens

    print('FINALIZACIÓN DEL PROGRAMA'.center(40, '-'))
    return [content, total_tokens]










