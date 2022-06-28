import pygame.draw
from constantes import *
from elemento_jogo import ElementoJogo
from pacman import Pacman
from fantasma import Fantasma


class Cenario(ElementoJogo):

    def __init__(self, tamanho, pacman):
        self.pacman = pacman
        self.moviveis = []
        self.tamanho = tamanho
        self.pontos = 0
        self.vidas = 5
        self.estado = JOGANDO
        self.matriz = MATRIZ

    def get_direcoes(self, linha, coluna):
        direcoes = []

        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(ACIMA)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(ABAIXO)
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)

        return direcoes

    def adicionar_movivel(self, objeto):
        self.moviveis.append(objeto)

    def pintar_linha(self, tela, numero_linha, liha):
        for numero_coluna, coluna in enumerate(liha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = PRETO

            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)

            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + half, y + half), self.tamanho // 10, 0)

    def pintar_score(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f'Score: {self.pontos}', True, AMARELO)
        img_vidas = fonte.render(f'Vidas: {self.vidas}', True, AMARELO)
        tela.blit(img_vidas, (pontos_x, 25))
        tela.blit(img_pontos, (pontos_x, 50))

    def pintar(self, tela):
        if self.estado == JOGANDO:
            self.pintar_jogando(tela)
        elif self.estado == PAUSADO:
            self.pintar_jogando(tela)
            self.pintar_pausado(tela)
        elif self.estado == GAME_OVER:
            self.pintar_jogando(tela)
            self.pintar_game_over(tela)
        elif self.estado == VITORIA:
            self.pintar_jogando(tela)
            self.pintar_vitoria(tela)

    @staticmethod
    def pintar_texto_centro(tela, texto):
        texto_img = fonte.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))

    def pintar_game_over(self, tela):
        self.pintar_texto_centro(tela, 'G A M E   O V E R')

    def pintar_vitoria(self, tela):
        self.pintar_texto_centro(tela, 'V O C Ê   V E N C E U ! ! !')

    def pintar_pausado(self, tela):
        self.pintar_texto_centro(tela, 'P A U S A D O')

    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)

        self.pintar_score(tela)

    def processar_eventos(self, eventos):
        for i in eventos:
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    if self.estado == JOGANDO:
                        self.estado = PAUSADO
                    else:
                        self.estado = JOGANDO

    def calcular_regras(self):
        if self.estado == JOGANDO:
            self.calcular_regras_jogando()
        elif self.estado == PAUSADO:
            self.calcular_regras_pausado()
        elif self.estado == GAME_OVER:
            self.calcular_regras_game_over()
        elif self.estado == VITORIA:
            self.calcular_regras_vitoria()

    def calcular_regras_game_over(self):
        pass

    def calcular_regras_vitoria(self):
        pass

    def calcular_regras_pausado(self):
        pass

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao)

            direcoes = self.get_direcoes(lin, col)

            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and \
                    movivel.linha == self.pacman.linha and \
                    movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <= 0:
                    self.estado = GAME_OVER
                else:
                    self.pacman.linha = 1
                    self.pacman.coluna = 1
            else:
                if 0 <= col_intencao <= 28 and 0 <= lin_intencao <= 29 and \
                        self.matriz[lin_intencao][col_intencao] != 2:
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                        self.pontos += 1
                        self.matriz[lin][col] = 0
                        if self.pontos >= 306:
                            self.estado = VITORIA
                else:
                    movivel.recusar_movimento(direcoes)

    def recusar_movimento(self, direcoes):
        pass

    def aceitar_movimento(self):
        pass
