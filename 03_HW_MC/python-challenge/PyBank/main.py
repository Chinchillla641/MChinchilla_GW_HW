#dependencies
import os
import csv

csvpath = os.path.realpath("D:/Git/GWU-ARL-DATA-PT-09-2019-U-C/02-Homework/03-Python/Instructions/Part-2/PyBank/Resources/budget_data.csv")

total_months = 0
net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
 
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader, None)
    print(header)

    # Extract first row to avoid appending to net_change_list
    # YOUR CODE HERE

    for row in reader:

    # Track the total
        total_months = total_months + 1

        # Track the net change
        net = net + int(row[1])

        # Calculate the greatest increase
        if int(row[1]) > greatest_increase[1]:
            greatest_increase[1] = int(row[1])
            greatest_increase[0] = row[0]
            
        # Calculate the greatest decrease
        if int(row[1]) < greatest_decrease[1]:
            greatest_decrease[1] = int(row[1])
            greatest_decrease[0] = row[0]
            
# Calculate the Average Net Change
# YOUR CODE HERE


print(total_months)
print(net)
print(greatest_increase)
print(greatest_decrease)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
# YOUR CODE HERE

# Export the results to text file
# YOUR CODE HERE
