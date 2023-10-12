from panther_detection_helpers.caching import put_string_set, get_string_set
import random


def rule(event):
    r = random.randint(1, 5)
    key = event.get("eventType") or event.get("action") or "default"

    if r == 5:
        val = event.get("eventID") or event.get("interfaceId") or "default"
        put_string_set(key, [val], epoch_seconds=event.event_time_epoch() + 1_000)
    else:
        get_string_set(key, force_ttl_check=True)

    return False
