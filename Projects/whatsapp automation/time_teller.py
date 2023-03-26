import time
hour=int(time.strftime('%H'))
#print ("hour is ",hour)
minute=int(time.strftime('%M'))
#print ("minute is ",minute)
sec=int(time.strftime('%S'))
#print ("seconds  is ",sec)
print ("Current time is ",time.strftime("%H : %M : %S "))
if (hour < 12 ):
    print("Good morning")
elif (hour <4 and hour > 12):
    print ("good afternoon")
elif (hour <9 and hour >5):
    print ("good evening")
else :
    print ("good night")