# Definicion de librerias

import sys
import openai

# Se define la clave de la API de OpenAI
openai.api_key = "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"

# Esta es la inicialización de las variables y otros parámetros
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"
# Esta variable determina la inicialización del while
contestacion = True

# Lista para almacenar todas las consultas realizadas por el usuario
consulta_buffer = []

#
if ((len(sys.argv)) > 0):
    if "--convers" in sys.argv:
        contestacion
    else:
        print('No ha ingresado el parametro correcto')
        print("Gracias por usar la API.")
        contestacion = False
else:
    contestacion = False
    print('No se ha activado el modo conversacion.')
    print("Gracias por usar la API.")

# comienzo del bucle iterativo
while contestacion:
    try:
        PROMPT = input("You: ")
    except:
        print("Error al aceptar la consulta del usuario.")

    # Se trata la consulta del usuario y se agrega al buffer
    try:
        if PROMPT != "":
            consulta_buffer.append(PROMPT)
    except:
        print("Error al almacenar la consulta en el buffer.")

    # una cadena de texto con todas las consultas almacenadas en el buffer
    consulta_concatenada = "\n".join(consulta_buffer)

    # Se configura el modelo y el prompt con la cadena concatenada
    try:
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=consulta_concatenada,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=STOP
        )
    except:
        print("Error al tratar la consulta del usuario.")

    # Se analiza si el usuario ingreso una consulta

    if PROMPT == "exit":
            print("Gracias por usar la API.")
            break

    try:
        if (len(PROMPT)) > 0:
            print("chatGPT:", completion.choices[0].text)
        else:
            print("chatGPT: No se ha ingresado una consulta.")
    except AttributeError:
        print("chatGPT: Error al acceder al atributo 'choices' del objeto 'completion'.")

    if PROMPT == "exit":
        contestacion = False