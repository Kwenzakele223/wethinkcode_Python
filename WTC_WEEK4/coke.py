#the amount due is 50
amount_due = 50


#looping to check whether the coins inserted are 5,10, and 25

while True:
    print(f"Amount Due: {amount_due}")
    coins = int(input("Insert a coin: "))
    if coins == 25 or coins == 10 or coins == 5:
        amount_due = amount_due - coins

#checking if the amount due is 0 or less than 0 so that the user sees the amount owed
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")

            break
        else:
           print(f"Amount Due: {amount_due}")
