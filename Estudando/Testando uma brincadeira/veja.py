import win32com.client
import random

voz = win32com.client.Dispatch("SAPI.SpVoice")

frases = [
    "Cadê o trailer",
    "Já passou da hora",
    "Lança logo isso",
]

print("inclusive me lembrei de uma coisa")
pergunta = str(input())

if pergunta:
    while True:
        print("Cadê o trailer?")
        voz.Speak(random.choice(frases))

    




