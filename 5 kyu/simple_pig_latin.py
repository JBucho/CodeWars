def pig_it(latin):
    latin = latin.split(' ')
    pig_latin = []
    for w in latin:
        if w.isalpha():
            pig_word = w[1:] + w[0] + 'ay'
            pig_latin.append(pig_word)
        else:
            pig_latin.append(w)
    return ' '.join(pig_latin)


def pig_it2(latin):
    return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in latin.split()])


print(pig_it("Pig latin is cool !"))
print(pig_it2("Pig latin is cool !"))