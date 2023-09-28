from panther_detection_helpers.caching import put_string_set, get_string_set
import time


def rule(event):
    key = event.get("eventType") or event.get("action") or "default"
    val = event.get("eventID") or event.get("interfaceId") or "default"
    t = time.mktime(time.strptime(event.get("p_event_time", "").split(".")[0], "%Y-%m-%d %H:%M:%S"))
    put_string_set(key, [val], epoch_seconds=int(t) + 1_000)
    get_string_set(key, force_ttl_check=True)
    return False
