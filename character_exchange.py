# Create a string from given string where first and last characters exchanged. [eg: python –>
# nythop]

word=input("enter a word :")
change=word[-1]+word[1:-1]+word[0]
print("changed word is :",change)