months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date:").strip()

    if "/" in date:
        try:
            m,d,y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)

            if m < 1 or m > 12 or d < 1 or d > 31:
                pass
            else:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass

    if "," in date:
        try:
            date = date.replace(",", "")
            m, d, y = date.split(" ")

            if m in months:
                m = months[m]
                d = int(d)
                y = int(y)

                if m < 1 or m > 12 or d < 1 or d > 31:
                    continue
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break

            elif d in months:
                pass

        except ValueError:
            pass