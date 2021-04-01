# Election_Analysis
## Project Overview
The Colorado Board of Election asked for an election audit to be performed to find the following information for a congressional election:
1. Calculate the total number of votes
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Software: Visual Studio Code (1.54.3), Python (3.9.2)
- Data source: election_results.csv

## Summary of results
The following candidates were up for election: Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane. The follwing table shows a summary of the election results:

| Candidate   | Votes       | Perecentage |
| ----------- | ----------- | ----------|
| Stockham    | 85,213      | 23.0%     |
| Degette     | 272,892     | 73.8%     |
| Doane       | 11,606      | 3.1%      |
         

As is presented in the above table, the winner of the electoral race was Diana DeGette with 272,892 votes which is 73.8% of the total. All of this information was written to a text file election_analysis.txt in the 'Analysis' folder.

## Challenge Overview
The purpose of the challenge was to add the following data to the analysis:
- The voter turnout for each county
- The percentage of couty votes to the total
- The county with the highest turnout

## Summary of Results

The following table summarizes the results from the challenge.

| County   | Votes       | Perecentage |
| ----------- | ----------- | ----------|
| Jefferson   | 38,855      | 10.5%     |
| Denver      | 306,055     | 82.8%     |
| Arapahoe    | 24,801      | 6.7%      |
        

Denver county had, by far the largest voting turnout, ringing in over 80% of the total votes. The python script also wrote this information to the election_analysis.txt file.

## ELection-Audit Summary
This script can be edited to accept election results of much larger sample sizes, as long as a CSV file is provided with a county, candidate, and vote. Additionally this script could be easily modified to add informations for states in a nationwide election, the groundwork has already been laid with the for loops and conditional statements. It would not be hard to sum up total votes for each state, or compare candiate outcomes in each state.