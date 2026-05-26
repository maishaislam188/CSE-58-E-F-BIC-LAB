temperature = input("Today's temperature: ")
temperature = int(temperature)

if temperature > 30:
    print("It is hot")
elif 20 <= temperature <= 30:
    print("It is nice")
elif temperature < 20:
    print("It is cold")
