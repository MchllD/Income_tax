# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20


# pseudocode

# Set initial values
# Display the given income
# Check income ranges and calculate tax payable accordingly
# No tax if income is up to 10000
# Calculate tax for income between 10001 and 20000
# Calculate tax for income above 20000
# # Tax for the first 10000
# Tax for the remaining income above 20000
# Display the total tax to pay

# -------------------------------------- actual code -------------------------------------------------------

# Set initial values
income = 45000
tax_payable = 0

# Display the given income
print ("Given income:", income)


# Check income ranges and calculate tax payable accordingly
if income <= 10000:
    # No tax if income is up to 10000
    tax_payable = 0
elif income <= 20000:
    # Calculate tax for income between 10001 and 20000
    x = income - 10000
    tax_payable = x * 0.10
else:
    # Calculate tax for income above 20000
    tax_payable = 0
    
    # Tax for the first 10000
    tax_payable += 10000 * 0.10
    