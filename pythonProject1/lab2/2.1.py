p = input("Your password is:  ")
p2 = input("repeat password:  ")
if len(p) < 4:
    print ("Your password too short")
elif 3 < len(p) and len(p) < 6:
    print ("weak password")
else:
    print ("OK.")
    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False
    for char in p:
        if char.isnumeric():
            is_numeric = True
        elif char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        elif char in "#@!*&%^":
            is_spec = True
    if is_numeric and is_upper and is_lower and is_spec:
        print("Password accepted")
        if p == p2:
            print ("Registration is over")
        else:
            print ("passwords mismatch")