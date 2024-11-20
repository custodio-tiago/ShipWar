import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, enemy_images):
        self.image = random.choice(enemy_images)
        
        # Ajuste: a posição 'x' do inimigo será 0 ou a largura da tela (extremidades), e a posição 'y' será aleatória entre 50 e metade da tela
        self.rect = self.image.get_rect(center=(random.choice([0, screen_width]), random.randint(50, screen_height // 2)))
        
        self.speed = random.randint(3, 6)  # Aumentando a velocidade de movimento
        self.direction = 1 if self.rect.centerx == 0 else -1  # Se começa na esquerda (0), vai para a direita, e vice-versa

    def move(self):
        self.rect.x += self.speed * self.direction  # Movendo para a esquerda ou direita

    def shoot(self):
        return EnemyBullet(self.rect.centerx, self.rect.bottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyBullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("tiroenemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
