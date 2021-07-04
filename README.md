# Election_Analysis
python analysis of voter data

##Overview

In this module I was tasked with aiding the Colorado election board in tabulating congressional votes. I was responsible for reporting the total number of votes cast, total votes for each candidate, the percentage of votes for each candidate, and the winner of the elction based on the popular vote. I used python to automate the election audit process and certify the winner of the election. 

In the challenge, the election commission requested some additional data to complete the audit. I expanded my report to include County results including; the County with the highest voter turnout, voter turnout for each County and the percentage of votes from each county out of the total count. 

##Election Audit Results 
* In total, 369,711 votes were cast in this congressional election. 

* ![County_Votes_Screengrab] (file:///Users/tylerlentini/Desktop/County_Votes_Screengrab.png)

* ![Largest_County](file:///Users/tylerlentini/Desktop/Screen%20Shot%202021-07-03%20at%208.12.48%20PM.png)

* ![Candidate_Stats](file:///Users/tylerlentini/Desktop/Candidate_votes.png)

* ![Election_Winner](file:///Users/tylerlentini/Desktop/Election_Winner.png)

##Election-Audit Summary 

This script is applicable for use in other elections. We know that one of the most frustrating facets of elections is waiting to hear the results. This script speeds up the process of tabulating results and can be modified for different scenarios. The data set is interchangeable and can be applied to an array of voter outcomes. 

My proposal is to modify the script for the ranked-choice voting format gaining popularity in numerous states. One modification would be additional conditional statements to loop through the data multiple times. Each time a candidate is eliminated the script would run again until a majority is reached. There would many modifications in this case but a second example would be to reallocate the votes from the previous round to the second choice candidates of the voters whose first choice candidate was elimanted in the previous round. The second step can be accomplished adding logical operators and conditional statements. Our current script provides a solid framework to build upon. 