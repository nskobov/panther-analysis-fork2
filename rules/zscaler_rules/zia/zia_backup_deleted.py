from panther_zscaler_helpers import zia_alert_context, zia_success


def rule(event):
    if not zia_success(event):
        return False
    action = event.deep_get("event", "action", default="ACTION_NOT_FOUND")
    category = event.deep_get("event", "category", default="CATEGORY_NOT_FOUND")
    if action == "DELETE" and category == "BACKUP_AND_RESTORE":
        return True
    return False


def title(event):
    return (
        f"[Zscaler.ZIA]: Backup was deleted by admin with id "
        f"[{event.deep_get('event', 'adminid', default='<ADMIN_ID_NOT_FOUND>')}]"
    )


def alert_context(event):
    return zia_alert_context(event)
