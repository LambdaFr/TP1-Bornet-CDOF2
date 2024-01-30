import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 600, 600 #agrandissement de l'image (issue 2)
block_size = 20
speed = 8

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Initialisation de l'écran
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initialisation du serpent
snake = [(width // 2, height // 2)]
snake_direction = (block_size, 0)

# Initialisation de la pomme
apple = (random.randint(0, (width - block_size) // block_size) * block_size,
         random.randint(0, (height - block_size) // block_size) * block_size)

# Initialisation de la pomme (issue 2)
score = 0

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_direction != (block_size, 0):
        snake_direction = (-block_size, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-block_size, 0):
        snake_direction = (block_size, 0)
    elif keys[pygame.K_UP] and snake_direction != (0, block_size):
        snake_direction = (0, -block_size)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -block_size):
        snake_direction = (0, block_size)

    # Mise à jour de la position du serpent
    x, y = snake[0]
    new_head = (x + snake_direction[0], y + snake_direction[1])

    # Vérification des collisions avec les bords
    if (
        new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= height
    ):
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Vérification des collisions avec la pomme
    if new_head == apple:
        score += 1
        # Générer une nouvelle position pour la pomme qui ne soit pas sur le serpent (issue 1)
        while True:
            apple = (random.randint(0, (width - block_size) // block_size) * block_size,
                     random.randint(0, (height - block_size) // block_size) * block_size)
            if apple not in snake:
                break
    else:
        snake.pop()

    # Effacement de l'écran
    screen.fill(black)

    # Affichage de la pomme
    pygame.draw.rect(screen, red, (apple[0], apple[1], block_size, block_size))

    # Affichage du serpent
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], block_size, block_size))
    
    # Affichage du score (issue 2)
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.draw.rect(screen, red, (apple[0], apple[1], block_size, block_size))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Régulation de la vitesse du serpent
    pygame.time.Clock().tick(speed)
