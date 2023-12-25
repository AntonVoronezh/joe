import difflib


def check_similarity(list_1, list_2):
    normalized_1 = " ".join(list_1).lower()
    normalized_2 = " ".join(list_2).lower()
    matcher = difflib.SequenceMatcher(None, normalized_1, normalized_2)
    rat = matcher.ratio()
    return round(rat, 4)


def check_jaccard(list_1, list_2):
    intersection = len(list(set(list_1).intersection(list_2)))
    union = (len(list_1) + len(list_2)) - intersection
    return float(intersection) / union
