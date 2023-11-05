import struct

def scale_number(unscaled, to_min, to_max, from_min=0, from_max=4294967295):
    # Scale the number to the new range
    return (to_max - to_min) * (unscaled - from_min) / (from_max - from_min) + to_min

def check_for_repeats(time_intervals):
    # Check if there are any repeated time intervals
    seen = set()
    for interval in time_intervals:
        if interval in seen:
            return True
        seen.add(interval)
    return False

def generate_time_intervals(input_file_path, output_file_name, min_interval, max_interval):
    time_intervals = []
    with open(input_file_path, 'r') as in_file:
        for line in in_file:
            unscaled_num = int(line.strip())
            interval = scale_number(unscaled_num, min_interval, max_interval)
            time_intervals.append(interval)

    if check_for_repeats(time_intervals):
        print("Repeated time intervals were found.")
    else:
        print("No repeated time intervals were found.")

    # Write the scaled time intervals to the output file
    with open(output_file_name, 'w') as out_file:
        for interval in time_intervals:
            out_file.write(f"{interval}\n")
    print(f"Time intervals have been generated and saved to {output_file_name}")

# Ask user for input and output details
min_interval = float(input("Enter the minimum time interval in seconds: "))
max_interval = float(input("Enter the maximum time interval in seconds: "))
output_file_name = input("Enter the desired output file name (with extension, e.g., 'output_intervals.txt'): ")

# Validate the time interval range
if min_interval < 0 or max_interval <= min_interval:
    print("Invalid range. The minimum interval must be non-negative and less than the maximum interval.")
else:
    # Set the path to the file with the integer values
    integer_input_file_path = 'tq-qrng-4bytevalues.txt'

    # Validate the output file name
    if not output_file_name.strip():
        print("Invalid file name. Please provide a valid file name.")
    else:
        # Generate and save the time intervals to the output file
        generate_time_intervals(integer_input_file_path, output_file_name, min_interval, max_interval)
