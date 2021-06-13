def is_palindrome(num):
    # Skip single-digit inputs
    if num//10 == 0:
        return False
    temporary = num
    reversed_num = 0

    while temporary != 0:
        print(f"{reversed_num * 10} {temporary%10}")

        reversed_num = (reversed_num * 10) + (temporary % 10)
        print(f"reversed_num {reversed_num}")
        temporary = temporary//10
        print(f" temporaryi {temporary}")


    if num == reversed_num:
        return num
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        print("is palindrome" if is_palindrome(int(sys.argv[1])) else "Not a palindrome")
    else:
        pal_gen = infinite_palindromes()

        #for i in range(10):
        #    print(next(pal_gen))
        #    pal_gen.send(i*50000000)
    
        for i in pal_gen:
            print(i)
            digits = len(str(i))
            if digits == 8:
                print("limit reached...")
                pal_gen.close()

