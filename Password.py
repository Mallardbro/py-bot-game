class Password:

    def __init__(self, json):
        # json = {"password": "p123", "encryption": "REVERSE"}
        self.password = json["password"]
        self.encryption = json["encryption"]

        # Apply encryption if necessary
        if not self.encryption:
            self.encrypted = self.password
        else:
            self.encrypted = self.encrypt()
        print(f"Encrypted password: {self.encrypted}")

    def encrypt(self):
        # Possible encryption: REVERSE, IGNORE_DIGITS, CEASAR_N
        e = self.encryption

        if e == "REVERSE":
            return self.password[::-1]

        if e == "IGNORE_DIGITS":
            return self.ignore_digits_encryption()

        if e[0:6] == "CAESAR":
            return self.ceasar_encryption()

        return "No encryption found"

    def ignore_digits_encryption(self):
        out = ""
        for c in self.password:
            if c.isalpha():
                out += c
        return out

    def ceasar_encryption(self):
        out = ""
        shift = int(self.encryption[7:])
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for c in self.password:
            upper = c.isupper()
            c = c.lower()
            if c not in alphabet:
                out += c
                continue
            position = alphabet.index(c)
            next_c = alphabet[(position + shift) % 26]
            if upper:
                next_c = next_c.upper()
            out += next_c
        return out

# p = Password({"password": "abcd1463ffhh63dc", "encryption": "REVERSE"})
