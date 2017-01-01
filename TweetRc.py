import ConfigParser
import os
import sys

RC_DIR = "./2008rc"

class TweetRc(object):
    def __init__(self):
        self._config = None
        
    def GetConsumerKey(self):
        return self._GetOption('consumer_key')
    
    def GetConsumerSecret(self):
        return self._GetOption('consumer_secret')
    
    def GetAccessKey(self):
        return self._GetOption('access_key')

    def GetAccessSecret(self):
        return self._GetOption('access_secret')
    
    def _GetOption(self, option):
        try:
            return self._GetConfig().get('Tweet', option)
        except:
            return None
    
    def _GetConfig(self):
        if not self._config:
            self._config = ConfigParser.ConfigParser()
            self._config.read(os.path.expanduser(RC_DIR))
        return self._config
