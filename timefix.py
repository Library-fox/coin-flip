import time
basestring= time.asctime()

#isolates clock
stringclock=basestring
length1=len(stringclock)
length1=length1-13
stringclock=stringclock[length1:]
stringclock=stringclock[:-5]
lengthclock=len(stringclock)+1

#isolates hours minutes and seconds
stringtime=stringclock
hours=stringtime[:-6]
minutes=stringtime[3:-3]
seconds=stringtime[6:]

#converts time bits back into a single string
finalclock=str(hours)+';'+str(minutes)+';'+str(seconds)

#isolates year
stringyear=basestring
length=len(stringyear)
stringyear=stringyear[-4:]
lengthyear=len(stringyear)+1

#isolates day 
stringday=basestring
cutlength1=lengthyear+lengthclock
stringday=stringday[4:]
stringday=stringday[:-cutlength1]
stringmonth=stringday #for later
stringday=stringday[5:]

#isolates month
length2=len(stringmonth)
length2=length2-3
stringmonth=stringmonth[:length2]

#strings everything back together into a date and time
finalstring=stringmonth+' '+stringday+' '+stringyear+' '+finalclock
