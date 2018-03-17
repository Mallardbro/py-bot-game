from Password import Password


class Security:

    def __init__(self, list_of_json):
        # list_of_json = [{"password": "p4ss", "encryption": null}, {"password": "p123", "encryption": "REVERSE"}]
        # An array of {"password": "___", "encryption": ____}

        self.passwords = []

        for p in list_of_json:
            self.passwords.append(Password(p))
