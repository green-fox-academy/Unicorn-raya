class Fibonacci:
    def fibo(self,number):
        if number == 0:
            return 0
        elif number == 1:
            return 1 
        else:
            return self.fibo(number - 2) + self.fibo(number - 1)

print(Fibonacci().fibo(5))