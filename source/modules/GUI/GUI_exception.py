# Custom Exception

class DuplicateObjectNameError(Exception):
    def __init__(self, message):
        self.msg = message