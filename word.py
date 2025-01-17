# Add the 'ing' at the end of the given string, if it already ends with 'ing',then add 'ly'.

word=input("enter a word :")
if word.endswith('ing'):
    word+='ly'
else:
    word+='ing'
print(f"word is {word}")