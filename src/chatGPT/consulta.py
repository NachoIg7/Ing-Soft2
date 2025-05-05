"""
Este script permite al usuario realizar consultas a la API de ChatGPT
controlando errores en cada etapa del proceso. Además, permite recuperar
la última consulta con la tecla de flecha ↑ para editarla y reenviarla.
"""
#Importamos librerias necesarias para el desarrollo
import os
import sys
import readline # recuperar la ultima consulta realizada con el cursor, en la misma consola".
from openai import OpenAI
import openai

# ininiclizamos el cliente de la API
CLIENT = OpenAI()

#intentamos obtener la API key
try:
    openai.api_key = os.getenv ("OPENAI_API_KEY") # carga la Api desde el sistema
    if openai.api_key is None:
        # si no se encuentra la api, aparece un error
        raise ValueError (" La API key no esta configurada correctamente.")
except ValueError as e:
    print (f"Error al configurar la AKI key: {e}")
    sys.exit (1) # salimos del programa si no se puede obtener la API key


# intentamos obtener la consulta del usuario
try:
    CONSULTA = input ("Ingresa tu consulta : ")

    # uardamos la consulta en el historial para usar flecha hacia arriba
    if CONSULTA.strip():
        readline.add_history(CONSULTA)
        print (f"Yoy: {CONSULTA}")
    else:
        print("No ingresaste una consulta")
        sys.exit(1)
except Exception as e:
    print (f"Error al obtener la consulta del usuario: {e}")
    sys.exit(1) # Salir si hay un error al tomar la consulta del usuario 

#preparacion y llamada a la API
try:
    # Definimos el contexto, proposito y la consulta
    CONTEXT = "Sos un asistente útil que responde preguntas de forma clara y concisa."
    USERTASK = "Quiero obtener una respuesta a la siguiente consulta."
    USERQUERY = CONSULTA.strip()
    print(" Enviando consulta a la API...")

    # Realizamos la llamada a la API de OpenAi para obtener una respuesta.
    RESPONSE = CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[
                        {
                        "role": "system",
                        "content": CONTEXT }, # Mensaje que establece el contexto para el modelo.
                        { 
                        "role": "user",
                        "content" : USERTASK }, # Mensaje que define el proposito de la consulta
                        {
                        "role": "user",
                        "content": USERQUERY } # emnsaje con la consulta real del usuario.
                        ],
                        temperature=1,
                        max_tokens=16384,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
     # Verificar si hay contenido
    if RESPONSE.choices and RESPONSE.choices[0].message.content:
        respuesta = RESPONSE.choices[0].message.content # obtenemos la respuesta
        print(f" ChatGPT: {respuesta}") # Mostramos la respuesta
    else:
        print(" No se recibió respuesta del modelo.")

except Exception as e:
    print(f" Error al generar respuesta: {e}")
    sys.exit(1)

# intentamos obtener y mostrar la respuesta de la API.
try:
    #si la respuesta esta disponible, la mostramos.
    respuesta = RESPONSE.choices[0].message.content
    print (f"ChatGPT: {respuesta}")

    # Guadamos la respuesta en un JSON
    jsonStr = respuesta

    #*--- post process response message to eliminate garbage from the JSON file.
    jsonStr=RESPONSE.choices[0].message.content
except Exception as e:
    # Si hay un error al obtener y mostrar la respuesta de la API, imprime el error y termina el programa
    print (f"Error al obtener y mostrar la respuesta de la API: {e}")
    sys.exit(1) # Salir si hay un error al obtener y mostrar la respuesta