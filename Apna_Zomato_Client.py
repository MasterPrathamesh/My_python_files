
def order_food():
    flag = 0
    print()
    d_id = input("Enter Dish ID Which You Want to order :- ")

    ob = open("All_Hotels.txt", "r")
    ls = ob.readlines()
    ob.close()

    order = None
    for val in ls:
        ls1 = val.split(",")
        ht_nm = ls1[1]
        hotel = ht_nm + ".txt"

        ob = open(hotel, "r")
        ls2 = ob.readlines()
        ob.close()

        for val1 in ls2:
            ls3 = val1.split(",")
            if ls3[0] == d_id:
                flag = 1
                order = val1
                break

    if flag == 0:
        print("No Such Dish Found...")
    else:
        ls = order.split(",")
        print("Dish Name = ", ls[1])
        print("Dish Price = ", ls[2])
        print("Ratings = ", ls[3] + "/10")
        print("\n1. To Confirm Order.")
        print("2. Go Back.")
        ch2 = int(input("Enter Your Choice :- "))

        if ch2 == 1:
            nm = input("Enter Your Name :- ")
            mob = input("Enter Your Mobile No. :- ")
            adr = input("Enter Your Address :- ")
            ob = open("All_Orders.txt", "a")
            ob.write(nm + "," + mob + "," + adr + "," + "Paid" + "," + "\n")
            ob.close()
            print("Order Confirmed Successfully...")


