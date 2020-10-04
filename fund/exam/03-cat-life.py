
def get_male_age(argument):
    cat_breed = {
        "British Shorthair": 13,
        "Siamese"           : 15,
        "Persian"           : 14,
        "Ragdoll"           : 16,
        "American Shorthair": 12,
        "Siberian"          : 11
    }
    return cat_breed.get(argument, -1)

def get_female_age(argument):
    cat_breed = {
        "British Shorthair": 14,
        "Siamese"           : 16,
        "Persian"           : 15,
        "Ragdoll"           : 17,
        "American Shorthair": 13,
        "Siberian"          : 12
    }
    return cat_breed.get(argument, -1)

breed = input()
sex = input()
if sex == "m":
    human_months = get_male_age(breed)
elif sex == "f":
    human_months = get_female_age(breed)

if human_months >= 1:
    human_months = human_months *12
    cat_months = human_months / 6
    print ("%d cat months"%cat_months)
else:
    print ("%s is invalid cat!"%breed)

