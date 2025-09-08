def error_test(choice):
    try:
        float(choice)
    except ValueError:
        return True
    else:
        return False


continuing = True
while continuing:
    valid = False
    while not valid:
        option = input("Please type '1' or '2':\n1: Convert lb to kg\n2: Convert kg to lb\n")

        if option == "1":
            measurement = "lb"
            valid = True
        elif option == "2":
            measurement = "kg"
            valid = True
        
    weight = input(f"Please enter weight in {measurement}:\n")
    while error_test(weight):
        weight = input(f"Please enter weight in {measurement}:\n")
        
    valid_measurement = False
    while not valid_measurement:
        if measurement == "lb":
            new_weight = round(float(weight) * 0.45359237,2)
            print(f"You weigh {new_weight:.2f} kg")
            valid_measurement = True
        elif measurement == "kg":
            new_weight = round(float(weight) * 2.2046,2)
            print(f"You weigh {new_weight:.2f} lbs")
            valid_measurement = True
        else:
            print("Please enter a valid measurement\n")

    carry_on = input("Type 'y' to make another calculation or 'n' to exit:\n")
    if carry_on == "n":
        continuing = False