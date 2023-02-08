from prettytable import PrettyTable
from datetime import datetime
from tabulate import tabulate
import requests
import argparse
import json
import sys

f = open('data.json')
data = json.load(f)

def list_teams():
    teams = [
    'Arsenal',
    'Aston Villa',
    'Bournemouth',
    'Brentford',
    'Brighton & Hove Albion',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Fulham',
    'Leeds United',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Nottingham Forest',
    'Southampton',
    'Tottenham Hotspur',
    'West Ham United',
    'Wolverhampton Wanderers'
    ]
    myTable = PrettyTable(["Teams",])

    for x in range(len(teams)):
        myTable.add_row([teams[x]])
    print(myTable)
    exit(0)

def main():
    if len(sys.argv) <= 1:
        print('statspremierleague\n%s -h for help.' % (sys.argv[0]))
        exit(0)
    elif len(sys.argv) > 3:
        print('statspremierleague\n%s Error: only one argument allowed at a time' % (sys.argv[0]))
        exit(0)
        
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--team",
                        dest="team",
                        help="Print statistics for the mentioned team",
                        action='store')
    parser.add_argument("-l", "--listeams",
                        dest="list",
                        help="List of teams available for consultation",
                        action='store_true')                        

    args = parser.parse_args()
    team = args.team
    listeams = args.list

    if listeams == True:
        list_teams()

    myTable = PrettyTable(["Date", "Team", "Condition", "Goals scored", "Rival", "Goals conceded", "Possession", "Corners", "Yellow card", "Red cards", "Faults", "Shots"])

    for x in range(len(data)):
        if data[x]["Nombre"] == team:
            date = data[x]["Fecha"]
            team = data[x]["Nombre"]
            condition = data[x]["Condicion"]
            scored = data[x]["Goles_Anotados"]
            rival = data[x]["Rival"]
            conceded = data[x]["Goles_Recibidos"]
            possession = data[x]["Poseción"]
            corners = data[x]["Corners"]
            yellow = data[x]["Amarillas"]
            red = data[x]["Rojas"]
            faults = data[x]["Faltas"]
            shots = data[x]["Tiros"]
            myTable.add_row([date, team, condition, scored, rival, conceded, possession, corners, yellow, red, faults, shots])

    print(myTable)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt Detected.")
        print("Exiting...")
        exit(0)
