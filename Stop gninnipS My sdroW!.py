def spin_words(sentence):
    new_string = ''
    words = sentence.split()
    for word in words:
        if len(word) < 5:
            new_string += word + ' '
        else:
            new_string += word[::-1] + ' '
    return new_string.rstrip()
