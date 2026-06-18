name = "Anshu"
print(name[0:3])
print(name[-3:-1])  # To find negative slicing fast and easily, you just have to remove the
                    # negative sign and replace the number with corresponding positive positions
                    # it will give the same result, i.e. 0 1 2 3 4 -> -5 -4 -3 -2- -1
print(name[2:4]) 

print(name[-5:-1])  
print(name[0:4])

print(name[:4]) # is same as print(name[0:4]) i.e. Ansh
print(name[1:]) # is same as print(name[1:5]) i.e. Ansh
print(name[:])  # is same as print(name[0:5]) i.e. Anshu

# Slicing with Skip Value: We can provide a skip value as a part of our slice like this:
# word = "amazing" 
# word[1:6:2] # mzn

a = "0123456789"
print(a[0:10:3])
# answer will be 0369 first we do 0 to 10 index that will be "0123456789" then we take 0 and skip
# 2 steps and take 3rd one as answer i.e. 03 , then skip 2 and take 3rd one i.e. 036 and so on....

