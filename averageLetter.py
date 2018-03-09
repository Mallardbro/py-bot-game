def get_average(_str):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    s = 0
    l = 0
    for c in _str.lower():
        if c in alphabet:
            s += alphabet.index(c)
            l += 1
    return float(s)/l


def word_cost(_str, vowel, cons):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    out = 0
    for c in _str.lower():
        if c in alphabet:
            if c in vowels:
                out += vowel
            else:
                out += cons
    return out


print(get_average("Raynor"))
print(word_cost("Mallard",150, 25))


