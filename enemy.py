import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, enemy_images):
        self.image = random.choice(enemy_images)
        
        # Ajuste: a posição 'x' do inimigo será 0 ou a largura da tela (extremidades), e a posição 'y' será aleatória entre 50 e metade da tela
        self.rect = self.image.get_rect(center=(random.choice([0, screen_width]), random.randint(50, screen_height // 2)))
        
        # Atributos de velocidade e chance de tiro, variando conforme o tipo de inimigo
        if self.image == enemy_images[0]:  # enemy1
            self.speed = random.randint(1, 3)  # Velocidade mais lenta
            self.shoot_chance = 0.025  # Menos chance de atirar
            self.points = 100
            self.bullet_image = "tiroenemy1.png"
        elif self.image == enemy_images[1]:  # enemy2
            self.speed = random.randint(3, 6)  # Velocidade normal
            self.shoot_chance = 0.05  # Chance de tiro padrão
            self.points = 130
            self.bullet_image = "tiroenemy2.png"
        else:  # enemy3
            self.speed = random.randint(4, 9)  # Velocidade mais rápida
            self.shoot_chance = 0.075  # Maior chance de tiro
            self.points = 185
            self.bullet_image = "tiroenemy3.png"

        self.direction = 1 if self.rect.centerx == 0 else -1  # Se começa na esquerda (0), vai para a direita, e vice-versa

    def move(self):
        self.rect.x += self.speed * self.direction  # Movendo para a esquerda ou direita

    def shoot(self):
        return EnemyBullet(self.rect.centerx, self.rect.bottom, self.bullet_image)  # Usando imagem diferente para cada tipo de inimigo

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyBullet:
    def __init__(self, x, y, bullet_image):
        self.image = pygame.image.load(bullet_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
