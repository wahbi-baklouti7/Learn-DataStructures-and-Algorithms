lst=list()
max_num=None
arr = [2,3,6,6,5]
arr_copy=set(arr)
first_largest=None
second_largest=None
for n in arr_copy:
    if not first_largest or n>first_largest:
        if first_largest:
            second_largest=first_largest
        first_largest=n


print(second_largest)
