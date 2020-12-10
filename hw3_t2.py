while True:
    number = int(input('Your four-digit number: '))
    if len(str(number)) == 4:
        break
    else:
        print ('Error! Use four-digit number!')

#1 product
number_list = list(str(number))
number_product = int(number_list[0]) * int(number_list[1]) * int(number_list[2]) * int(number_list[3])
print (f'Your product number:', number_product)

#2 reverse
reversed_number = 0
while number>0:
     remainder = number % 10
     reversed_number = (reversed_number * 10) + remainder
     number = number//10
print('Your reversed number: {}'.format(reversed_number)) 

#3 sort
number_list.sort()
number_sorted = int(''.join(number_list))
print(f'Your sorted number: {number_sorted}')