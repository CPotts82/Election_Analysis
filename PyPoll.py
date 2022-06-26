# Add dependencies
import csv
import os

#Assign variable for file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
#Creata a filename variable to direct or indirect path where file is kept
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: Read and analyze the data
#REad the file object with the reader function
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)

#Find total number of votes by adding them up
#Use loop, or something of the sort to figure out total number of candidates
#After figuring out how many candidates - use another loop to add up each individuals total votes
#Using the total number of votes cast and each candidates total votes, calculate percentage for each candidate
#Candidate with the highest percentage of votes is winner - use if statment or loop?