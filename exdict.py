import os
import shelve


class Exdict(dict):
    """
    Behaves like a dict and a class
    """
    def __getattr__(self, key):
        if key in ["__getattr__", "__setattr__", "__getstate__"] + dir(dict):
            #return dict.__getattr__(self, key)
            #TODO: use super(dict,self).__getattr__(key)
            return None
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value
    def __dir__(self):
        return dir(super(Exdict, self)) + self.keys()