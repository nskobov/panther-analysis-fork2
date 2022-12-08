from panther_base_helpers import deep_get


def target(event):
    org = deep_get(event, "parameters", "ORG_UNIT_NAME")
    if org:
        return f" for OU '{org}'"
    domain = deep_get(event, "parameters", "DOMAIN_NAME")
    if domain:
        return f" for domain '{domain}'"
    return ""


def rule(event):
    if event.get("name") == "ALLOW_STRONG_AUTHENTICATION":
        return True
    return False


def title(event):
    return (
        f"Google Workspace: Allow 2-Step Verification setting "
        f"has been changed from "
        f"'{event.get('parameters').get('OLD_VALUE')}' to "
        f"'{event.get('parameters').get('NEW_VALUE')}'"
        f"{target(event)}"
    )
