def fizzbuzz(max_num):
    FizzBuzz = []
    Fizz = []
    Buzz = []
    Neither = []


    """Loops through 1-max_num and prints message depending on evaluation of integer."""
    for num in range(1, max_num):
        fizz_buzz_dict = {}
        if num % 3 == 0 and num % 5 == 0:
            FizzBuzz.append(num)
            print(FizzBuzz)
        elif num % 3 == 0:
            Fizz.append(num)
            print(Fizz)
        elif num % 5 == 0:
            Buzz.append(num)
            print(Buzz)
        else:
            Neither.append(num)
            print(Neither)
    return fizz_buzz_dict

fizzbuzz(21)
