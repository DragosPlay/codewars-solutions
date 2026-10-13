def pig_it(text):
    pig_string = []
    for word in text.split():
        if word.isalpha():
            pig_string.append(word[1:] + word[0] + 'ay')
        else:
            pig_string.append(word)
    pig_string = ' '.join(pig_string)
    return pig_string
