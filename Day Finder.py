import matplotlib

day, month, year = (input("Give day: "),input("Give month: "),input("Give year: "))
day = int(day)
month = int(month)
year = int(year)

#idea is to take all the days and number them
#Similar to how utc time works since it counts
#seconds from January 1st 1970 

d = 0
#Find out the number of days given by the user
#Golden, find out the difference
#2008 till end is 733422 days
#01, 01, 2009 is 733423 is 1st of January 2008
amount_y = ((year - 2000) * 365) + 730500
for i in range(2001,year):
    print(i)
    if i % 4 == 0:
        amount_y = amount_y + 1
        d = d + 1
        print ("Hello")
#print("\nAmount")
#print(amount_y)
amount_m = 0
amount_d = 0

#If the given year is a leap year 
if year % 4 == 0:
    #For loop so days in a month add until the month's number
    for i in range(1,month):
        #Every month which is odd and before July have 31 days
        if i <= 7:
            if i % 2 != 0:
                amount_m = amount_m + 31
            #February is an exception since it is the only month
            #with less than 30 days
            elif i == 2:
                amount_m = amount_m + 29
            #Else if the month is even, add 30 days
            elif i % 2 == 0:
                amount_m = amount_m + 30
        #odd months have 30 days after August
        elif i >= 8:
            #Therefore even months add 31 days
            if i % 2 == 0:
                amount_m = amount_m + 31
            #Odd months add 30 days
            elif i % 2 != 0:
                amount_m = amount_m + 30
#Else if the year is not a leap year
elif year % 4 != 0:
    for i in range(1,month):
        if i <= 7:
            if i % 2 != 0:
                amount_m = amount_m + 31
            elif i == 2:
                amount_m = amount_m + 28
            elif i % 2 == 0:
                amount_m = amount_m + 30
        elif i >= 8:
            if i % 2 == 0:
                amount_m = amount_m + 31
            elif i % 2 != 0:
                amount_m = amount_m + 30
            
#Find the amount of days and 7 plus them or subtract to find the day! Where the frame
#or base of reference is 730501 which is the first of JANUARY 2001! which is a
#MONDAY!

full_amount = amount_y + amount_m + day #(Total amount of days) Integer values
#Amount of days according to month
#print("Days uptil month")
#print(amount_m)
#print("\nFull")
#print(full_amount)

difference = full_amount - 730501 #Difference is subtracting total days from 
                                  #01/01/2001, using it as a frame of reference

#print(difference)
remainder = difference % 7 
#print(remainder)

#6 - SAT #0 - SUN #1 - MON #2 - TUE #3 - WED #4 - THU #5 - FRI
if remainder == 0:
    print("Sunday")
elif remainder == 2:
    print("Tuesday!")
elif remainder == 3:
    print("Wednesday")
elif remainder == 1:
    print("Monday")
elif remainder == 4:
    print("Thursday")
elif remainder == 6:
    print("Saturday")
elif remainder == 5:
    print("Friday!")

#Calculations when working out the problems of this program
#733,787(all of 2008) + 120 = 733907
#733422
#259 is september 16th
