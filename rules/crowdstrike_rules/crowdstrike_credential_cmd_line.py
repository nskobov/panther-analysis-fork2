import re

from panther_base_helpers import crowdstrike_process_alert_context

CREDENTIAL_STRINGS = {
    r".+:.+@",  # username:password@
    r"-u\s.+\:.+",  # -u username:password
    r"--user(\s|\=).+\s--password(\s|\=).+",  # --user=username --password=password"
}


def rule(event):
    if event.get("event_simpleName") == "ProcessRollup2":
        if event.udm("cmd"):
            for string in CREDENTIAL_STRINGS:
                cred_pattern = re.compile(string)
                if cred_pattern.search(event.udm("cmd")):
                    return True

    return False


def title(event):
    aid = event.get("aid", "<AID_NOT_FOUND>")
    return f"Crowdstrike: Credentials passed on commandline detected on aid [{aid}]"


def alert_context(event):
    return crowdstrike_process_alert_context(event)
