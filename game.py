import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the background image
room = pygame.image.load("room.jpg")
room = pygame.transform.scale(room, (560, 500))

# Set screen dimensions
WIDTH, HEIGHT = 560, 500

# Create the screen
screen = pygame.display.set_mode((560, 500))
room_surface = pygame.image.load('room.jpg')

# Set title of screen
pygame.display.set_caption("Eat the GumGum!")
font = pygame.font.Font(None, 50)

# Load images
luffy = pygame.image.load('luffy.png')

gumgum = pygame.image.load('gumgum.png')

# Scale Images
luffy = pygame.transform.scale(luffy, (130, 130))
gumgum = pygame.transform.scale(gumgum, (70, 120))

# Initialize position of gumgum
gumgum_x = random.randint(0, WIDTH - 100)
gumgum_y = random.randint(0, HEIGHT - 100)

# Initialize position of luffy
luffy_x = WIDTH / 2 - 10
luffy_y = HEIGHT / 2 - 10

# Initialize score
score = 0

# Set the initial time
initial_time = pygame.time.get_ticks()



# Game loop
running = True
start_time = time.time()
while running:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Get events from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and luffy_x > 0:
        luffy_x -= 5
    if keys[pygame.K_RIGHT]:
        luffy_x += 5
    if keys[pygame.K_UP] and luffy_y > 0:
        luffy_y -= 5
    if keys[pygame.K_DOWN]:
        luffy_y += 5

    # Draw the background image
    screen.blit(room, (0, 0))

    # Draw the luffy
    screen.blit(luffy, (luffy_x, luffy_y))

    # Draw the gumgum
    screen.blit(gumgum, (gumgum_x, gumgum_y))

    # Check for collision between luffy and gumgum
    if luffy_x + 100 > gumgum_x and luffy_x < gumgum_x + 100 and luffy_y + 100 > gumgum_y and luffy_y < gumgum_y + 100:
        score += 1
        gumgum_x = random.randint(0, WIDTH - 100)
        gumgum_y = random.randint(0, HEIGHT - 100)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Set the current time
    current_time = pygame.time.get_ticks()

    # Check if one minute has passed
    if current_time - initial_time >= 60000:
        print("One minute has passed.")
        initial_time = current_time

        # Draw the timer
    text = font.render(f"Time: {int((current_time - initial_time) / 1000)} seconds", True, (255, 255, 255))
    screen.blit(text, (10, 50))



    # Update the display
    pygame.display.flip()

pygame.quit()