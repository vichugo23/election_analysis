# election_analysis



import os
import csv
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("..","analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("election_results.csv")
# Open the election results and read the file.
with open("/Users/victoralvarado/Desktop/class folder/election_analysis/Resources/Resources/election_results.csv") as election_data:

    # Print the file object.
     print(election_data)

     # Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open("/Users/victoralvarado/Desktop/class folder/election_analysis/Resources/analysis/election_analysis.txt", "w") as outfile:
# Write some data to the file.
    outfile.write("Hello World")

# Close the file
outfile.close()


#The data we need to retrieve
#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. the percentage of votes each candidate won.
#4. the total number of votes each candidate won.
#5. the winner of election based on popular vote.
