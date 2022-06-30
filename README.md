# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate received. 
5. Determine the winner of the election based on popular vote. 

The calculations, compiled lists and determinations taken into account to perform these tasks include all voting methods: mail-in-ballots, punch cards and direct recording electronic, (DRE counting machines).

## Resources
- Data Source: election_results.csv
- Software; Python 3.7.6, Visual Studio Code, 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of thet vote and 11,606 number of votes. 
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes. 

## Challenge Overview
The Colorado Board of Elections has requested not only the information regarding each candidate in this US Congressional Precinct Election but has also requested a Vote Count Report for the following counties in the election: Jefferson County, Arapahoe County and Denver County.  The Board has requested the following information:

1. Determine voter turnout per county.
2. Calculate percentage of votes from each county. 
3. Determine the county with the highest voter turnout.

As with the candidate analysis, the tasks in the above list will take in to account all three voting methods mentioned above. 

## Challenge Summary
The analysis of the election shows the following information regarding counties and then finally the winning candidate:
- There were 369,711 votes cast in this election.
- The counties in the election were:
  - Arapahoe County
  - Jefferson County
  - Denver County
- The results for each county were:
  - Arapahoe County contributed 6.7% of the vote count with 24,801 votes.
  - Jefferson County contributed 10.5% of the vote count with 38,855 votes.
  - Denver County contributed 82.8% of the vote count with 306,055 votes.
- The county with the highest voter turnout was Denver County.

- The candidates of this election were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham with 23.0% of the vote and 85,213 votes.
  - Diana Degette with 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane with 3.1% of the vote and 11,606 votes. 
- The winning candidate results:
  - Diana Degette with 73.8% of the vote and 272,892 votes.

### The Election results summary:

![election_analysis](https://user-images.githubusercontent.com/106348899/176748703-3d12c9d9-3eb3-4da0-bcf5-94ad0dc9a031.png)

### Procedure 
In order to find the number of votes for each county a for loop was created that iterated through the csv file.  Inside the for loop there were multiple decision statements that pulled out unique county names and placed them in a list, the loop also tracked the vote count per county. This was also done for the candidate data inside the same overall with loop. 
```# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        #print(candidate_name)
        
        # 3: Extract the county name from each row.
        county_name = row[1]
        #print(county_name)

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1 
```
In order to find the county with the largest vote turnout another nested loop was built.  The outside loop is a while loop and the inside loop a for loop that retrieved the vote count per county, calculate the percentage of votes per county and printed the summary. Inside this for loop was an if statement that determined the county with the largest turnout. (The analysis on the winning candidate was done the same way.)
```# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name} : {county_vote_percentage:.1f}% ({votes:,})\n")
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_votes) and (county_vote_percentage > winning_percentage):
            winning_county = county_name
            winning_votes = votes
           
    # 7: Print the county with the largest turnout to the terminal.
    county_win = (
        f"-------------------------\n"
        f"Largest County Turnout : {winning_county}\n"
        f"-------------------------\n")
    print(county_win)
```
## Statement Summary 
