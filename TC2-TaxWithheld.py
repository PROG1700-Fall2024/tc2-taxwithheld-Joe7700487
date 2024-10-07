# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # introduction
    print("Tax Withholding Calculator \n")
    # init variables
    provTaxRate = 0.06
    fedTaxRate = 0.25
    provTax = 0
    fedTax = 0
    totalTax = 0
    deduction = 0
    deductRate = 0.02
    takeHome = 0
    weeklySalary = int(input("Please enter the full amount of your weekly salary: "))
    dependents = int(input("How many dependants do you have?: "))

    # calculate tax rates
    provTax = weeklySalary * provTaxRate
    fedTax = weeklySalary * fedTaxRate
    deduction = (deductRate * dependents) * weeklySalary
    totalTax = provTax + fedTax - deduction
    takeHome = weeklySalary - totalTax

    # print final answer
    print("\nProvincial Tax Withheld: ${0:.2f}".format(provTax))
    print("Federeal Tax Withheld: ${0:.2f}".format(fedTax))
    print("Dependent Deduction for 2 dependents: ${0:.2f}".format(deduction))
    print("Total Withheld: ${0:.2f}".format(totalTax))
    print("Total Take-Home Pay: ${0:.2f}".format(takeHome))

    # YOUR CODE ENDS HERE
main()
