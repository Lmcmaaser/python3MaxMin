largest = None
smallest = None
print('Please enter numbers, and then type the word done when complete.')
while True:
    value = input('Enter a number:\n')
    if value == 'done':
        break
    try:
        ivalue = int(value)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = ivalue
    elif ivalue < smallest:
        smallest = ivalue

    if largest is None:
        largest = ivalue
    elif ivalue > largest:
        largest = ivalue

print('Maximum is', largest)
print('Minimum is', smallest)
