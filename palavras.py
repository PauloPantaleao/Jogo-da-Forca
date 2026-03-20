from random import choice
palavras = [
    'abacaxi', 'melancia', 'morango', 'uva', 'manga',
    'laranja', 'limao', 'pera', 'maca', 'banana',
    'framboesa', 'acerola', 'goiaba', 'maracuja', 'caju',
    'abacate', 'kiwi', 'ameixa', 'cereja', 'figo',
    'pitanga', 'carambola', 'graviola', 'jabuticaba', 'coco'
]
def sortear_palavra():
    return choice(palavras)
def palavra_oculta(palavra):
    oculta = ['_' for l in palavra]
#    for l in range(0, len(palavra)):
#        oculta.append('_')
    return oculta
