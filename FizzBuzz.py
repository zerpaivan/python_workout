def check_multi(num):
    label = ""
    if num % 3 == 0:
        label = "Fizz"
    if num % 5 == 0:
        label = label + "Buzz"
    if label == "":
        return num
    else: 
        return label

for i in range(1, 101):
    print(check_multi(i))