import difflib


def check_similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    rat = matcher.ratio()
    return round(rat, 4)


def check_jaccard(list1, list2):
    print(list1, list2)
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
