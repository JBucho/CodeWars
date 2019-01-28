"""Move the first letter of each word to the end of it, then add "ay"
to the end of the word. Leave punctuation marks untouched."""


def pig_it(latin):
    latin = latin.split(' ')
    pig_latin = []
    for word in latin:
        if word.isalpha():
            pig_word = word[1:] + word[0] + 'ay'
            pig_latin.append(pig_word)
        else:
            pig_latin.append(word)
    return ' '.join(pig_latin)


def pig_it2(latin):
    return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in latin.split()])


if __name__ == '__main__':
    print(pig_it("Pig latin is cool !"))
    print(pig_it2("Pig latin is cool !"))
