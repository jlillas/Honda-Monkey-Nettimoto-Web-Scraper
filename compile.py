import pandas as pd
import datetime

# Read the .csv file
file_path = 'prices.csv'  # Update this path to the location of your .csv file
df = pd.read_csv(file_path, header=None, skiprows=1, names=['Award'])

# Ensure all values are strings and clean the data
df['Award'] = df['Award'].astype(str).str.replace(',', '').str.strip()

# Convert the 'Award' column to numeric, handling any errors
df['Award'] = pd.to_numeric(df['Award'], errors='coerce')

# Drop any rows with NaN values
df.dropna(inplace=True)

# Calculate total, median, and mean
total = df['Award'].sum()
median = df['Award'].median()
mean = df['Award'].mean()
amount = round(total / mean)
mean = round(mean, 2)
min_value = df['Award'].min()
max_value = df['Award'].max()
profit = round(mean - min_value, 2)

# Print the results
print(f"Amount: {amount}")
print(f"Total: {total} €")
print(f"Median: {median} €")
print(f"Mean: {mean} €")
print(f"Min: {min_value} €")
print(f"Max: {max_value} €")
print(f"Profit: {profit} €")

# Define the content to be saved
content = f"""amount = {amount}
total = {total}
median = {median}
mean = {mean}
min = {min_value}
max = {max_value}
profit = {profit}
"""

save = str(input("y or n: "))

if save == "y":

    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the date and time to match the desired file name format
    file_name = current_time.strftime("Honda_Monkey_Prices_%Y-%m-%d_%H-%M.txt")

    # Save the content to the file
    with open(file_name, "w") as file:
        file.write(content)

    print(f"File '{file_name}' has been created with the specified content.")
    
if save != "y":
    print("this did not save.")