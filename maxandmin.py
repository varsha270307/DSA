a=10
b=20
maximum=max(a,b)
minimum=min(a,b)
print(maximum)
print(minimum)

numbers=[12,24,45,67,88,99]
max_value=numbers[0]
min_value=numbers[0]
for i in numbers:
    if i>max_value:
        max_value=i
    if i<min_value:
        min_value=i
print("maximum value is:",max_value)
print("minimum value is:",min_value)