import csv
import os
import datetime

def mood_record(rating):
    if os.path.isfile("mood_history.csv") == False:
        with open("mood_history.csv", 'w', newline='') as file:
            record = csv.writer(file)
            record.writerow(["Date", "Time", "Rating", "Comment"])
        file.close()
    history = open("mood_history.csv", 'a', newline = '')
    writehistory = csv.writer(history)
    writehistory.writerow(rating)
    history.close()

def main():
    rating = []
    os.system('cls')
    print("Hey! How are you doing?")
    rating.append(str(datetime.datetime.now())[:10])
    rating.append(str(datetime.datetime.now())[11:19])
    rate = float(input("Between 1-5, how do you rate your mood?\n"))
    if rate >= 1 and rate <= 5:
        rating.append(rate)
    else:
        print("Invalid Rating. Try again.\n")
        main()
    rating.append(input("Any notes to add with this?\n"))
    mood_record(rating)
    os.system('cls')

working = True
while working == True:
    print ("Welcome to mooder. Select an option below.\n You can rate your mood:\n1. Now\n2. Another Time\n3. View Ratings\n4. Chart Ratings\n5. Exit\n6. Clear History\n")
    select = input("Select an option.\n")
    if select == "1":
        main()
    elif select == "2":
        print ("feature not available yet\n")
    elif select == "3":
        print ("feature not available yet\n")
    elif select == "4":
        print ("feature not available yet\n")
    elif select == "5":
        working = False
    elif select == "6":
        confirm = input ("Are you sure you want to proceed?\nAll previous data will be deleted! y to proceed\n")
        if confirm == "y":
            try:
                os.remove("mood_history.csv")
            except:
                print("File has already been deleted.")
        else:
            pass
    else:
        print("Invalid selection!\n")
print("Have a great day!")