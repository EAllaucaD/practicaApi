import openai
from pydantic import BaseModel

openai.organization = 'org-2wJUCGKBvFD1KsyjlmtDw8yo'
openai.api_key = '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'


class Document(BaseModel):
    prompt: str = ''


def inference(prompt) -> str:
    openai.organization = 'org-2wJUCGKBvFD1KsyjlmtDw8yo'
    openai.api_key = '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'
    print('PROCESANDO'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un abogado, genera una explicación al tema que se te proporciona
            E.G: Leyes
            -Es como las reglas o normas  que las establece una autoridad superior"""},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('SE TERMINÓ DE PROCESAR'.center(40, '-'))
    return [content, total_tokens]
