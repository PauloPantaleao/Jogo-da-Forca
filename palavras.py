from random import choice
palavras = ['abacaxi',
'melancia',
'coragem',
'borboleta',
'pular',
'esconder',
'laranja',
'curioso',
'caminhar',
'framboesa']
def sortear_palavra():
    return choice(palavras)
def palavra_oculta(palavra):
    oculta = []
    for l in range(0, len(palavra)):
        oculta.append('_')
    return oculta