def search_hotel():
    flag = 0
    print()
    print("1. Search By Hotel ID.")
    print("2. Search By Hotel Name.")
    ch1 = int(input("Enter Your Choice :- "))

    if ch1 == 1:
        ht_id = input("Enter Hotel ID :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        ls1 = None
        for val in ls:
            ls1 = val.split(",")

            if ls1[0] == ht_id:
                flag = 1
                print("\n--- Available Hotel ---")
                print("Hotel ID = ", ls1[0])
                print("Hotel Name = ", ls1[1])
                print("Hotel Contact No. = ", ls1[2])
                print("Hotel Address = ", ls1[3])
                print("Hotel Ratings = ", ls1[4])
                print("-" * 30)
                break

        if flag == 0:
            print("No Such Hotel Available...")
        elif flag == 1:
            print("1. To View Menu of " + ls1[1])
            print("2. Go Back")
            ch2 = int(input("Enter Your Choice :- "))

            if ch2 == 1:
                print()
                hotel = ls1[1] + ".txt"
                ob = open(hotel, "r")
                ls = ob.readlines()
                ob.close()

                count = 0
                print("--- Menu ---")
                for val in ls:
                    ls1 = val.split(",")
                    count = count + 1
                    print("Dish No. = ", count)
                    print("Dish ID = ", ls1[0])
                    print("Dish Name = ", ls1[1])
                    print("Dish Price = ", ls1[2])
                    print("Dish Ratings = ", ls1[3])
                    print("-"*30)

    elif ch1 == 2:
        ht_nm = input("Enter Hotel Name :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        for val in ls:
            ls1 = val.split(",")

            if ls1[1] == ht_nm:
                flag = 1
                print("\n--- Available Hotel ---")
                print("Hotel ID = ", ls1[0])
                print("Hotel Name = ", ls1[1])
                print("Hotel Contact No. = ", ls1[2])
                print("Hotel Address = ", ls1[3])
                print("Hotel Ratings = ", ls1[4])
                print("-"*30)
                break

        if flag == 0:
            print("No Such Hotel Available...")
        elif flag == 1:
            print("1. To View Menu of " + ht_nm)
            print("2. Go Back")
            ch2 = int(input("Enter Your Choice :- "))

            if ch2 == 1:
                print()
                hotel = ht_nm + ".txt"
                ob = open(hotel, "r")
                ls = ob.readlines()
                ob.close()

                count = 0
                print("--- Menu ---")
                for val in ls:
                    ls1 = val.split(",")
                    count = count + 1
                    print("Dish No. = ", count)
                    print("Dish ID = ", ls1[0])
                    print("Dish Name = ", ls1[1])
                    print("Dish Price = ", ls1[2])
                    print("Dish Ratings = ", ls1[3])
                    print("-"*30)



def search_dish():
    print()
    print("1. Search By Dish ID.")
    print("2. Search By Dish Name.")
    ch1 = int(input("Enter Your Choice :- "))

    if ch1 == 1:
        flag = 0
        d_id = input("Enter Dish ID Which You Want to order :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        ht_nm = None
        order = None
        for val in ls:
            ls1 = val.split(",")
            ht_nm = ls1[1]
            hotel = ht_nm + ".txt"

            ob = open(hotel, "r")
            ls2 = ob.readlines()
            ob.close()

            for val1 in ls2:
                ls3 = val1.split(",")
                if ls3[0] == d_id:
                    flag = 1
                    order = val1
                    break

        if flag == 0:
            print("No Such Dish Found...")
        else:
            ls = order.split(",")
            print("\n--- Available Dish ---")
            print("Hotel Name = ", ht_nm)
            print("Dish ID = ", ls[0])
            print("Dish Name = ", ls[1])
            print("Dish Price = ", ls[2])
            print("Ratings = ", ls[3] + "/10")


    if ch1 == 2:
        flag = 0
        print()
        d_nm = input("Enter Dish Name :- ")
        print("\n--- Available Dishes ---")
        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        count = 0
        for val in ls:
            ls1 = val.split(",")
            ht_nm = ls1[1]
            hotel = ht_nm + ".txt"

            ob = open(hotel, "r")
            ls2 = ob.readlines()
            ob.close()

            for val1 in ls2:
                ls3 = val1.split(",")
                if ls3[1] == d_nm:
                    count = count + 1
                    flag = 1
                    print("Dish = ", count)
                    print("Hotel Name = ", ht_nm)
                    print("Dish ID = ", ls3[0])
                    print("Dish Name = ", ls3[1])
                    print("Dish Price = ", ls3[2])
                    print("Ratings = ", ls3[3] + "/10")
                    print("-" * 30)

        if flag == 0:
            print("No Such Dish Found...")
            print("Please Enter Correct Dish Name...")
        print("\n", "*" * 35, "END", "*" * 35)


def view_menu():
    flag = 0
    print()
    print("1. View Menu By Hotel ID.")
    print("2. View Menu By Hotel Name.")
    ch1 = int(input("Enter Your Choice :- "))

    if ch1 == 1:
        ht_id = input("Enter Hotel ID :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        ls1 = None
        for val in ls:
            ls1 = val.split(",")

            if ls1[0] == ht_id:
                flag = 1
                break

        if flag == 0:
            print("No Such Hotel Available...")
        elif flag == 1:
            print()
            hotel = ls1[1] + ".txt"
            ob = open(hotel, "r")
            ls = ob.readlines()
            ob.close()

            count = 0
            print("--- Menu ---")
            for val in ls:
                ls1 = val.split(",")
                count = count + 1
                print("Dish No. = ", count)
                print("Dish ID = ", ls1[0])
                print("Dish Name = ", ls1[1])
                print("Dish Price = ", ls1[2])
                print("Dish Ratings = ", ls1[3])
                print("-"*30)

    elif ch1 == 2:
        ht_nm = input("Enter Hotel Name :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        for val in ls:
            ls1 = val.split(",")

            if ls1[1] == ht_nm:
                flag = 1
                break

        if flag == 0:
            print("No Such Hotel Available...")
        elif flag == 1:
            print()
            hotel = ht_nm + ".txt"
            ob = open(hotel, "r")
            ls = ob.readlines()
            ob.close()

            count = 0
            print("--- Menu ---")
            for val in ls:
                ls1 = val.split(",")
                count = count + 1
                print("Dish No. = ", count)
                print("Dish ID = ", ls1[0])
                print("Dish Name = ", ls1[1])
                print("Dish Price = ", ls1[2])
                print("Dish Ratings = ", ls1[3])
                print("-"*30)



def cancel_order():
    pass


def all_hotels():
    print()
    ob = open("All_Hotels.txt", "r")
    ls = ob.readlines()
    ob.close()

    print(" --- Displaying All Hotels List --- \n")
    print("=" * 80)
    print("Hotel ID\t" + "||" + "\t" + "Hotel Name\t" + "||" + "\t" + "Hotel Contact No.\t" + "||" + "\t" + "Hotel Address\t" + "||" + "\t" + "Hotel Ratings")
    print("=" * 80, "\n")
    print("-" * 80)
    for val in ls:
        ls1 = val.split(",")
        print(ls1[0] + "\t" + "||" + "\t" + ls1[1] + "\t" + "||" + "\t" + ls1[2] + "\t" + "||" + "\t" + ls1[3] + "\t" + "||" + "\t" + ls1[4])
        print("-" * 80)

    print("\n", "*"*35, "END", "*"*35)


def give_feed():
    print()
    print("1. To Give Ratings.")
    print("2. To Give Feedback.")
    ch1 = int(input("Enter Your Choice :-"))

    if ch1 == 1:
        flag = 0
        print()
        print("1. To Give Rating To a Hotel.")
        print("2. To Give Rating To a Dish.")
        ch2 = int(input("Enter Your Choice :- "))

        if ch2 == 1:
            ht_id = input("Enter Hotel ID :- ")

            ob = open("All_Hotels.txt", "r")
            ls = ob.readlines()
            ob.close()

            ht_nm = None
            for val in ls:
                ls1 = val.split(",")
                if ls1[0] == ht_id:
                    flag = 1
                    ht_nm = ls1[1]
                    break

            if flag == 0:
                print("No Such Hotel Found...")
            elif flag == 1:
                hotel = ht_nm + ".txt"

                print("Hotel Name = ", ht_nm)
                r = input("Enter How Many Rating You Want To Give (Between 1-10) :- ")

                #Remaining Code...
                print("Rating is Added Successfully...")



def view_feed():
    pass




while True:
    print()
    print("--- Select Options ---")
    print("1. Order Food.")
    print("2. Search Hotel.")
    print("3. Search Dish.")
    print("4. View Menu.")
    print("5. Cancel Order.")
    print("6. Show All Hotels.")
    print("7. Feedback and Ratings.")
    print("8. View Feedback and Ratings.")
    print("0. Exit.")
    ch = int(input("Enter Your Choice :- "))

    if ch == 1:
        order_food()

    elif ch == 2:
        search_hotel()

    elif ch == 3:
        search_dish()

    elif ch == 4:
        view_menu()

    elif ch == 5:
        cancel_order()

    elif ch == 6:
        all_hotels()

    elif ch == 7:
        pass

    elif ch == 8:
        pass

    elif ch == 9:
        pass

    elif ch == 0:
        break