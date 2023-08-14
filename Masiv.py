import random

blok_empety = [];

def masiv(blok_empety):
    blok_empety = [random.randint(0, 10000) for i in range(10000)];
    return blok_empety

blok = masiv(blok_empety)

