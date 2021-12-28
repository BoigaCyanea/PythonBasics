num_init = int(input("Enter an integer: "))
gr_dig = 0
num = num_init

while num > 0:
     digit = num % 10
     if digit > gr_dig:
         gr_dig = digit
         if gr_dig == 9:
             break
     num = num // 10

print(f"the biggest digit in the number {num_init} is {gr_dig}")