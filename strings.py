 #string always in double quotes
#string are immutable 

apple="he wants to east apple"
print("heelo" +apple)
print("heelo" ,apple)

name="""Sharjeel 
        Saleem """

apple1='He said "i want to eat apple" '
print(apple1)
print(apple[0])
print(len(apple))

#now we move to string methods
#len
print(len(apple))
#to upper code
a="sharjeel is a     beautifull boy "
f="    "
b="yasir sharjeel IN SHA ALLAH part of Dataventiv"
c="ABC"
D="abc"
g="WORLD COMPANY"
print(a.upper())
print(a.lower())
print(a.strip('!')) # strip is used to remove  the item overall in string
print(a.rstrip("!"))# rstrip removes only last
print(a.replace("Sharjeel1","sharjeel11"))# replace old with new 
print(b.split(" "))# it will give gap between the string
print(a.capitalize())#it capitalize first word
print(a.endswith("@"))
print(a.endswith("ir",0,5))# it will only check that between these indexes if a part of string ends with is
print(a.find("is")) #if not foundd return -1
print(a.index("is"))# it same as find but it ggive exception and on find we got index -1
print(c.isalnum())#it only give true when entire string is capirtaloer small or 0-9
print(a.isalpha())# only check if the string ia A-Z or a-z
print(c.islower())#give true only when the complete string is small
print(a.isupper())# give true when the complete string is uppercase
print(a.isprintable())# give true if these is no specil character
print(f.isspace())#give true when theere is only space
print(g.istitle())#search
print(a.startswith("sharjeel"))
print(a.swapcase())#upper to lower and lower to upper 




















