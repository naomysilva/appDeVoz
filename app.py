from winsound import PlaySound
import gtts
from playsound import playsound

with open('frase.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha,lang='pt-BR')
        frase.save('ola.mp3')
        PlaySound('ola.mp3')