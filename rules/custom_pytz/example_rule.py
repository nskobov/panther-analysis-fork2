from datetime import datetime
from pytz import timezone
from panther_base_helpers import deep_get, pattern_match


## Required
#
# The logic to determine if an alert should send.
# return True = Alert, False = Do not Alert
def rule(event):
 
    return  deep_get(event, "alert", default=False)


def title(_):
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    return f"PYTZ timezone says now is {now_utc}"

# Additional information append to an alert, must return a dictionary
def alert_context(event):
    return dict(event)

