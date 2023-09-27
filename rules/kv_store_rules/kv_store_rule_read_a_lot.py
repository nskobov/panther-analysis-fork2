from panther_oss_helpers import get_string_set, put_string_set
import random

ignore = {"hi", "bye"}


def rule(event):
    r = random.randint(1, 5)
    if r == 5:
        put_string_set(f"r={r}", {"hi", "bye"})
        return True

    ignore = get_string_set(f"r={r}")
    return False


