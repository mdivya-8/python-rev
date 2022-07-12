#datetime
import datetime      #displays the current date time
x=datetime.datetime.now()
print(x)
print(x.strftime("%p"))  # AM/PM
print(x.strftime("%M"))  # minute 00-59
print(x.strftime("%S"))  #second 00-59
print(x.strftime("%j"))  #num of days in a year
print(x.strftime("%f"))  #microsecond
###Returning the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)    #it gives the year
print(x.strftime("%A"))  #strftime formates the date into string
                         #%A gives the weekday
print(x.strftime("%a"))  #%a gives the weekday as short like sun,mon..etc.,
###Create a date object:
import datetime

x = datetime.datetime(2022, 7, 12)

print(x)

#Display the name of the month:
import datetime

x = datetime.datetime(2022, 7, 12)

print(x.strftime("%B"))  #%B gives the month name
print(x.strftime("%b")) # gives month name in short version
print(x.strftime("%m")) #gives month as a num 01-12
print(x.strftime("%y")) # years as short without century
print(x.strftime("%Y"))  #year as full version
print(x.strftime("%C"))  #century
print(x.strftime("%x"))  #local version of date
print(x.strftime("%X"))  #local version of time
import datetime

x = datetime.datetime(2022, 7, 12)

print(x.strftime("%w")) #%w weekday as a number as 0-6
