# =======================================================================
# Project: Titanic Dataset
# Description: Combining and structuring data with NumPy.
# The project uses Python's NumPy library to merge and structure two datasets into one.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====

# The main.py file contains code that:
# - converts two CSV datasets into Python lists and subsequently into NumPy arrays.
# - merges the two datasets (NumPy arrays) into one.
# - converts the merged dataset (NymPy array) back into one combined CSV file.
# =======================================================================

import csv
import numpy as np

### Converts titanic1.csv and titanic2.csv to CSV reader objects, then to Py lists, and finally to NumPy arrays:

with open("titanic1.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  # Gets the header row (1st row) of CSV object:
  headers = next(data)
  # Gets all rows of CSV object and converts to Python list:
  data_list = list(data)
  # Assign the Python list variable with the CSV data to a NumPy array:
  titanic_data1 = np.array(data_list)

with open("titanic2.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  # Gets the header row (1st row) of CSV object:
  headers = next(data)
  # Gets all rows of CSV object and converts to Python list:
  data_list = list(data)
  # Assign the Python list variable with the CSV data to a NumPy array:
  titanic_data2 = np.array(data_list)

### Merges the two datasets:

combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

# Dimensions of combined dataset:
print(combined_data.ndim)
# Output: 2 - i.e. a 2D array.

# Shape of combined dataset:
print(combined_data.shape)
# Output: (887, 8) - i.e. a 2D array consisting of 887 1D arrays each with 8 elements.

### Turns combined NumPy array dataset back into into one combined CSV file:

# Converts combined NumPy array into a regular Py list (a list of lists):
listify = combined_data.tolist(
)  # one list for each row of the combined datasets.
# Loop turns the list of lists into a string:
titanic_lists_to_string = []  # stores data converted to string.
for titanic_lists in listify:
  # Turns each list into a string:
  # - comma indicates how each string is currently separated.
  titanic_string = (",").join(titanic_lists)
  # Adds and stores each converted list of the NumPy array:
  titanic_lists_to_string.append(titanic_string)

# Converts the entire NumPy array into a string:
# - delimiter "\n" puts each row of data on one line.
complete_titanic = ("\n").join(titanic_lists_to_string)

# Writes combined string to a new CSV file:
with open("titanic.csv", "w") as file:
  # Selects headers and data columns to add to CSV file:
  # - \n indicates the rest of the data must start on new line.
  file.write(
      'Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n'
  )
  file.write(complete_titanic)
