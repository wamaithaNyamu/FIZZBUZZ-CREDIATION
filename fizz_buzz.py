# CREDIATION TASK ONE:

def fizzbuzz(start, end):
    """
       prints the numbers from 1 to 100.
       But for multiples of three print "Fizz" instead of the number
       and for the multiples of five print "Buzz".
       For numbers which are multiples of both three and five print "FizzBuzz".

       Parameters:
         start - range start
         end - range end
    """
    for i in range(start, end + 1):
        # if the current number when divided by 15 is 0, its a multiple of both 3 and 5 print Fizzbuzz
        if i % 15 == 0:
            print("FizzBuzz")
        # if the current number when divided by 3 is 0, its a multiple of 3  Fizz
        elif i % 3 == 0:
            print("Fizz")

        # if the current number when divided by 5 is 0, its a multiple of 5  Buzz
        elif i % 5 == 0:
            print("Buzz")

        # if the current number is not a multiple of 3 and 5 print the number
        else:
            print(i)


fizzbuzz(1, 100)
