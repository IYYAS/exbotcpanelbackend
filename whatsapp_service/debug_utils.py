import json


def safe_debug_value(value):
    """Return a printable representation that avoids UnicodeEncodeError on ASCII stdout."""
    if value is None:
        return ""

    if isinstance(value, bytes):
        try:
            return safe_debug_value(value.decode("utf-8"))
        except UnicodeDecodeError:
            return safe_debug_value(value.decode("utf-8", errors="replace"))

    if isinstance(value, str):
        return value.encode("unicode_escape").decode("ascii")

    if isinstance(value, (dict, list, tuple, set)):
        try:
            return json.dumps(value, ensure_ascii=True, sort_keys=True, default=str)
        except Exception:
            return repr(value)

    try:
        return json.dumps(value, ensure_ascii=True, default=str)
    except Exception:
        return repr(value)
