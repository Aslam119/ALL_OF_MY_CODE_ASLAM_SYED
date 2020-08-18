
import time

p = float(input("Enter The Principal: "))
r = float(input("Enter The Rate: "))
t = float(input("Enter The Time: "))
print("COMPUTER IS CALCULATING THE SIMPLE INTEREST......")
time.sleep(1)
i = float((p * r * t) / 100)
print("YOUR SIMPLE INTEREST IS Rs ", i)
