import palavras
import write
from time import sleep
write.line()
write.title('JOGO DA FORCA.')
write.line()
palavra = palavras.sortear_palavra().upper()
oculta = palavras.palavra_oculta(palavra)
usadas = []
vidas = 6
sleep(2)
while True:
    while True:
        for display in oculta:
            print(display, end=' ')
        print('!')
        sleep(1)
        if '_' not in oculta:
            break
        print(f'{vidas} vidas restantes!')
        write.line()
        if vidas == 0:
            for revelar in palavra:
                print(revelar, end=' ')
            write.line()
            break
        sleep(1)
        palpite = str(input('Digite seu palpite: ')[0]).upper()
        write.line()
        sleep(1)
        acerto = 0
        for pos, letra in enumerate(palavra):
            if palpite in usadas:
                acerto = -1
                break
            elif palpite in letra:
                oculta[pos] = palpite
                acerto += 1
        if acerto == 0:
            vidas -= 1
            print('Você errou! -1 vida.')
        elif acerto > 0:
            print('Você acertou o palpite!')
            usadas.append(palpite)
        else:
            print('Já tem essa letra!')
        write.line()
        sleep(2)
    sleep(2)
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
        sleep(2)
        write.line()
        write.title('OBRIGADO POR JOGAR!')
        write.line()
        break
    else:
        vidas = 6
        palavra = palavras.sortear_palavra().upper()
        oculta = palavras.palavra_oculta(palavra)
        usadas = []
        sleep(2)
        write.line()
        write.title('JOGO DA FORCA.')
        write.line()
        continue
