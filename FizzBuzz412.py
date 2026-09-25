class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        Fizzbuzz = []
        for i in range(n):
            if ((i+1) % 3) == 0 and ((i+1) % 5) == 0:
                Fizzbuzz.append("FizzBuzz")
            elif ((i+1) % 3) == 0 and ((i+1) % 5) != 0:
                Fizzbuzz.append("Fizz")
            elif ((i+1) % 3) != 0 and ((i+1) % 5) == 0:
                Fizzbuzz.append("Buzz")
            else :
                Fizzbuzz.append(str(i+1))
        return Fizzbuzz


