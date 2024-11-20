import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, enemy_images):
        self.image = random.choice(enemy_images)  # Seleciona uma imagem aleatória
        self.image = pygame.transform.scale(self.image, (70, 70))  # Tamanho fixo para as naves inimigas
        self.rect = self.image.get_rect()

        # Escolher se o inimigo começa à esquerda ou à direita
        self.direction = random.choice(['left', 'right'])

        if self.direction == 'left':
            self.rect.x = -self.rect.width  # Spawn à esquerda da tela
            self.speed = random.randint(1, 3)  # Velocidade aleatória
        else:
            self.rect.x = screen_width + self.rect.width  # Spawn à direita da tela
            self.speed = random.randint(-3, -1)  # Velocidade aleatória (negativa para a direção certa)

        self.rect.y = random.randint(0, screen_height - self.rect.height)  # Posição vertical aleatória

    def move(self):
        # Move o inimigo para a direção correta
        self.rect.x += self.speed

    def shoot(self):
        return EnemyBullet(self.rect.centerx, self.rect.bottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyBullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("tiroenemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 5))  # Tamanho do tiro inimigo
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
