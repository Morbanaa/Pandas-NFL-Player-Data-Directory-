# Teddy Rodd

import pandas as pd
from other import *

# Creates data frame and calls main loop with menu() The df is formated before being sent over
def main():
    df = pd.read_csv("bearsRoster2026.csv")

    df.columns = df.columns.str.title()

    if "Player Name" in df.columns:
        df["Player Name"] = df["Player Name"].str.title()

    if "Position" in df.columns:
            df["Position"] = df["Position"].str.upper()
    

    menu(df)

# Allows player to choose what type of filter they want to use and then calls the function             
def menu(df):
    while True:
        print("\nWould you like to:")
        print("(1) Filter by position")
        print("(2) Filter by age")
        print("(3) Filter by weight class")
        print("(4) Show full roster")
        print("(5) Sort players by last name")
        print("(6) Exit")
        choice = input("Choose (1-6): ")  

        if choice == "1":
            filter_position(df)
        elif choice == "2":
            filter_age(df)
        elif choice == "3":
            filter_weight(df)
        elif choice == "4":
            show_full_roster(df)
        elif choice == "5":
            filter_last_name(df)
        elif choice == "6":
            break
        else:
            print("Not a valid input!")

# Program Entry point
if __name__ == "__main__":
    main()
    print("Have a good day!\n")
