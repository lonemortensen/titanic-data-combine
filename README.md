# Titanic Datasets: Combining Data
Combining datasets with Python's NumPy library.

## About
This project uses Python's NumPy library and the CSV module to merge and structure two Titanic datasets into one dataset in order to make the data easier to work with and analyze. 

## Project Background
The project was built as part of the coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

During this project, I practiced: 

- Combining two datasets in CSV format using the NumPy library. This included first converting the CSV files into Python lists and subsequently converting the Python lists into NumPy arrays. Finally, the two NumPy arrays were combined using the np.concatenate() function. 

- Printing the dimensions and shape of the combined NumPy array. 

- Converting the combined NumPy array dataset back into one combined CSV file, using the tolist() method to first turn the NumPy array back into a list of regular Python lists which subsequently were converted into a list of strings with the join() method. Finally, the entire NumPy array of strings was converted into a string and written to a new CSV file.  

## Built With 
- Python
- CSV module
- NumPy

## Launch
[See the project here:](https://replit.com/@lonemortensen/skillcrush-py-cl03-ls03-titanic-combine-data-numpy-final)

## Acknowledgements

**Skillcrush** - I coded the project's main.py file with support and guidance from Skillcrush. 