import random


mum =[]
for i in range(20):
    mum.append(random.randrange(1,80))
random.shuffle(mum)

print("Random numbers are: ",mum)
hold = mum[0]
toSwap = 0

for i in range (len(mum)):
    hold = mum[i]
    for g in range(len(mum)-i):
        if mum[g+i] <= hold:
            hold = mum[g+i]
            toSwap = g+i
            print("putting ", hold,"into slot", g)
    temp = mum[i]
    mum[i]=hold
    mum[toSwap]=temp

print("The smallest is ",mum[0])
    
print(mum)
