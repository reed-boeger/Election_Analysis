voting_data= []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.insert(1,{"county": "jefferson", "registered_voters": 461149})
voting_data.pop(0)
#voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
#print(voting_data)
#for i in range(len(voting_data)):
  #  print(voting_data[i])
# for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
for county_dict in voting_data:

     print(county_dict['registered_voters'])
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")