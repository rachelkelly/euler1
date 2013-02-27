#Copyright Creative Commons 2013 Rachel Kelly
#Project Euler #1


c = 0
i = 999
totalthree = 0
threebox = []

e = 0
k = 995
totalfive = 0
deletablek = 0
fivebox = []

total = 0
totalbox = []

while i > 0:
    c = totalthree + i
    #print(totalthree,"+",i,"=")
    i = i-3
    totalthree = c
    threebox += [c]
    #print((i//3),":",totalthree)
    #print(c)
#print("threebox:",threebox)

print("totalthree",totalthree)
input("push enter")

while k > 0:
    e = totalfive + k
    k = deletablek
    if e in threebox:
        print(e)
        #print(threebox)
        print(e,"duplicate number from previous list, not included")
        e = 0
        totalfive += e
        print("totalfive remains",totalfive)
        input("push enter.")
    elif e not in threebox:
            if deletablek in threebox:
                print(deletablek)
                print(deletablek,"duplicate number from threebox, not included")
                k = deletablek - 5
            elif deletablek not in threebox:
                k = k - 5
            else:
                print("ERROR")
    #print(totalfive,"+",k,"=")
    #totalfive += k
            fivebox += [k] #don't think I need a fivebox.  ohwell
            totalfive += k
        #print(fivebox)
# RUN A NOTEPAD THROUGH OF THIS
# CHECK THIS OUT
# RUN IT ON THROUGH WITH SOME NUMBERS YO
    else:
        print("ERROR")
    #print(totalfive)
    #print(e)
    #print(totalfive)

#print("threebox:",threebox)
#input("fuh")
#print("fivebox minus dupes:",fivebox)
input("cluh")
totalbox = threebox + fivebox
print(totalfive)

total = c + totalfive
#print(totalbox)
print("total: ",total)
