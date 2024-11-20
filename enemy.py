import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, enemy_images):
        self.image = random.choice(enemy_images)
        self.rect = self.image.get_rect(center=(random.randint(0, screen_width), 0))
        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.y += self.speed

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
