import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PUBG Mini Shooter")

clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)
player_speed = 5

# Bullets
bullets = []

# Enemies
enemies = []

score = 0
font = pygame.font.SysFont(None, 30)

def spawn_enemy():
    x = random.randint(0, WIDTH-30)
    y = random.randint(0, HEIGHT-30)
    enemies.append(pygame.Rect(x, y, 30, 30))

spawn_event = pygame.USEREVENT
pygame.time.set_timer(spawn_event, 800)

running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == spawn_event:
            spawn_enemy()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(pygame.Rect(player.centerx, player.centery, 6, 6))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: player.x -= player_speed
    if keys[pygame.K_d]: player.x += player_speed
    if keys[pygame.K_w]: player.y -= player_speed
    if keys[pygame.K_s]: player.y += player_speed

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for enemy in enemies[:]:
        if enemy.colliderect(player):
            print("Game Over!")
            running = False

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1

    screen.fill((10,10,30))
    
    pygame.draw.rect(screen,(0,255,100),player)

    for bullet in bullets:
        pygame.draw.rect(screen,(255,255,0),bullet)

    for enemy in enemies:
        pygame.draw.rect(screen,(255,50,50),enemy)

    score_text = font.render("Kills: " + str(score),True,(255,255,255))
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()
