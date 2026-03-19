import palavras
import write
from time import sleep
write.line()
write.title('JOGO DA FORCA.')
write.line()
palavra = palavras.sortear_palavra().upper()
oculta = palavras.palavra_oculta(palavra)
usadas = []
print(palavra)
vidas = 6
while True:
    while True:
        for display in oculta:
            print(display, end=' ')
        print('!')
        if '_' not in oculta:
            break
        print(f'{vidas} vidas restantes!')
        write.line()
        if vidas == 0:
            break
        palpite = str(input('Digite seu palpite: ')[0]).upper()
        write.line()
        acerto = False
        for pos, letra in enumerate(palavra):
            if palpite in letra and palpite not in usadas:
                oculta[pos] = palpite
                acerto = True
        if acerto is False:
            vidas -= 1
            print('Você errou! -1 vida.')
        else:
            print('Você acertou o palpite!')
            usadas.append(palpite)
        write.line()
    write.line()
    if vidas > 0:
        write.title('VOCÊ VENCEU!')
    else:
        write.title('VOCÊ PERDEU!')
    write.line()
    decidir = ''
    while decidir not in ['S', 'N']:
        decidir = str(input('Deseja continuar[S/N]?')[0]).upper()
    if decidir == 'N':
        write.line()
        write.title('OBRIGADO POR JOGAR!')
        write.line()
        break
    else:
        vidas = 6
        palavra = palavras.sortear_palavra().upper()
        oculta = palavras.palavra_oculta(palavra)
        usadas = []
        write.line()
        write.title('JOGO DA FORCA.')
        write.line()
        print(palavra)
        continue
