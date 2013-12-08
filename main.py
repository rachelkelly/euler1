# Hey!  Hey you!  Yeah, you!  Don't read this if you haven't figured it out yourself!
# Need a hint?  Explore the difference between python's different kinds of division.



























i=1
threebox = 0
fivebox = 0
while i < 1000:
    if i%3==0:
        #print (i," fizz!")
        threebox += i
    elif i%5==0:
        #print (i," bang!")
        fivebox += i
    elif i%15==0:
        fivebox -= i
    else:
        #print ("not in three/fivebox:",i)
    i += 1

print (threebox + fivebox)
