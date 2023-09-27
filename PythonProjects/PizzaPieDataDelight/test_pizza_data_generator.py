import unittest
import os
import pandas as pd
from pizza_data_generator import generate_pizza_data

class TestPizzaDataGeneration(unittest.TestCase):

    def test_generated_data_columns(self):
        # Verify that the generated data has the expected columns
        data = generate_pizza_data()
        expected_columns = ['Place Name', 'Pizza Size', 'Pizza Style', 'Pizza Sauce', 'Toppings', 'Price by Slice', 'Price by Size', 'Customer']
        self.assertEqual(list(data.columns), expected_columns)

    def test_generate_pizza_sizes(self):
        # Call the function to generate pizza data
        data = generate_pizza_data()
        
        # Extract the 'Pizza Size' column from the generated data
        pizza_sizes = data['Pizza Size'].unique()
        
        # Define a list of valid pizza sizes
        valid_sizes = ['sm', 'md', 'lg']
        
        # Check if all pizza sizes are in the list of valid sizes
        for size in pizza_sizes:
            self.assertIn(size, valid_sizes)

    def test_data_storage_to_excel(self):
        # Generate some sample data
        data = generate_pizza_data()

        excel_file = 'test_pizza_data.xlsx'

        # Check if the file already exists and delete it (for a clean test)
        if os.path.exists(excel_file):
            os.remove(excel_file)

        # Save sample data to an Excel file
        data.to_excel(excel_file, index=False)

        # Check if the file was created
        assert os.path.exists(excel_file)

        loaded_data = pd.read_excel(excel_file)

        # Verify that the loaded data has the same columns as the original data
        assert list(loaded_data.columns) == list(data.columns)
        assert not loaded_data.empty

if __name__ == '__main__':
    unittest.main()