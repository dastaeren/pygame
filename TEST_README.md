# Test Documentation

This documentation provides a detailed description of the resources used to develop the test cases for the game.

## Resources

- Pygame: A set of Python modules designed for writing video games.
- unittest: A built-in Python library for creating and running test cases.
- MagicMock: A class from the unittest.mock module that can be used to replace parts of your system under test and make assertions about how they have been used.

## Justification for the use of resources
Using Pygame provides functionalities for creating games in Python. It includes modules for graphics, sound, and even networking, which are essential for our game.

Using unittest and MagicMock allow to create automated tests for our game. This ensures that the game works as expected and helps us to catch bugs early.

## Test Cases

Here are the test cases developed in the game:

- `test_pygame_initialization`: This test case checks if Pygame is initialized correctly.
- `test_screen_creation`: This test case checks if the game screen is created correctly.
- `test_image_loading`: This test case checks if the game images are loaded correctly.
- `test_sound_loading`: This test case checks if the game sounds are loaded correctly.
- `test_sound_playing`: This test case checks if the game sounds are played correctly.

