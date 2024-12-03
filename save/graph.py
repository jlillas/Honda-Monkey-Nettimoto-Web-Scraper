import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

# Function to parse the values from the .txt file
def parse_file(file_path):
    data = {}
    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expressions to find the numerical values
    data['amount'] = int(re.search(r'amount\s*=\s*(\d+)', content).group(1))
    data['total'] = int(re.search(r'total\s*=\s*(\d+)', content).group(1))
    data['median'] = float(re.search(r'median\s*=\s*([\d.]+)', content).group(1))
    data['mean'] = float(re.search(r'mean\s*=\s*([\d.]+)', content).group(1))
    data['min'] = int(re.search(r'min\s*=\s*(\d+)', content).group(1))
    data['max'] = int(re.search(r'max\s*=\s*(\d+)', content).group(1))
    data['profit'] = float(re.search(r'profit\s*=\s*([\d.]+)', content).group(1))

    return data

# Function to extract the datetime from the filename
def extract_datetime_from_filename(filename):
    # Example filename: "Suzuki_PV_Prices_2024-05-16_13-59"
    date_time_str = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2})', filename).group(1)
    # Convert the extracted string into a datetime object
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d_%H-%M')
    return date_time_obj

# Function to search for all .txt files in the folder and extract data
def find_txt_files_and_extract_data():
    extracted_data = []
    folder = os.getcwd()  # Get the current working directory

    # Iterate through all files in the current directory
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder, filename)
            data = parse_file(file_path)
            timestamp = extract_datetime_from_filename(filename)
            extracted_data.append((timestamp, data))

    # Sort the data by datetime (in case the files are not in order)
    extracted_data.sort(key=lambda x: x[0])
    
    return extracted_data

# Function to plot the data using matplotlib without the total
def plot_data_in_one_graph(data_list):
    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Titles and colors for each parameter, excluding 'total'
    keys = ['amount', 'median', 'mean', 'min', 'max', 'profit']
    titles = ['Amount', 'Median', 'Mean', 'Min', 'Max', 'Profit']
    colors = ['blue', 'orange', 'red', 'purple', 'brown', 'pink']
    
    # Plot each parameter on the same graph
    for idx, key in enumerate(keys):
        values = [data[1][key] for data in data_list]
        timestamps = [data[0] for data in data_list]
        
        plt.plot(timestamps, values, marker='o', label=titles[idx], color=colors[idx])

    # Set plot details
    plt.title('Comparison of Parameters over Time (Excluding Total)')
    plt.xlabel('Date and Time')
    plt.ylabel('Values')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
    plt.legend(loc='upper left')  # Show legend to differentiate between parameters
    plt.tight_layout()

    # Show the plot
    plt.show()

# Main function
def main():
    data_list = find_txt_files_and_extract_data()
    if data_list:
        plot_data_in_one_graph(data_list)
    else:
        print("No .txt files found in the directory.")

if __name__ == '__main__':
    main()
