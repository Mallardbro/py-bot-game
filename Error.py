class Error:
    def __init__(self, s):
        self.message = s

    def __str__(self):
        return "Error: " + self.message
