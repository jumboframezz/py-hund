'''
User Logins

Write a program that receives a list of username-password pairs in the format “{username} -> {password}”. If there’s
already a user with that username, replace their password. After you receive the command “login”, login requests start
coming in, using the same format. Your task is to print the status of user login, using different messages as per
the conditions below:

If the password matches with the user’s password, print “{username}: logged in successfully”.
If the user doesn’t exist, or the password doesn’t match the user, print “{username}: login failed”.
When you receive the command “end”, print the count of unsuccessful login attempts, using the format
“unsuccessful login attempts: {count}”.

Examples
Input                                           Output
ivan_ivanov -> java123                          pesh0: login failed
pesh0 ->; qwerty                                ivan_ivanov: logged in successfully
stamat4e -> 111111                              stamat4e: login failed
princess_penka -> MyPrince                      princess_penka: logged in successfully
login                                           unsuccessful login attempts: 2
pesh0 -> qwertt
ivan_ivanov -> java123
stamat4e -> 111112
princess_penka -> MyPrince
end

ivan_ivanov -> java123
pesh0 -> qwerty
stamat4e -> 111111
princess_penka -> MyPrince
login
pesh0 -> qwertt
ivan_ivanov -> java123
stamat4e -> 111112
princess_penka -> MyPrince
end

'''

in_line=input().strip(" ")
dict = {}
login_dict = {}
badlogins = 0
out_string=""
while in_line != "login":
    params = in_line.split(" -> ")

    user_name = params[0]
    user_pass = params[1]
    if dict.get(user_name):
            dict[user_name] = user_pass
    else:
            dict[user_name] = user_pass
    in_line = input().strip(" ")

in_line=input().strip(" ")
while in_line != "end":
    params = in_line.split(" -> ")
    user_name = params[0]
    user_pass = params[1]
    if not dict.get(user_name):
        out_string += f"{user_name}: login failed\n"
        badlogins +=1
    elif dict.get(user_name) and (user_pass == dict[user_name]):
        out_string += f"{user_name}: logged in successfully\n"
    else:
        out_string += f"{user_name}: login failed\n"
        badlogins +=1
    in_line = input().strip(" ")


print(out_string, end="")
print(f"unsuccessful login attempts: {badlogins}")







