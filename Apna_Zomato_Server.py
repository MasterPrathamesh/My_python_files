


def add_hotel():
    print()
    ht_id = input("Enter Hotel ID :- ")
    ht_nm = input("Enter Hotel Name :- ")
    ht_no = input("Enter Hotel Contact No. :- ")
    ht_adr = input("Enter Hotel Address :- ")

    hotel = ht_nm + ".txt"

    ob = open(hotel, "a")
    ob.close()

    ob = open("All_Hotels.txt", "a")
    ob.write(ht_id + "," + ht_nm + "," + ht_no + "," + ht_adr + "," + "0" + "," + "\n")
    ob.close()
    print("New Hotel Added Successfully...")



def add_dish():
    flag = 0
    print()
    d_htid = input("Enter Hotel ID :- ")
    d_id = input("Enter Dish No. :- ")
    d_nm = input("Enter Dish Name :- ")
    d_price = input("Enter Dish Price :- ")

    ob = open("All_Hotels.txt", "r")
    ls = ob.readlines()
    ob.close()

    d_ht = None
    for val in ls:
        ls1 = val.split(",")
        if ls1[0] == d_htid:
            d_ht = ls1[1]
            break

    hotel = d_ht + ".txt"

    ob = open(hotel, "r")
    ls = ob.readlines()
    ob.close()

    for val in ls:
        ls1 = val.split(",")
        if ls1[0] == d_id:
            flag = 1
            break

    if flag == 0:
        ob = open(hotel, "a")
        ob.write(d_id + "," + d_nm + "," + d_price + "," + "0" + "," + "\n")
        ob.close()
        print("One Dish Added Successfully...")

    else:
        print("This Dish ID is Already Added...")


def update_price():
    print()
    d_ht = input("Enter Hotel Name :- ")
    d_id = input("Enter Dish No. :- ")
    d_n_price = input("Enter New Price of Dish :- ")

    hotel = d_ht + ".txt"

    ob = open(hotel, "r")
    ob.close()


def add_delivery_boy():
    print()
    db_id = input("Enter Delivery Boy ID :- ")
    db_nm = input("Enter Delivery Boy Name :- ")
    db_no = input("Enter Delivery Boy Contact No. :- ")
    db_age = input("Enter Delivery Boy Age :- ")
    db_sal = input("Enter Delivery Boy Salary :- ")

    ob = open("All_Delivery_Boys.txt", "a")
    ob.write(db_id + "," + db_nm + "," + db_no + "," + db_age + "," + db_sal + "," + "\n")
    ob.close()
    print("Delivery Boy Details Added Successfully...")


def add_offers():
    pass


def add_menu():
    flag = 0
    print()
    ht_id = input("Enter Hotel ID :- ")

    ob = open("All_Hotels.txt", "r")
    ls = ob.readlines()
    ob.close()

    for val in ls:
        ls1 = val.split(",")
        if ls1[0] == ht_id:
            flag = 1
            val1 = ls1[1]
            break

    if flag == 0:
        print("No Such Hotel Found...")
    elif flag == 1:

        hotel = val1 + ".txt"

        i = int(input("Enter How Many Dishes You Want to Add :- "))

        ob = open(hotel, "w")
        j=1
        while j<=i:
            print()
            print("Dish No. = ", j)
            d_id = input("Enter Dish ID :- ")
            d_nm = input("Enter Dish Name :- ")
            d_price = input("Enter Dish Price :- ")
            ob.write(d_id + "," + d_nm + "," + d_price + "," + "0" + "," + "\n")
            j = j + 1

        ob.close()
        print("Menu Added Successfully...")



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


