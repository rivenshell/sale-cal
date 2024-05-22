print("I will calculate the percentage of your item sale!")
# n = input()

#logic
def percentCal(firstnum, secondnum) -> float:
    if secondnum == 0:
        return "You cant divide by zero silly..... or can you?"
    
    percentage = (firstnum / secondnum) * 100
    return percentage

#input
firstnum = float(input("Sale price (1/2): "))
secondnum = float(input("Original Price (2/2): "))

result = percentCal(firstnum, secondnum)

if isinstance(result, float):
    print(f"You saved {result}%")
else:
    print(result)
