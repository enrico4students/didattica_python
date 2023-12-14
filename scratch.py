x = 10

for y in [2, 0]:
    try:
        z = x/y
    except Exception as myExc:
        print(f"ECCEZIONE {type(myExc)}: il divisore è {y}, non possibile")
    finally:
        print("Tutto fatto")