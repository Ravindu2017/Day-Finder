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
print("\nAmount")
print(amount_y)
amount_m = 0
amount_d = 0
##if year % 4 == 0:
####    if month <= 7:
####        if month % 2 != 0:
####            
####    elif month >= 8:
####        if month % 2 == 0:
##    for i in range(0,month):
##        if month <= 7:
##            if month % 2 != 0:
##                amount_m = amount_m + 31
##            elif month == 2:
##                amount_m = amount_m + 29
##            amount_m = amount_m + 30
##        elif month >= 8:
##            if month % 2 == 0:
##                amount_m = amount_m + 31
##            amount_m = amount_m + 30
##
##elif year % 4 != 0:
##    for i in range(0,month):
##        if month <= 7:
##            if month % 2 != 0:
##                amount_m = amount_m + 31
##            elif month == 2:
##                amount_m = amount_m + 28
##            amount_m = amount_m + 30
##        elif month >= 8:
##            if month % 2 == 0:
##                amount_m = amount_m + 31
##            amount_m = amount_m + 30

if year % 4 == 0:
    for i in range(1,month):
        if i <= 7:
            if i % 2 != 0:
                amount_m = amount_m + 31
            elif i == 2:
                amount_m = amount_m + 29
            elif i % 2 == 0:
                amount_m = amount_m + 30
        elif i >= 8:
            if i % 2 == 0:
                amount_m = amount_m + 31
            elif i % 2 != 0:
                amount_m = amount_m + 30

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

full_amount = amount_y + amount_m + day #(Total amount of days)
#Amount of days according to month
print("Days uptil month")
print(amount_m)
print("\nFull")
print(full_amount)

difference = full_amount - 730501

print(difference)
remainder = difference % 7
print(remainder)
if difference % 4 == 0:
    print("Friday")
elif difference % 5 == 0:
    print("Saturday")
elif difference % 3 == 0:
    print("Thurday")
elif difference % 7 == 0:
    print("Monday")
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
#733,787(all of 2008) + 120 = 733907
#733422
#259 is september 16th
#1 is a sunday
#2 is a monday
#3 is a tuesday
#4 is a wednesday
#5 is a Thursday
#6 is a Friday
#0 is a saturday
##if year % 4 == 0:
##    
##    
##elif day and month == 1:
##    if year == 2001:
##        print("Monday")
##September is
'''01 01 2001 is a Monday
    111 is my obsession
    Up till 2001 there has been
    500 leap years
    730500 is all 2000 years
    2001,1,1 in days is
    1500*365+500*366+1=730501
    730501 - Monday
         2
         3
         4
         5
         6
         7
    730508 - Monday

    732922
'''
#print(day+1,month+2,year+5)
