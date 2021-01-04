import csv

exampleFile      = open('test.csv')
exampleReader    = csv.DictReader(exampleFile,['time','name','amount'])
exampleData      = list(exampleReader)   
 
# print(exampleData)
# print(exampleData[0][0] +' '+  exampleData[0][1] +' '+ exampleData[0][2])     

for row in exampleData:
    print (row['time']+ ' ' + row['name'])


outputFile             = open('output.csv','w',newline='')
outputDictWriter       = csv.DictWriter(outputFile,['Name','Pet','Phone']) 
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Karen', 'Pet': 'dog', 'Phone': '555-1234'})
outputDictWriter.writerow({'Pet': 'cat', 'Phone': '555-1234'})
outputFile.close()


print('----------------------------------')

exampleFile             = open('exampleWithHeader.csv')
exampleDictReader       = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'])
