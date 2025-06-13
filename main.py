import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_img = pygame.image.load("assets/player-removebg-preview.png")
alien_img = pygame.image.load("assets/alien-removebg-preview.png")
bullet_img = pygame.image.load("assets/peluru.png")

player_img = pygame.transform.scale(player_img, (60, 60))
alien_img = pygame.transform.scale(alien_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 30))

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 5
        self.bullets = []

    def draw(self):
        screen.blit(player_img, (self.x, self.y))
        for b in self.bullets:
            b.draw()

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 60:
            self.x += self.speed

    def shoot(self):
        bullet = Bullet(self.x + 25, self.y)
        self.bullets.append(bullet)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7

    def draw(self):
        screen.blit(bullet_img, (self.x, self.y))

    def move(self):
        self.y -= self.speed

class Alien:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = random.randint(-100, -40)
        self.speed = 1

    def draw(self):
        screen.blit(alien_img, (self.x, self.y))

    def move(self):
        self.y += self.speed

def tampilkan_game_over(score):
    font_game_over = pygame.font.SysFont(None, 60)
    text = font_game_over.render("GAME OVER", True, WHITE)
    text_score = font.render(f"Score: {score}", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(text_score, (WIDTH // 2 - text_score.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000)  # tunggu 3 detik

player = Player()
aliens = [Alien() for _ in range(5)]
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    player.move(keys)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()

    for bullet in player.bullets:
        bullet.move()

    for alien in aliens:
        alien.move()

    for alien in aliens:
        for bullet in player.bullets:
            if (
                bullet.x < alien.x + 50 and
                bullet.x + 10 > alien.x and
                bullet.y < alien.y + 50 and
                bullet.y + 30 > alien.y
            ):
                try:
                    player.bullets.remove(bullet)
                    aliens.remove(alien)
                    aliens.append(Alien())
                    score += 1
                except ValueError:
                    pass

    
        if alien.y > HEIGHT:
            tampilkan_game_over(score)
            running = False


    player.draw()
    for alien in aliens:
        alien.draw()
    skor_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(skor_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
