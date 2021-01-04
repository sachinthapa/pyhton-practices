from sys import argv
from os.path import exists

scrpit, file_from, file_to = argv

print ("Copying file form %s to file %s" %(file_from,file_to))

file_from_open  =  open(file_from)
file_from_data = file_from_open.read()

print("File exists ", exists(file_to))
input("hit enter to copy ")

file_to_open = open(file_to,'w')
file_to_open.write(file_from_data)

print("copyying completed")

file_to_open.close()
file_from_open.close()
