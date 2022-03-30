FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (in,ft,yd,mi): ")

if (FromUnit == "in" or "ft" or "yd" or "mi"): 
    multiplier = 1
else:
    print("From unit is not valid")
    exit()


ToUnit = input("Enter To Unit (in, ft, yd, mi): ")

if (ToUnit == "in" or "ft" or "yd" or "mi"): 
    multiplier = 1
else:
    print("To Unit is not valid")
    exit()

if (FromUnit == "in" and ToUnit == "in"):
    multiplier = 1
elif (FromUnit == "ft" and ToUnit == "ft"):
    multiplier = 1
elif (FromUnit == "yd" and ToUnit == "yd"):
    multiplier = 1
elif (FromUnit == "mi" and ToUnit == "mi"):
    multiplier = 1
elif (FromUnit == "in" and ToUnit == "ft"):
        multiplier = 0.0833333
elif (FromUnit == "in" and ToUnit == "yd"):
        multiplier = 0.0277778
elif (FromUnit == "in" and ToUnit == "mi"):
        multiplier = 0.00001578282828283 
elif (FromUnit == "ft" and ToUnit == "in"):
        multiplier = 12
elif (FromUnit == "ft" and ToUnit == "yd"):
        multiplier = 0.3333333333333 
elif (FromUnit == "ft" and ToUnit == "mi"):
        multiplier = 0.0001893939393939 
elif (FromUnit == "yd" and ToUnit == "in"):
        multiplier = 36
elif (FromUnit == "yd" and ToUnit == "ft"):
        multiplier = 3
elif (FromUnit == "yd" and ToUnit == "mi"):
        multiplier = 0.0005681818181818 
elif (FromUnit == "mi" and ToUnit == "in"):
        multiplier = 63360
elif (FromUnit == "mi" and ToUnit == "ft"):
        multiplier = 5280
elif (FromUnit == "mi" and ToUnit == "yd"):
        multiplier = 1760
else:
    print("INVALID!")

multiplication = round(multiplier * FromValue,7)
print("{} {} => {} {}".format(FromValue, FromUnit, multiplication, ToUnit))