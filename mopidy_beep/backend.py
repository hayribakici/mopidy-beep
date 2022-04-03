'''
Python module for Mopidy Beep backend.
'''

__all__ = (
    'BeepBackend',
)

from logging import getLogger

import pykka

from mopidy import backend as backend
from mopidy import audio as audio
from .sound import play_sound



LOGGER = getLogger(__name__)

class BeepBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        # super(BeepBackend(config, audio), self).__init__(self, {'audio', Beep})
        super(BeepBackend(config, audio), self).__init__()
        LOGGER.info("Hello from BeepBackend 👋")
        


class Beep(audio.Audio):

    def __init(self, config, mixer):
        LOGGER.debug("Hello from Beep 👋")
