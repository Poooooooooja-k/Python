# strings are immutable 
# new strings are made as copy of original and its changed
a="!!!! pooja!!! !!!!!!"
print(len(a))
print(a.lower())
print(a.upper())
# rstrip():removes any trailling characters
print(a.rstrip("!"))
print(a.replace("pooja","anu"))
print(a.split(" "))
heading="introduction to python"
print(heading.capitalize())
# convert the 1st character to uppercase and rest to lowercase
str1="welcome to console"
print(str1.center(50))
# aligns string to the center as per the parameters given
new="hi hlo hi hlo"
print(new.count("hlo"))
st="welcome to the console!!!"
print(st.endswith("!!"))
print(st.endswith("to",4,10))
# checks is the given string ends
strr="my name is pooja"
print(strr.find("is"))
# searches for the 1st occurance of the given value and returns the index where it is present
s="WelcomeToTheConsole00"
print(s.isalnum())
# returns true only if the entire string only consists of A-Z,a-z,0-9
print(s.isalpha())
# returns true only if entire stringh consists of A-Z,a-z
y="hello word"
print(y.islower())
# checks if the string is lower or not 
e=" "
print(e.isspace())
# returns true only if contains white spaces
q="World Health Organization"
print(q.istitle())
# returns true only if the 1st letter of each word of the string is capitalized
z="HI POOJA"
print(z.isupper())
x="python is easy"
print(x.startswith("python"))
# cheks if the string startswith given value
print(x.swapcase())
# converts lowercase to upper and uppercase to lower
print(x.title())
# capitalizes each letter of the word within the string
