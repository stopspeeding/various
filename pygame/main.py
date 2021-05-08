import pygame
import random
import math

from pygame import mixer

# Initializes pygame
pygame.init()

# Creates window
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('bg.jpg')

# BGM
mixer.music.load('bgm.wav')
mixer.music.play(-1)

# Window name and icon
pygame.display.set_caption("Pest Control")
icon = pygame.image.load('bz.ico')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
# Position
playerX = 370
playerY = 480
playerX_c = 0

# Boss
bossImg = pygame.image.load('boss.png')
# Position
bossX = 370
bossY = 50
bossX_c = 0.5

# Bullet ready/fire
bulletImg = pygame.image.load('bullet.png')
# Position
bulletX = 0
bulletY = 480
bulletX_c = 0
bulletY_c = 0.9
bullet_state = "ready"

# Boss hp
hp_value = 6
font = pygame.font.Font('Blacklisted.ttf', 32)

textX = 10
textY = 10

# Game end
end_font = pygame.font.Font('Blacklisted.ttf', 64)


def show_hp(x, y):
    hp = font.render("Roach Alt accounts left: " + str(hp_value), True, (255, 0, 0))
    screen.blit(hp, (x, y))


def game_end():
    end_text = font.render("DONATE TO BE UNBANNED", True, (139, 0, 0))
    screen.blit(end_text, (230, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def boss(x, y):
    screen.blit(bossImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def bCollision(bossX, bossY, bulletX, bulletY):
    distance = math.sqrt((math.pow(bossX - bulletX, 2)) + (math.pow(bossY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game
running = True
while running:

    screen.fill((128, 128, 100))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_c = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_c = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_s = mixer.Sound('bullet.wav')
                    bullet_s.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_c = 0

    # Player boundary
    playerX += playerX_c

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet path
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_c

    # Collision
    collision = bCollision(bossX, bossY, bulletX, bulletY)
    if collision:
        hit_s = mixer.Sound('hit.wav')
        hit_s.play()
        bulletY = 480
        bullet_state = "ready"
        hp_value -= 1
        bossX = random.randint(0, 735)
        bossY = random.randint(50, 150)

    # Boss boundary
    bossX += bossX_c

    if bossX <= 0:
        bossX_c = 0.6
    elif bossX >= 736:
        bossX_c = -0.6

    # Game end
    if hp_value == 0:
        game_end()

    player(playerX, playerY)
    boss(bossX, bossY)
    show_hp(textX, textY)
    pygame.display.update()
