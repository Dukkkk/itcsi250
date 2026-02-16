annual_salary = int(input("Ta jiliin orlogo oo oruulna uu: "))
total_cost = 1000000
months = 36
down_payment = 250000
r = 0.04
semi_annual_raise = 0.07

low = 0
high = 10000
steps = 0
best_rate = None

while low <= high:
    steps += 1
    guess = (low + high) // 2
    portion_saved = guess / 10000

    current_savings = 0
    annual_salary_temp = annual_salary

    for month in range(1, months + 1):
        current_savings += (annual_salary_temp / 12) * portion_saved + (current_savings * r / 12)

        if month % 6 == 0:
            annual_salary_temp += annual_salary_temp * semi_annual_raise
    
    if abs(current_savings - down_payment) <= 100:
        best_rate = portion_saved
        break
    elif current_savings < down_payment:
        low = guess + 1
    else:
        high = guess - 1

if best_rate is None:
    print("Ta 36 sariin dotor bairnii down payment-iig hadgalj chadahgui baina.")
else:
    print("Tanii hadgalah heregtei huvi: ", best_rate)
    print("Tanii hadgalah heregtei saruudiin too: ", steps)