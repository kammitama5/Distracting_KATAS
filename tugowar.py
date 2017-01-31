def tug_o_war(teams):
    # Which one?
    # return "Team 1 wins!"
    # return "Team 2 wins!"
    team1 = teams[0]
    team2 = teams[1]
    
    sumteam1 =  sum(team1)
    sumteam2 = sum(team2)
    
    anchor1 = team1[0]
    anchor2 = team2[-1]

    if (sumteam1 > sumteam2):
      return "Team 1 wins!"
    elif (sumteam2 > sumteam1):
     return "Team 2 wins!"
    elif ((sumteam1 == sumteam2) and (anchor1 > anchor2)):
      return "Team 1 wins!"
    elif ((sumteam1 == sumteam2) and (anchor2 > anchor1)):
      return "Team 2 wins!"
    else:
      return "It's a tie!"
	  