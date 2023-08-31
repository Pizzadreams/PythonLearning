import pandas as pd

# Load the pizza data from the Excel file
data = pd.read_excel('pizza_data.xlsx')

# Sort by Pizza Size in ascending order
sorted_by_size = data.sort_values(by='Pizza Size')

# Sort by Price by Slice in descending order
sorted_by_price_slice = data.sort_values(by='Price by Slice', ascending=False)

# Sort by Place Name and then by Customer in ascending order
sorted_by_place_and_customer = data.sort_values(by=['Place Name', 'Customer'])

# Display the sorted dataframes
print(f"Sorted by Pizza Size:\n{sorted_by_size}")

print(f"\nSorted by Price by Slice:\n{sorted_by_price_slice}")

print(f"\nSorted by Place Name and Customer:\n{sorted_by_place_and_customer}")