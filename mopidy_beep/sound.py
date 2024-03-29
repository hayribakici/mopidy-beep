'''
Python module to play sounds.
'''

__all__ = (
    'play_sound',
)

from os import path, system

def play_sound(sound):
    '''
    Play sound via play.

    :param str sound: The name of the sound file
    '''
    file_path = path.join(path.dirname(__file__), 'sounds', sound)
    system('play -q {}'.format(file_path))
