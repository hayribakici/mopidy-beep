'''
Python module for Mopidy Beep frontend.
'''

__all__ = (
    'BeepFrontend',
)

from logging import getLogger

import pykka

from mopidy import core as mopidy_core
from .sound import play_sound



LOGGER = getLogger(__name__)


class BeepFrontend(pykka.ThreadingActor, mopidy_core.CoreListener):
    '''
    Beep frontend which basically gives auditive feedback on mopidy events.
    '''

    def __init__(self, config, core):
        super().__init__()
        self.core = core

    #def on_event(self, event, **kwargs):
    #    LOGGER.info(f'{event}')

    def tracklist_changed(self):
        LOGGER.info("Playing bell sound")
        play_sound('bell.ogg')



