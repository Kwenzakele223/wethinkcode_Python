while True:
    try:
        frc = input("Fraction : ")
        x , y = frc.split("/")
        x= int(x)
        y = int(y)
        if y == 0 or x > y or x < 0:
            raise ValueError
    except (ValueError,ZeroDivisionError) :
        pass
    else:
        break
per=(int(round((x / y) * 100)))
per1 = str(per) + "%"
if per >= 99:
    print("F")
elif per <= 1:
    print("E")
else:
    print(f"{per1}")
