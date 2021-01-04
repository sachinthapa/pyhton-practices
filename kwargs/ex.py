def my_sum(*args):
    result = 0 ;
    for x in args:
        result += x;
    return result

print(my_sum(1,2,3,4,5))

my_list = [1,2,3,4,5]

print('DEFAULT = ', my_list)
print('UNPACKED = ', *my_list)

# unpacking_call.py
def my_sum_unpacking(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum_unpacking(*my_list)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [1,2,3,4]

print("MULT LIST SUM = ", my_sum(*list1, *list2, *list3))

a, *b, c = list1 #unpack list to fields

my_merged_list = [*list1, *list2]
print("my_merged_list = ",  my_merged_list)

my_list_string = [*"MYNAMEISSACHIN"]

*my_list_string_myst, = "MYNAMEISSACHIN"
print("my_list_string = ",  my_list_string)
print("my_list_string_myst = ",  my_list_string_myst)



