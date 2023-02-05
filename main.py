from prettytable import PrettyTable
from datetime import datetime
from tabulate import tabulate
import requests
import argparse
import json
import sys

f = open('data.json')
data = json.load(f)

def main():
    if len(sys.argv) <= 1:
        print('\n%s -h for help.' % (sys.argv[0]))
        exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--team",
                        dest="team",
                        help="Print statistics for the mentioned team",
                        action='store')


    args = parser.parse_args()
    team = args.team

    myTable = PrettyTable(["Fecha", "Equipo", "Condicion", "Goles_Anotados", "Rival", "Goles_Recibidos", "Poseción", "Corners", "Amarillas", "Rojas", "Faltas", "Tiros"])

    for x in range(len(data)):
        if data[x]["Nombre"] == team:
            myTable.add_row([data[x]["Fecha"], data[x]["Nombre"], data[x]["Condicion"], data[x]["Goles_Anotados"], data[x]["Rival"], data[x]["Goles_Recibidos"], data[x]["Poseción"], data[x]["Corners"], data[x]["Amarillas"], data[x]["Rojas"], data[x]["Faltas"], data[x]["Tiros"]])

    print(myTable)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt Detected.")
        print("Exiting...")
        exit(0)
