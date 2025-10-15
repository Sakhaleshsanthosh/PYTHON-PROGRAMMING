def sum_of_digit(num):
    total=0
    while num > 0:
      digit = num % 10
      total += digit
      num  //= 10
    return total
a=int(input("Enter a number:"))
print("Sum of digits of a number=",sum_of_digit(a))

    
