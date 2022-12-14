#This answers the most basic FizzBuzz leetcode question.
#if divizible by 3 and 5, string[i] = fizzbuzz
#if divizible by 3, string[i] = fizzbuzz
#if divizible by 5, string[i] = fizzbuzz
#All else, just the number


def fizzbuzz(n):
    n = int(input("Input max number: "))
    answer=[]
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i%3 == 0 and i%5 != 0:
            answer.append("Fizz")
        elif i%5 == 0 and i%3 !=0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    print(answer)

fizzbuzz(10)
