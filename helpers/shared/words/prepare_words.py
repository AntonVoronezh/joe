def prepare_words(words):
    result = []
    for word in words:
        elem = word.lower().strip()

        if len(elem) > 2:
            result.append(elem)

    return result
