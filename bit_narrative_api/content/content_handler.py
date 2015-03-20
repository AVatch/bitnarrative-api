import re


def strip_tags(s):
    """
    removes all < * > </ * > tags
    """
    return re.sub("<.*?>", "", s)
