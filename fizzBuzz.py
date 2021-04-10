  # F I Z Z B U Z Z
  # return FIZZBUZZ for every number divisible by 3 and 5, 
  # Buzz for every number divisible by 5,
  # and Fizz for every number divisible by 3!
for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FIZZ BUZZ!!!")
    elif number % 5 == 0:
        print("Buzz!")
    elif number % 3 == 0:
        print("Fizz!")
    else:
        print(number)
