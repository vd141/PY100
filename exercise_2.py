def even_or_odd(input_num):
    print('Even' if input_num%2 == 0 else 'Odd')

def upper_if_over_ten(input_string):
    if len(input_string) > 10:
        return input_string.upper()
    else:
        return input_string.lower()

even_or_odd(1)
even_or_odd(2)

print(upper_if_over_ten("roooooooooooor"))

def number_range(an_int):
    if an_int >= 0 and an_int <= 50:
        print(f'{an_int} is between 0 and 50')
    elif an_int > 50 and an_int <= 100:
        print(f'{an_int} is between 51 and 100')
    elif an_int > 100:
        print(f'{an_int} is greater than 100')
    else:
        print(f'{an_int} is less than 0')
    
number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)