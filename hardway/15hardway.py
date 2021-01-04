from sys import argv

script , filename = argv
txt = open(filename)

print ("Selected file name %s " % filename)
print (txt.read())

print ("Selected another file tp read ")
nxt_file = input("> ")

print (nxt_file.read())


