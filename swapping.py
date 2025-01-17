# Create a single string separated with space from two strings by swapping the
# character at position 1.

str1=input("enter a string :")
str2=input("enter a string :")
res=str2[0]+str1[1:]+" "+str1[0]+str2[1:]
print(res)
