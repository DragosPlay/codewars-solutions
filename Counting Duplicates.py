def duplicate_count(text):
    counter = 0
    text = text.lower()
    for char in set(text):
        if text.count(char) > 1:
            counter += 1
    return counter
