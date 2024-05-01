def mult_list(numbers):
    if not numbers:  
        return None  
    product = 1
    for number in numbers:
        product *= number
    return product


print(mult_list([1, 2, 3, 4]))  
print(mult_list([]))            
