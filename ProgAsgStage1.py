##Name and ID
##Date created: 24 Feb, 2022
##Date last changed: 24 Feb, 2022
##This program prints the menu to choose the option i.e. Athletes information, search athletes and exit
##the athletes information prints all the details of athletes in the list,
##search athletes searches the sport in the list and displays the entire row of than sport
#constant for the list of the atheletes with the details
ATHLETES = [[1, "Bart", "Walsh", "Male", 23, 75, 178, "Blue", "Tennis", "B"],
            [2, "Beth", "Wolf", "Female", 25, 55, 162, "Black", "Tabletennis", "A"],
            [3, "Blaine", "Mann", "Male", 18, 70, 172, "Gray", "Volleyball", "A"],
            [4, "Chris", "House", "Female", 17, 60, 170, "Brown", "Netball", "C"],
            [5, "Dawn", "Holt", "Female", 26, 62, 177, "Green", "Volleyball", "B"],
            [6, "Earle", "Hobbs", "Male", 27, 80, 185, "Blue", "Basketball", "B"],
            [7, "Fay", "Nash", "Female", 19, 56, 158, "Amber", "Cycling", "A"],
            [8, "Gayle", "Pierce", "Female", 19, 57, "159", "Hazel", "Gymnastics", "A"],
            [9, "Glenn", "Green", "Male", 21, 71, 166, "Amber", "Tabletennis", "C"],
            [10, "Jacques", "Pace", "Male", 26, 65, 163, "Gray", "Swimming", "A"],
            [11, "Jeanne", "Riggs", "Female", 18, 62, 172, "Blue", "Netball", "B"],
            [12, "Jim", "Leach", "Male", 16, 72, 164, "Brown", "Cycling", "C"],
            [13, "Joan", "Hill", "Female", 16, 53, 164, "Black", "Netball", "C"],
            [14, "Jon", "Webb", "Male", 30, 63, 175, "Green", "Gymnastics", "A"],
            [15, "Leigh", "Graves", "Female", 31, 70, 180, "Black", "Volleyball", "A"],
            [16, "Marc", "Klein", "Male", 32, 79, 188, "Blue", "Volleyball", "C"],
            [17, "Merle", "Joyce", "Male", 24, 74, 183, "Green", "Basketball", "B"],
            [18, "Pearl", "Roach", "Female", 23, 63, 182, "Gray", "Tennis", "C"],
            [19, "Reid", "Short", "Male", 20, 66, 168, "Hazel", "Swimming", "A"],
            [20, "Shawn", "Kane", "Female", 20, 61, 174, "Brown", "Tabletennis", "A"]]


#main function
def main():
    choice = 0
    val = 0
    #while loop for menu options
    while True:
        print("\nWelcome to Athletes App!! \n")
        print("1. Athletes Information \n2. Atheletes Search \n3. Exit")
        choice = int(input("Enter your choice "))
        #for choice = 1 go to fuction printinfo to display the details of the athletes
        if choice == 1:
            printinfo()
        #for choice 2 go to function searchathletes to search the details of the items from the list of athletes
        elif choice == 2:
            searchathletes(ATHLETES)
        #exit the program for choice 3
        elif choice == 3:
            break
        else:
            print("Invalid Option Provided")

#function to display the details of the athletes
def printinfo():
    print("Athelete Number\tFirstname\tLastname\tGender\t\t   Age\t\t  Weight\t     Height\t\tEyecolor\t  Sport\t\t  Class")
    #print the details of each atheletes in a row
    for row in ATHLETES:
        print(f'{row[0]: <18}{row[1]: <18}{row[2]: <13}{row[3]: <18}{row[4]: <18}{row[5]: <18}{row[6]: <18}{row[7]: <18}{row[8]: <18}{row[9]: <18}')

    print("Press 1 to go back to main menu, or any key to exit the program: ")
    i = int(input(f"Enter a number: "))
    #if the number is 1 go to main menu
    if (i == 1):
        main()
    #otherwise exit the program
    elif (i != 1):
        print("Goodbye! Hope to see you next time")
        exit()

#function to search the provided item from the list
def searchathletes(items):
    count=0
    val = input("Enter the sports you want to search: ")
    print("Below mentioned is the result of the search")
    print("Athelete Number\tFirstname\tLastname\tGender\t\t   Age\t\t  Weight\t     Height\t\tEyecolor\t  Sport\t\t  Class")
    #for loop in the row to search for the item
    for row in items:
        for data in row:
            #if data is the searched item then count++
            if data == val:
                count=count+1
                #print the searched item and their details in a row
                print(f'{row[0]: <18}{row[1]: <18}{row[2]: <13}{row[3]: <18}{row[4]: <18}{row[5]: <18}{row[6]: <18}{row[7]: <18}{row[8]: <18}{row[9]: <18}')

    if count==0:
        print("No item found")

    print("Press 1 to go back to main menu, or any key to exit the program: ")
    i = int(input(f"Enter a number: "))
    #if 1 is entered go to main menu
    if (i == 1):
        main()
    #else exit
    else:
        print("Goodbye! Hope to see you next time")
        exit()
#function call
main()
