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
        super(BeepFrontend, self).__init__()
        self.core = core

    #def on_event(self, event, **kwargs):
    #    LOGGER.info(f'{event}')

    def on_start(self):
        play_sound('start.ogg')

    def on_stop(self):
        play_sound('stop.oga')

    def tracklist_changed(self):
        play_sound('bell.ogg')



