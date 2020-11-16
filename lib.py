
def percentage(part, whole):
    return 100 * float(part) / float(whole)


def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


# finds differences in days between 2 string dates. Keep in mind that if You use it from today +=1
def days_between(d1, d2):
    from datetime import datetime
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d2 - d1).days


def read_int_line():
    striped_line = ""
    striped_line = "8 2 2 8 2 2 3 7"
    if len(striped_line) == 0:
        striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


def in_range (xr,yr, xr1, yr1,  xr2, yr2 ):
    if (xr == xr1 or xr == xr2) and (yr >= yr1 and yr <= yr2):
        return True
    else:
        return False


def in_border (xr,yr, xr1, yr1,  xr2, yr2 ):
    if inrange(xr,yr, xr1, yr1,  xr2, yr2) or inrange(yr, xr, yr1, xr1, yr2, xr2):
        return True
    else:
        return False


# Inside in rectangle - not used
def inside(xr, yr, xr1, yr1, xr2, yr2):
    if (xr >= xr1 and xr <= xr2) and (yr > yr1 and yr < yr2):
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


# Coins:
# I was searching for clever way and found:
def _get_change_making_matrix(set_of_coins, r: int):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        m[0][i] = float('inf')  # By default there is no way of making change
    return m


def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]
coins_values = [1, 2, 5, 10, 20, 50, 100, 200, 500]
print(change_making(coins_values, 523))

# Coins end

# Reverse string:
text = ""
result = text[::-1]

nums = "alabala"
a = 5 if len(nums) > 2 else 3 # a = 2
nums = [1, 2, 34, 45,  55]
lst = ["even" if _ % 2 == 0 else "odd" for _ in nums]
a = nums.copy()
result = [[index, a[index]] for index in range(len(a))]

matrix = [[j for j in range(5)] for i in range(5)] 