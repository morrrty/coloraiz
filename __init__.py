
import sys
import importlib

class Proxy:

    def __init__(self, module):
        self._original_module = importlib.import_module(module)

    def __getattr__(self, name):
        original_attr = getattr(self._original_module, name)
        if callable(original_attr):
            def wrapped(*args, **kwargs):
                result = original_attr(*args, **kwargs)
                return result
            return wrapped
        else:
            return original_attr
try:
    sys.modules['colorama'] = Proxy('colorama')
except ModuleNotFoundError:
    pass
