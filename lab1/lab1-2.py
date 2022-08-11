num1, num2 = map(int, input('*** multiplication or sum ***\nEnter num1 num2 : ').split(' '))

if num1 * num2 > 1000:
  print('The result is {}'.format(num1 + num2))
else:
  print('The result is {}'.format(num1 * num2))