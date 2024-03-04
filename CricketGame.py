import random

t1 = ("Virat Kohli", "Rohit Sharma", "Kedar Jadhav", "Ajinkya Rahane", "Mayank Agrawal", "Ravindra Jadeja", "MS Dhoni", "Jasprit Bumrah", "Shardul Thakur", "Bhuvneshwar Kumar", "Yuzvendra Chahal")
t2 = ("Joe Root", "Eoin Morgan", "Moeen Ali", "Jason Roy", "Domm Sibley", "Ben Stokes", "Jos Buttler", "Tom Curren", "Mark Wood", "Adil Rashid", "Jofra Archer")
r = ("0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "2", "2", "2", "2", "2", "3", "3", "3", "4", "4", "4", "4", "4", "4", "6", "6", "6", "6", "6", "W", "W", "W", "W", "W", "WD", "WD")
out = ("Run Out", "Catch Out", "Stump Out", "LBW Out")

dt1 = {"Virat Kohli":0, "Rohit Sharma":0, "Kedar Jadhav":0, "Ajinkya Rahane":0, "Mayank Agrawal":0, "Ravindra Jadeja":0, "MS Dhoni":0, "Jasprit Bumrah":0, "Shardul Thakur":0, "Bhuvneshwar Kumar":0, "Yuzvendra Chahal":0}
dt2 = {"Joe Root":0, "Eoin Morgan":0, "Moeen Ali":0, "Jason Roy":0, "Domm Sibley":0, "Ben Stokes":0, "Jos Buttler":0, "Tom Curren":0, "Mark Wood":0, "Adil Rashid":0, "Jofra Archer":0}

bat = [1,2]

team1=0
team2=0

toss = (1,1,1,1,1,2,2,2,2,2)
input("Press Enter To Toss :- ")
ts = random.choice(toss)
ts1=0
ts2=0
if ts==1:
    print("Team India Won The Toss!!!")
    print("1. Bat")
    print("2. Ball")
    ts1 = int(input("Enter Your Choice :- "))
    if ts1==1:
        print("Team India Choose To Bat")
    elif ts1==2:
        print("Team India Choose To Ball")
else:
    print("Team England Won The Toss!!!")
    print("1. Bat")
    print("2. Ball")
    ts2 = int(input("Enter Your Choice :- "))
    if ts2==1:
        print("Team England Choose To Bat")
    elif ts2==2:
        print("Team England Choose To Ball")

print()
print("Match Starts Now...")

count3=0


pl=1
bat[0]=t1[0]
bat[1]=t1[1]
i=0
count1=0
count2=0
if ts1==1 or ts2==2:
    count3 = count3 + 1
    print()
    print("India's Batting...")
    print("6 Overs Inning Starts Now...")
    while 1:
        print()
        print(bat[i], "is on Strike")
        input("Press Enter To Throw The Ball :- ")
        run = random.choice(r)
        count2 = count2 + 1
        if run == "W":
            o = random.choice(out)
            print(bat[i], "get", o, "...")
            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''
            pl = pl + 1
            bat[i] = t1[pl]
        elif run == "WD":
            print("It's a Wide Ball")
            team1 = team1 + 1
        else:
            print(bat[i], "Taken", run, "Runs.")
            val = dt1[bat[i]]
            run = int(run)
            dt1[bat[i]] = val + run
            team1 = team1 + run

        if run == 1:
            if i == 0:
                i = 1
            else:
                i = 0
        elif run == 3:
            if i == 0:
                i = 1
            else:
                i = 0


        if count2 == 6:
            print("Over Completed2")
            count1 = count1 + 1
            count2 = 0
            if i == 0:
                i = 1
            else:
                i = 0

            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1,
                  "\t\t\t\t", (pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''

        if count1 == 2:
            if count3 == 1:
                ts1 = 2
                ts2 = 1

            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")

            break
        if pl == 10:
            if count3 == 1:
                ts1 = 2
                ts2 = 1
            print("Team India All Out...")
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            break


pl=1
bat[0]=t2[0]
bat[1]=t2[1]
i=0
count1=0
count2=0
if ts1==2 or ts2==1:
    count3 = count3 + 1
    print()
    print("England's Batting...")
    print("6 Overs Inning Starts Now...")
    while 1:
        print()
        print(bat[i], "is on Strike")
        input("Press Enter To Throw The Ball :- ")
        run = random.choice(r)
        if run == "W":
            o = random.choice(out)
            print(bat[i], "get", o, "...")
            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt2[bat[0]], "\t\t\t\t\t", dt2[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''
            pl = pl + 1
            bat[i] = t2[pl]
        elif run == "WD":
            print("It's a Wide Ball")
            team2 = team2 + 1
        else:
            print(bat[i], "Taken", run, "Runs.")
            val = dt2[bat[i]]
            run = int(run)
            dt2[bat[i]] = val + run
            team2 = team2 + run

        if run == 1:
            if i == 0:
                i = 1
            else:
                i = 0
        elif run == 3:
            if i == 0:
                i = 1
            else:
                i = 0

        count2 = count2 + 1
        if count2 == 6:
            count1 = count1+1
            count2 = 0
            if i == 0:
                i = 1
            else:
                i = 0
            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt2[bat[0]], "\t\t\t\t\t", dt2[bat[1]], "\t\t\t\t\t", team1,
                  "\t\t\t\t", (pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''

        if count1 == 2:
            if count3 == 1:
                ts1 = 1
                ts2 = 2
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt2[bat[0]], "\t\t\t\t\t", dt2[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            break

        if pl == 10:
            if count3 == 1:
                ts1 = 1
                ts2 = 2
            print("Team England All Out...")
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt2[bat[0]], "\t\t\t\t\t", dt2[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            break

pl=1
bat[0]=t1[0]
bat[1]=t1[1]
i=0
print("6 Overs Inning Starts Now...")
count1=0
count2=0
if ts1==1 or ts2==2:
    count3 = count3 + 1
    print()
    print("India's Batting...")
    print("6 Overs Inning Starts Now...")
    while 1:
        print()
        print(bat[i], "is on Strike")
        input("Press Enter To Throw The Ball :- ")
        run = random.choice(r)
        if run == "W":
            o = random.choice(out)
            print(bat[i], "get", o, "...")
            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''
            pl = pl + 1
            bat[i] = t1[pl]
        elif run == "WD":
            print("It's a Wide Ball")
            team1 = team1 + 1
        else:
            print(bat[i], "Taken", run, "Runs.")
            val = dt1[bat[i]]
            run = int(run)
            dt1[bat[i]] = val + run
            team1 = team1 + run

        if run == 1:
            if i == 0:
                i = 1
            else:
                i = 0
        elif run == 3:
            if i == 0:
                i = 1
            else:
                i = 0

        count2 = count2 + 1
        if count2 == 6:
            count1 = count1 + 1
            count2 = 0
            if i == 0:
                i = 1
            else:
                i = 0
            '''
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score",
                  "\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1,
                  "\t\t\t\t", (pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            '''

        if count1 == 2:
            if count3 == 1:
                ts1 = 2
                ts2 = 1
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t",(pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            break
        if pl == 10:
            if count3 == 1:
                ts1 = 2
                ts2 = 1
            print("Team India All Out...")
            print()
            print("\t\t\t\t---SCORE BOARD---")
            print("__________________________________________________________________________________")
            print("\tOvers", "\t|\t", bat[0], "'s Score", "\t|\t", bat[1], "'s Score", "\t|\tTotal Score","\t|\tWickets", sep="")
            print("----------------------------------------------------------------------------------")
            print("\t", count1, ".", count2, "\t\t\t\t", dt1[bat[0]], "\t\t\t\t\t", dt1[bat[1]], "\t\t\t\t\t", team1, "\t\t\t\t", (pl - 1), sep="")
            print("----------------------------------------------------------------------------------")
            break




if team1>team2:
    print("Team India Won!!!")
else:
    print("Team England Won!!!")












