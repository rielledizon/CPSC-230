# converts seconds in a day to hour, minute, seconds
time = int(input("Enter a number from 1 to 86400: "))
hour = time // 3600
# 3600 = seconds in an hour
minute = (time % 3600) // 60
# quotient remainder of time divided by 60 = seconds in a minute
sec = (time % 3600) - (minute * 60)
# must convert everything to seconds to get remaining seconds
print (time, "seconds is equivalent to", hour, "hours,",
       minute, "minutes, and", sec, "seconds.")
# linebreak to keep all in one window without scrolling
