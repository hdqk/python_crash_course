# print("Python")
# print("\tPython") #\t adds a tab
# print("Languages:\nPython\nC\nJavascript") #\n adds a newline
# print("Languages:\n\tPython\n\tC\n\tJavascript") #combined

# favorite_language = " python "
# print(favorite_language)
# print(f"'{favorite_language.lstrip()}' left stripped") #strips whitespace from left
# print(f"'{favorite_language.rstrip()}' right stripped") #strips whitespace from right
# print(f"'{favorite_language.strip()}' fully stripped") #strips whitespace from both sides
# print(favorite_language)
# favorite_language = favorite_language.strip() #assigns stripped value to variable
# print(favorite_language)

nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://")) #remove a given prefix string
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)