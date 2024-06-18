# prime number checker
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True
print(is_prime(3))

# to Sum numbers 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(sum_of_digits(123))  

# unique element in list
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
print(unique_elements([1, 2, 3, 1, 2, 4]))  # [1, 2, 3, 4]
print(unique_elements(['a', 'b', 'a', 'c']))  # ['a', 'b', 'c'] 5, 5]))  


# check  anagram or not
def anagram(str1,str2):
    return sorted(str1)==sorted(str2)
print(anagram('hello', 'hi'))  


# merge two lists 
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  