def all_dishes():
    print()
    ob = open("All_Hotels.txt", "r")
    ls = ob.readlines()
    ob.close()

    print(" --- Displaying All Dishes List --- \n")
    print("=" * 80)
    print("Hotel Name\t" + "||" + "\t" + "Dish ID\t" + "||" + "\t" + "Dish Name\t" + "||" + "\t" + "Dish Price\t" + "||" + "\t" + "Dish Ratings")
    print("="*80,"\n")
    print("-" * 80)
    for val in ls:
        ls1 = val.split(",")
        hotel = ls1[1] + ".txt"
        ob = open(hotel, "r")
        ls2 = ob.readlines()
        ob.close()
        for val1 in ls2:
            ls3 = val1.split(",")
            print(ls1[1] + "\t" + "||" + "\t" + ls3[0] + "\t" + "||" + "\t" + ls3[1] + "\t" + "||" + "\t" + ls3[2] + "\t" + "||" + "\t" + ls3[3])
            print("-"*80)

    print("\n", "*" * 35, "END", "*" * 35)


def info():
    print()
    print("--- Select Option ---")
    print("1. Show Menu.")
    print("2. Show All Delivery Boys Details.")
    ch1 = int(input("Enter Your Choice :- "))

    if ch1 == 1:
        print()
        ht_id = input("Enter Hotel ID :- ")

        ob = open("All_Hotels.txt", "r")
        ls = ob.readlines()
        ob.close()

        ht_nm = None
        for val in ls:
            ls1 = val.split(",")
            if ls1[0] == ht_id:
                ht_nm = ls1[1]
                break

        hotel = ht_nm + ".txt"

        ob = open(hotel, "r")
        ls = ob.readlines()
        ob.close()

        print(" --- Dishes List of Hotel", ht_nm, "--- \n")
        print("=" * 80)
        print("Dish ID\t" + "||" + "\t" + "Dish Name\t" + "||" + "\t" + "Dish Price\t" + "||" + "\t" + "Dish Ratings")
        print("=" * 80, "\n")
        print("-" * 80)
        for val in ls:
            ls1 = val.split(",")
            print(ls1[0] + "\t" + "||" + "\t" + ls1[1] + "\t" + "||" + "\t" + ls1[2] + "\t" + "||" + "\t" + ls1[3])
            print("-" * 80)

        print("\n", "*" * 35, "END", "*" * 35)

    elif ch1 == 2:
        print()
        ob = open("All_Delivery_Boys.txt", "r")
        ls = ob.readlines()
        ob.close()

        print(" --- Displaying All Delivery Boys Details List --- \n")
        print("=" * 100)
        print("Delivery Boy ID\t" + "||" + "\t" + "Delivery Boy Name\t" + "||" + "\t" + "Delivery Boy Contact No.\t" + "||" + "\t" + "Delivery Boy Age\t" + "||" + "\t" + "Delivery Boy Salary")
        print("=" * 100, "\n")
        print("-" * 100)
        for val in ls:
            ls1 = val.split(",")
            print(ls1[0] + "\t" + "||" + "\t" + ls1[1] + "\t" + "||" + "\t" + ls1[2] + "\t" + "||" + "\t" + ls1[3] + "\t" + "||" + "\t" + ls1[4])
            print("-" * 100)

        print("\n", "*" * 50, "END", "*" * 50)


while True:
    print()
    print("--- Select Options ---")
    print("1. Add New Hotel.")
    print("2. Add New Dish.")
    print("3. Update Price.")
    print("4. Add New Delivery Boy.")
    print("5. Add Offers.")
    print("6. Add Menu.")
    print("7. Show All Hotels.")
    print("8. Show All Dishes.")
    print("9. Info.")
    print("0. Exit.")
    ch = int(input("Enter Your Choice :- "))

    if ch == 1:
        add_hotel()

    elif ch == 2:
        add_dish()

    elif ch == 3:
        update_price()

    elif ch == 4:
        add_delivery_boy()

    elif ch == 5:
        add_offers()

    elif ch == 6:
        add_menu()

    elif ch == 7:
        all_hotels()

    elif ch == 8:
        all_dishes()

    elif ch == 9:
        info()

    elif ch == 0:
        break