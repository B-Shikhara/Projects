#A program to display the calendar of a particular month

#importing the calendar module
import calendar

#Enter the year and month
yy= int(input("Enter the Year: "))
mm=int(input("Enter the Month: "))

print(calendar.month(yy,mm))#print the calendar of month entered
