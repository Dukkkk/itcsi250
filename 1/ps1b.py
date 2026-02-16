total_cost = int(input("Ta moroodliin bairnii une oruulna uu: "))
portion_saved = float(input("Ta orlogiinhoo heden huviig hadgalah ve: "))
annual_salary = int(input("Ta jiliin orlogo oo oruulna uu: "))
semi_annual_raise = float(input("Ta hagas jiliin tsalingiin osoltoo oruulna uu: "))

if portion_saved > 1:
    portion_saved = portion_saved / 100
if semi_annual_raise > 1:
    semi_annual_raise = semi_annual_raise / 100



def calculate_months_to_save(total_cost, portion_saved, annual_salary, semi_annual_raise):
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    r = 0.04
    months = 0
    
    while current_savings < portion_down_payment:
        current_savings += (annual_salary / 12) * portion_saved + (current_savings * r / 12)
        months += 1

        if months % 6 == 0:
             annual_salary += annual_salary * semi_annual_raise  


    return months

print("Tanii hadgalah heregtei saruudiin too: ", calculate_months_to_save(total_cost, portion_saved, annual_salary, semi_annual_raise))