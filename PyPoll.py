#Add our depenendencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")
# Using the with statement open the file as a text file.

   # Open the election results and read the file.
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

    # Print the header row.
        headers = next(file_reader)
        print(headers)

    # Print the file object.
        print(election_data)

    # Print each row in the CSV file.
        for row in file_reader:
            print(row)

# Close the file.
election_data.close()