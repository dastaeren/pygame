import pygame
import random
import time
from pygame import mixer

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

# Welcome text
welcome_text_font = pygame.font.Font(None,30)
welcome_text = welcome_text_font.render("Welcome!",True, (225,255,225))
welcome_text_rect = welcome_text.get_rect()
welcome_text_rect.center = (280,230)

welcome_text_font1 = pygame.font.Font(None,23)
welcome_text1 = welcome_text_font1.render("Let's see how much luffy can eat gum-gum fruit in one minute",True, (225,225,25))
welcome_text_rect1 = welcome_text1.get_rect()
welcome_text_rect1.center = (280,250)

# Display the welcome text
screen.blit(welcome_text, welcome_text_rect,)
screen.blit(welcome_text1, welcome_text_rect1,)
pygame.display.flip()
pygame.time.delay(3000)

# Load images
luffy = pygame.image.load('luffy.png')
gumgum = pygame.image.load('gumgum.png')

# Scale Images
luffy = pygame.transform.scale(luffy, (150, 130))
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

# Load sound
mixer.music.load('bites.mp3')

# Game loop
running = True
start_time = time.time()
while running:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        running = False

    # Get events from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and luffy_x > 0:
        luffy_x -= 5
    if keys[pygame.K_RIGHT] and luffy_x < WIDTH - 150:
        luffy_x += 5
    if keys[pygame.K_UP] and luffy_y > 0:
        luffy_y -= 5
    if keys[pygame.K_DOWN] and luffy_y < HEIGHT - 130:
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

        # Play the sound when luffy eats gum gum
        mixer.music.play()

    # Display the score
    font = pygame.font.Font(None, 30)
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
    screen.blit(text, (10, 40))

   # Update the screen
    pygame.display.flip()

pygame.quit()

# Display score
print('Your score is:', score)





import unittest
import pygame
from unittest.mock import patch

class TestGame(unittest.TestCase):
   @patch('pygame.init')
   def test_pygame_initialization(self, mock_pygame_init):
       # Initialize Pygame
       pygame.init()
       # Assert that pygame.init() was called
       mock_pygame_init.assert_called_once()

   @patch('pygame.display.set_mode')
   def test_screen_creation(self, mock_display_set_mode):
       # Create the screen
       pygame.display.set_mode((560, 500))
       # Assert that pygame.display.set_mode() was called with the correct arguments
       mock_display_set_mode.assert_called_once_with((560, 500))

   @patch('pygame.image.load')
   def test_image_loading(self, mock_image_load):
       # Load images
       pygame.image.load('luffy.png')
       pygame.image.load('gumgum.png')
       # Assert that pygame.image.load() was called with the correct arguments
       mock_image_load.assert_any_call('luffy.png')
       mock_image_load.assert_any_call('gumgum.png')

   @patch('pygame.mixer.music.load')
   def test_sound_loading(self, mock_music_load):
       # Load sound
       pygame.mixer.music.load('bites.mp3')
       # Assert that pygame.mixer.music.load() was called with the correct arguments
       mock_music_load.assert_called_once_with('bites.mp3')

   @patch('pygame.mixer.music.play')
   def test_sound_playing(self, mock_music_play):
       # Play the sound when luffy eats gum gum
       pygame.mixer.music.play()
       # Assert that pygame.mixer.music.play() was called
       mock_music_play.assert_called_once()

if __name__ == '__main__':
   unittest.main()
