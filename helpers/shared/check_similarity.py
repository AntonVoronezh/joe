import difflib


def check_similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    rat = matcher.ratio()
    return round(rat, 4)
