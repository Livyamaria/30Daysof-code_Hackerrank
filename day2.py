"""Objective
In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

Example
mealcot=100
tippercent=15
tax percent=8
A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value  and return from the function.
Function Description
Complete the solve function in the editor below.

solve has the following parameters:

int meal_cost: the cost of food before tip and tax
int tip_percent: the tip percentage
int tax_percent: the tax percentage
Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.
"""







def solve(meal_cost, tip_percent, tax_percent):
    m_tip = (tip_percent * meal_cost) / 100
    m_tax = (tax_percent * meal_cost) / 100
    m_total = m_tax + m_tip + meal_cost
    print(round(m_total))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
