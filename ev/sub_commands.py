

_SUB_COMMANDS=["track","untrack","history","checkout","comment"]

ROUTER = {}

class Actions:
    def __init__(self):
        pass

    def track(self,*args):
        pass

    def untrack(self,*args):
        pass

    def history(self,*args):
        pass
    
    def checkout(self,*args):
        pass

    def comment(self,*args):
        pass

def _setup_router(actions,command_names):
    for attr in dir(actions):
        if attr in _SUB_COMMANDS:
            ROUTER[attr] = actions.attr

def setup_router():
    _setup_router(Actions(),_SUB_COMMANDS)


