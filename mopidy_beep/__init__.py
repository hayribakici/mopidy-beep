'''
Mopidy Pummeluff Python module.
'''

import os

import mopidy
from .frontend import BeepFrontend




class Extension(mopidy.ext.Extension):
    '''
    Mopidy Beep extension.
    '''

    dist_name = 'Mopidy-Beep'
    ext_name = 'beep'

    def get_default_config(self):  # pylint: disable=no-self-use
        '''
        Return the default config.

        :return: The default config
        '''
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return mopidy.config.read(conf_file)

    def get_config_schema(self):
        '''
        Return the config schema.

        :return: The config schema
        '''
        schema = super(Extension, self).get_config_schema()
        return schema

    def setup(self, registry):
        '''
        Setup the extension.

        :param mopidy.ext.Registry: The mopidy registry
        '''
        registry.add('frontend', BeepFrontend)

