#!/usr/bin/python
import openai

# Se define la clave de la API de OpenAI

openai.api_key = "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"

# [aquí va la inicialización de las variables y otros parámetros]

TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"
PROMPT="text"

# [otra lógica necesaria – el texto del prompt debe colocarse en userText]

# Se configura el modelo y el prompt

completion = openai.Completion.create(
    engine=MODEL_ENGINE,
    prompt=PROMPT,
    max_tokens=MAX_TOKENS,
    n=NMAX,
    top_p=TOP_P,
    frequency_penalty=FREQ_PENALTY,
    presence_penalty=PRES_PENALTY,
    temperature=TEMPERATURE,
    stop=STOP
)

print(completion.choices[0].text)


