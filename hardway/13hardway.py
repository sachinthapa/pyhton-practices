from sys import argv

script, my_name  = argv
prompt = '> '

print ("i\'m running this script :", script)
print ("My name is ", my_name)

print ("What is your name ")
name = input(prompt)

print ("Where do you live ")
place = input(prompt)

print(".....")
print("""

So I %s asked you some questions in this scrpit %s.
You\'re name is %s and you live in %s

""" % (my_name,script,name,place))


