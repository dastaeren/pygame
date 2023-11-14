import unittest
import pygame
from unittest.mock import patch, MagicMock

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
