def equivalent_centigrade_temperatur(F):
    C = (5/9) * (F-32)
    return C

F = 35.8
C = equivalent_centigrade_temperatur(F)
print(f"{F} F.temp = {C} E.temp ")