l = [False, "Subham", "Shubi","Rohan","Sahil", 1 , 1.89]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1  # *** If you add =+ instead of += , python will create infinte loop of index one that 
           # is Subham after printing 0 index "False" as =+ is evaluated as i = (+1). You are 
           # reassigning i to the positive number 1 over and over again.
