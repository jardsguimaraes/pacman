from constantes import *
from pacman import Pacman
from cenario import Cenario
from fantasma import Fantasma

pygame.init()

if __name__ == "__main__":
    pacman = Pacman(SIZE)
    blinky = Fantasma(VERMELHO, SIZE)
    inky = Fantasma(CIANO, SIZE)
    clyde = Fantasma(LARANJA, SIZE)
    pinky = Fantasma(ROSA, SIZE)
    cenario = Cenario(SIZE, pacman)
    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)

    while True:
        # calcula as regras
        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

        # Pintar a tela
        SCREEN.fill(PRETO)
        cenario.pintar(SCREEN)
        pacman.pintar(SCREEN)
        blinky.pintar(SCREEN)
        inky.pintar(SCREEN)
        clyde.pintar(SCREEN)
        pinky.pintar(SCREEN)
        pygame.display.update()
        pygame.time.delay(150)

        # Captura os eventos
        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)
