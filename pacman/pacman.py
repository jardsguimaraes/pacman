from constantes import *
import pygame.draw

from elemento_jogo import ElementoJogo


class Pacman(ElementoJogo):

    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.velo_x = 0
        self.velo_y = 0
        self.raio = self.tamanho // 2
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.abertura = 0
        self.velocidade_abertura = 1

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.velo_x
        self.linha_intencao = self.linha + self.velo_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velo_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.velo_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.velo_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.velo_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    self.velo_x = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    self.velo_y = 0

    # Função paenas para fins academico
    def processar_eventos_mouse(self, eventos):
        delay = 100
        for i in eventos:
            if i.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = i.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

    def aceitar_movimento(self):
        self.coluna = self.coluna_intencao
        self.linha = self.linha_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna

    def pintar(self, tela):
        # Desenhar corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Animação da Boca do Pacman
        self.abertura += self.velocidade_abertura
        if self.abertura > self.raio:
            self.velocidade_abertura = -1
        if self.abertura <= 0:
            self.velocidade_abertura = 1

        # Desenhar boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.abertura)
        labio_inferior = (self.centro_x + self.raio, self.centro_y + self.abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Desenhar oho
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)
