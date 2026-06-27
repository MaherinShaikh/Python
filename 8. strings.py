name = "maherin"
print("hiii, " + name)

apple = 'an apple a day keeps the "doctor" away'
print(apple)

sentence = """This is a long sentence.

It has multiple lines.

This is the third line."""     #can be done with '''   ''' as well
print(sentence) 

#escape sequences
# \n - new line
# \t - tab space
# \\ - backslash    
# \' - single quote
# \" - double quote 

story = 'She said, "It\'s a beautiful day.\nLet\'s go out!"'
print(story)

#accessing characters in a string
fruit = "banana"
print(fruit[0])  #b
print(fruit[1])  #a
print(fruit[2])  #n
print(fruit[3])  #a
print(fruit[4])  #n
print(fruit[5])  #a
# print(fruit[6])  #error. index out of range
print(fruit[-1])  #a
print(fruit[-2])  #n

for char in story:
    print(char)
