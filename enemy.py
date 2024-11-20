import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height):
        images = ["enemy1.png", "enemy2.png", "enemy3.png"]
        self.image = pygame.image.load(random.choice(images))
        self.image = pygame.transform.scale(self.image, (70, 70))  # Redimensiona para 30x30
        spawn_side = random.choice(["left", "right"])
        if spawn_side == "left":
            self.rect = self.image.get_rect(left=0, top=random.randint(0, screen_height - 50))
            self.speed = random.randint(2, 4)
        else:
            self.rect = self.image.get_rect(right=screen_width, top=random.randint(0, screen_height - 50))
            self.speed = -random.randint(2, 4)

    def move(self):
        self.rect.x += self.speed

    def shoot(self):
        return BulletEnemy(self.rect.centerx, self.rect.bottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class BulletEnemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("tiroenemy.png")
        self.image = pygame.transform.scale(self.image, (5, 5))  # Redimensiona para 5x5
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)