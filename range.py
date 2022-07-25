 #print  odd numbers
odd_number = range(1,100,2)
for x in odd_number:
    print(x)
# Printing fizz buzz
def fizz_buzz():
    for fizzbuzz in range(51):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
        elif fizzbuzz % 3 == 0:
            print("fizz")
        elif fizzbuzz % 5 == 0:
            print("buzz")
        else:
            print(fizzbuzz)
fizz_buzz()
