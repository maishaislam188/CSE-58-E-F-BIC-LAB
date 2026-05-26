numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print(-1)
else:
    unique_numbers.sort()
    print(unique_numbers[-2])
