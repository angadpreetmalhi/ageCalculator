# Hey, You want to know when you will be 100yrs old
userCurrentage = int(input("Enter your age or year of birth"))
if str(userCurrentage).isnumeric():
    length= (str(userCurrentage))
    if len(length)<4 and userCurrentage<99:
        print(f"You are {userCurrentage} year old")
        print(f"You will be 100yr old within next {100-userCurrentage} in "
              f"{2019+(100-userCurrentage)}")
    elif len(length)==4 and 1914 < userCurrentage <2020:
        print(f"Your birth year is {userCurrentage}")
        print(f"you will be 100yr old in {userCurrentage+100} You are "
              f"{2019-userCurrentage} year old")
    else:
        print("Enter a correct format")
else:
    print("Enter correct format")
