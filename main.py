import pygame
import sys
import random
from player import Player
from enemy import Enemy

pygame.init()

# Configurações
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Inicialização
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Simples")
clock = pygame.time.Clock()

# Fundo do jogo
background = pygame.image.load("universe.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Pré-carregar imagens
enemy_images = [pygame.image.load(f"enemy{i}.png").convert_alpha() for i in range(1, 4)]
enemy_images = [pygame.transform.scale(img, (30, 30)) for img in enemy_images]

# Game loop
def main():
    player = Player(WIDTH // 2, HEIGHT - 70)
    enemies = []
    bullets = []
    enemy_bullets = []
    score = 0
    spawn_timer = 0
    game_over = False

    while True:
        screen.blit(background, (0, 0))  # Renderiza o fundo
        delta_time = clock.tick(FPS)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        if not game_over:
            player.move(keys, WIDTH, HEIGHT)

        # Spawn de inimigos
        spawn_timer += delta_time
        if spawn_timer >= random.randint(1000, 3000) and len(enemies) < 15:
            spawn_timer = 0
            enemies.append(Enemy(WIDTH, HEIGHT, enemy_images))

        # Atualizar e desenhar objetos
        if not game_over:
            # Atualizar tiros do player
            for bullet in bullets[:]:
                bullet.move()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            # Atualizar inimigos
            for enemy in enemies[:]:
                enemy.move()
                if enemy.rect.right < 0 or enemy.rect.left > WIDTH:
                    enemies.remove(enemy)
                if random.random() < 0.01:
                    enemy_bullets.append(enemy.shoot())

            # Atualizar tiros dos inimigos
            for e_bullet in enemy_bullets[:]:
                e_bullet.move()
                if e_bullet.rect.top > HEIGHT:
                    enemy_bullets.remove(e_bullet)

            # Colisões
            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 100

            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    game_over = True

            for e_bullet in enemy_bullets:
                if player.rect.colliderect(e_bullet.rect):
                    game_over = True

        # Renderizar
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for e_bullet in enemy_bullets:
            e_bullet.draw(screen)

        # Pontuação e Game Over
        score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = FONT.render("Game Over! Press R to Restart", True, (255, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main()

        pygame.display.flip()


if __name__ == "__main__":
    main()
