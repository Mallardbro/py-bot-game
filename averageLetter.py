def get_average(str):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    s = 0
    l = 0
    for c in str.lower():
        if c in alphabet:
            s += alphabet.index(c)
            l += 1
    return float(s)/l


print(get_average("Mallard"))
print(get_average("Raynor"))
