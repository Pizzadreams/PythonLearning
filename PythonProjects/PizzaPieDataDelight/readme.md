# Pizza Data Generator using Faker and Pandas
This project aims to generate pizza-related data using the Faker library and organize it with the Pandas library for data manipulation and analysis.

## Purpose
The goal of this project is for me to gain a hands-on understanding of data analysis using the Pandas library in Python. By creating and manipulating pizza-related data, I can practice various Pandas operations such as DataFrame creation, sorting, filtering, and exporting data to Excel files. Add Unit Test code to ensure various functions of the code are functioning correctly.

## Features
- Generates random pizza place names using the Faker library.
- Includes pizza sizes, styles, sauces, toppings, prices, and customer names.
- Exports the generated data to an Excel file using the XlsxWriter library.
- *'pizza_data.xlsx' file will overwrite after every code execution
- Implement test suite with:
 - File Creation testing: Verifies whether an Excel file was created successfully.
 - Column Matching: It checks whether the columns in the loaded data from the Excel file match the columns in your original pizza data. This ensures that the data was saved correctly.
 - Data Existence: Check whether the loaded data is not empty
 

## Requirements
Make sure you have the following libraries installed:
- [Pandas](https://pandas.pydata.org/): A powerful data analysis and manipulation library.
- [Faker](https://faker.readthedocs.io/en/master/): A library for generating fake data.
- [XlsxWriter](https://xlsxwriter.readthedocs.io/): A library for creating Excel files.

You can install these libraries using the following command:
```bash
pip install pandas faker XlsxWriter openpyxl