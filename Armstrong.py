# Check if a number is Armstrong
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

print(is_armstrong(153))  # True
