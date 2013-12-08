#don't look at the answers, this is just for me!

























a = 1
b = 2
i = 0
fibobox = 2

while i < 4000000:
    i = a + b
    #print ("a:",a,". b:",b,".  together they make:",i,"which should equal",a+b,".")
    a = b
    b = i
    if i%2==0:
        print ("the number",i,"is divisible by 2!  into the box it goes.")
        fibobox += i

print ("fibobox: ",fibobox,".")

