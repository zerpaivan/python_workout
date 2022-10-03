
def checkmulti(num):
    label = ""
    div_label = {3:"Fizz", 5:"Buzz", 7:"Wo"}
    for n in div_label:
        if num % n == 0:
            label += div_label[n]
    if not label:
        label = num
    return label

for i in range(1,101):
    print(checkmulti(i))