def c(F):
    return 5/9*(F-32)

gulrot = 10

for F in range(0,110,10):
    print(f"{F} F = {c(F)} C")

