num = 14063542789
numStr = str(num)
numArr = []

print('\n------------')
for digit in str(num):
    numArr.append(int(digit))
    print (digit, end='')

print('\n------------\n')

index = 1
sum =0

for x in range(9):
    print('index involved',index,index+1,index+2)

    mergedStr = numStr[index-1]+numStr[index]+numStr[index+1]

    if(int(mergedStr)%index == 0):
        print(f'{mergedStr}/{index} = ', int(mergedStr)/index, end = '\n\n')
    else:
        print(f'{mergedStr}/{index} not divisible ..', end = '\n\n')
    sum = numArr[index-1]+numArr[index]+numArr[index+1]
    index += 1 

