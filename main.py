
print("Welcome to the Football Roster App")

roster = []
player = input("Who is your defender: ").title()
roster.append(player)
player = input("Who is your midfielder: ").title()
roster.append(player)
player = input("Who is your forward: ").title()
roster.append(player)
player = input("Who is your goalkeeper: ").title()
roster.append(player)
player = input("Who is your winger: ").title()
roster.append(player)

print("\n\tYour starting 5 for the upcoming football match")
print(f"\t\tDefender\t : {roster[0]}")
print(f"\t\tMidfielder\t : {roster[1]}")
print(f"\t\tForward\t\t : {roster[2]}")
print(f"\t\tGoalkeeper\t : {roster[3]}")
print(f"\t\tWinger\t\t : {roster[4]}")

injured = roster.pop(2)
print(f"\nForward {injured} is injured!")

rosterlen = len(roster)
print(f"\nYou have best {rosterlen} players")

newplayer = input(f"\nWhich player would you like instead {injured}? ").title()
roster.insert(2, newplayer)

print("\n\tYour starting 5 for the upcoming football match")
print(f"\t\tDefender\t : {roster[0]}")
print(f"\t\tMidfielder\t : {roster[1]}")
print(f"\t\tForward\t\t : {roster[2]}")
print(f"\t\tGoalkeeper\t : {roster[3]}")
print(f"\t\tWinger\t\t : {roster[4]}")

print(f"\nGood luck {roster[2]}, you will do great!")
rosterlen = len(roster)
print(f"\nYou have full {rosterlen} players")
