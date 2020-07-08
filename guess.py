from collections import Counter
from typing import Tuple


def guess(query: str, answer: str) -> Tuple[int, int]:
    """Compute the outcome of guessing a word

    Args:
        query (str): the word guessed
        answer (str): The actual word

    Returns:
        [int, int]: get (matching location), touch (location mismatched)
    """

    # Verify input
    assert len(query) == len(answer)
    query = query.upper()
    answer = answer.upper()
    assert query.isalpha()
    assert answer.isalpha()

    # init data structure
    query_l = list(query)
    answer_l = list(answer)
    query_c = Counter()
    answer_c = Counter()
    get = 0
    touch = 0

    # compare
    for i in range(len(query_l)):
        if query_l[i] == answer_l[i]:
            get += 1
            query_l[i] = None
            answer_l[i] = None
        else:
            query_c[query_l[i]] += 1
            answer_c[answer_l[i]] += 1

    for k, v in query_c.items():
        touch += min(v, answer_c[k])

    return get, touch


def test_guess():
    assert guess("AAAA", "ABAB") == (2, 0)
    assert guess("AACC", "ABAB") == (1, 1)
    assert guess("BAAA", "AABB") == (1, 2)
    assert guess("TAKE", "GOAL") == (0, 1)
    assert guess("PLAY", "GOAL") == (1, 1)
    assert guess("UOAL", "GOAL") == (3, 0)
