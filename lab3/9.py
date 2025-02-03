import math

def war_kolem(radius):
    return (4/3) * math.pi * (radius ** 3)


r = float(input("Шардың радиусын: "))
print("Шардың көлемі:", war_kolem(r))