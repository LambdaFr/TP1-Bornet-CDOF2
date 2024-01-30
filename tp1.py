import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 700, 700  # agrandissement de l'image (issue 2)
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
apple = (
    random.randint(0, (width - block_size) // block_size) * block_size,
    random.randint(0, (height - block_size) // block_size) * block_size,
)

# Initialisation du score
score = 0

# Contrôle de l'état du jeu (issue 3)
running = False

# Début du jeu (issue 3)
start_ticks = 0

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion du clic de souris (issue 3)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not running:
                # Début du jeu si le bouton est cliqué et que le jeu n'est pas en cours
                running = True
                start_ticks = pygame.time.get_ticks()
                score = 0
                snake = [(width // 2, height // 2)]
                snake_direction = (block_size, 0)
                apple = (
                    random.randint(0, (width - block_size) // block_size) * block_size,
                    random.randint(0, (height - block_size) // block_size) * block_size,
                )

    if running:
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
            new_head[0] < 0 or new_head[0] >= width
            or new_head[1] < 0 or new_head[1] >= height
        ):
            running = False

        snake.insert(0, new_head)

        # Vérification des collisions avec la pomme
        if new_head == apple:
            score += 1
            # Générer une nouvelle position pour la pomme qui ne soit pas sur le serpent (issue 1)
            while True:
                apple = (
                    random.randint(0, (width - block_size) // block_size) * block_size,
                    random.randint(0, (height - block_size) // block_size) * block_size,
                )
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

        # Affichage du score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))

        # Affichage du temps écoulé en secondes (issue 3)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        time_text = font.render(f"Temps écoulé: {elapsed_time} s", True, white)
        screen.blit(time_text, (width - 220, 10))

    else:
        font = pygame.font.Font(None, 36)
        # Affichage du bouton de démarrage lorsque le jeu n'est pas en cours (issue 3)
        pygame.draw.rect(screen, (0, 255, 0), (width // 4, height // 2, width // 2, 50))
        start_text = font.render("Commencer", True, black)
        screen.blit(start_text, (width // 3, height // 2 + 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Régulation de la vitesse du serpent
    pygame.time.Clock().tick(speed)
