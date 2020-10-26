def check_if_ok(test_number):
    if(test_number % 3==0 and test_number % 5 ==0):
        print(number)
        print("Fizzbuzz")
        print("------------")
        return
    elif(test_number % 3==0):
        print(number)
        print("Fizz")
        print("-------------")
        return
    elif(test_number % 5 ==0):
        print(number)
        print("Buzz")
        print("-------------")
        return
    else:
        print(number)
        print("cann't divisible by 3 0r 5")
        print("--------------")
        return


for number in range(1,16):
    check_if_ok(number)
    