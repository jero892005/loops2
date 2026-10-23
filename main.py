def printmenu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def getprice(selection):
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 5.00
    elif selection == 3:
        return 4.50
    elif selection == 4:
        return 3.95
    else:
        return 0.00


def main():
    fooditems = ["Taco", "Burrito", "Nachos", "Soft Drink"]
    orders = []
    total = 0.0

    print("Welcome to Taco Palace! Please view the menu below and make a selection.")

    choice = 0

    while choice != 5:
        printmenu()
        choice = int(input("Enter your selection: "))

        if 1 <= choice <= 4:
            item = fooditems[choice - 1]
            price = getprice(choice)

            print("You have selected a " + item + ".")
            orders.append(item)
            total = total + price

        elif choice == 5:
            print("\nYour order:")

            if len(orders) > 0:
                print(" and ".join(orders))
            else:
                print("You did not order anything.")

            print(f"Your total is ${total:.2f}")

        else:
            print("Invalid selection. Please choose a number from 1 to 5.")


main()