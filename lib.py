'''
def percentage(part, whole):
    return 100 * float(part) / float(whole)


def inrange (xr,yr, xr1, yr1,  xr2, yr2 ):
    if (xr == xr1 or x == xr2) and (yr >= yr1 and y <= yr2):
        return True
    else:
        return False

def inborder (xr,yr, xr1, yr1,  xr2, yr2 ):
    if inrange(xr,yr, xr1, yr1,  xr2, yr2) or inrange(yr, xr, yr1, xr1, yr2, xr2):
        return True
    else
        return False

# Instide in rectangle - not used
def inside(xr, yr, xr1, yr1, xr2, yr2):
    if (xr >= xr1 and x <= xr2) and (yr > yr1 and y < yr2):
        return True
    else:
        return False

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def is_weekend(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day not in days:
        return "Error"
    elif days.index(day) >= 0 and days.index(day) <= 4:
        return "WorkingDay"
    else:
        return "Weekend"
'''