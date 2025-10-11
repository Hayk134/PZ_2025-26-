k = int(input("написать число от 1 до 365: "))

a = 1

day = (a+(k-1)) % 7

nedelya = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

print(nedelya[day])