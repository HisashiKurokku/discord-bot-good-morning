import pytz

def getTime(timezone):
    tz = ""
    if timezone == "SYSTEM":
        tz = "UTC"
    else:
        if tzCheck(timezone):
            tz = timezone
        else:
            tz = "UTC"
    print(tz)
    return tz


def tzCheck(timezone):
    exist = False
    for tz in pytz.all_timezones:
        if timezone.lower() == tz.lower():
            exist = True
            break
    return exist