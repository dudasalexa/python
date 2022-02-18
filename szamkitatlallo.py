import random
import math

lower = int(input("írd be az alsó számhatárt:- "))
 

upper = int(input("írd be az felső számhatárt:- "))
 

x = random.randint(lower, upper)
print("\n\t",
       round(math.log(upper - lower + 1, 2)),
      " lehetőséged van tippelni\n")
 

count = 0
 

while count < math.log(upper - lower + 1, 2):
    count += 1
 
    guess = int(input("írj be egy számot:- "))
 
    if x == guess:
        
        print("gratulálok kitaláltad a(z)",
              count,". próbálkozásra")

        break
    elif x > guess:
        print("kisebb számra tippeltél")
    elif x < guess:
        print("nagyobb számra tippeltél")
 

if count >= math.log(upper - lower + 1, 2):
    print("\nA szám a(z) %d volt" % x)
 
