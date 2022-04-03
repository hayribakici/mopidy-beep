'''
Mopidy Beep Python module.
'''

import os
import mopidy

__version__ =  pkg_resources.get_distribution("Mopidy-Beep").version

class Extension(mopidy.ext.Extension):
    '''
    Mopidy Beep extension.
    '''

    dist_name = 'Mopidy-Beep'
    ext_name = 'beep'
    version = __version__

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

    def validate_environment(self):
        # Any manual checks of the environment to fail early.
        # Dependencies described by setup.py are checked by Mopidy, so you
        # should not check their presence here.
        pass


    def setup(self, registry):
        '''
        Setup the extension.

        :param mopidy.ext.Registry: The mopidy registry
        '''
        # from .frontend import BeepFrontend
        from .backend import BeepBackend
        # registry.add('frontend', BeepFrontend)
        registry.add('backend', BeepBackend)

