# Checks data frame for players that match the position given by the player
def filter_position(df):
    while True:
        choice = input("\nFilter by (QB,RB,WR,TE,OT,G,C,ED,DL,LB,CB,K,P,LS): ").upper()

        options = ["QB","RB","WR","TE","OT","G","C","ED","DL","LB","CB","K","P","LS"]
        if choice in options:
            break
        else:
            print("Not a valid input...")

    print(f"Filter by {choice}:")
    print(df[df["Position"] == choice])

# Filters data frame for all players within the min to max age range given by the user
def filter_age(df):
    try:
        while True:
            min = int(input("\nEnter min age to filter by: "))
            if min <= 0:
                print("Must enter a number greater than zero...")
                continue
            else:
                break

        while True:
            max = int(input("Enter max age to filter by: "))
            if max < min:
                print(f"The max age must be greater than {min}")
            else:
                break

        by_age = df[(df["Age"] >= min) & (df["Age"] <= max)]

        if by_age.empty:
            print("\nNo result found!")
        else:
            print(f"\nFilter by age {min}-{max}:")
            print(by_age)
        
    except ValueError:
        print("Must enter a whole number greater than zero...")

# Filters data frame for all players within the min to max weight range given by the user
def filter_weight(df):
    
    try:
        while True:
            min = int(input("\nEnter min weight to filter by: "))
            if min <= 0:
                print("Must enter a number greater than zero...")
                continue
            else:
                break

        while True:
            max = int(input("Enter max weight to filter by: "))
            if max < min:
                print(f"The max weight must be greater than {min}")
            else:
                break

        by_weight = df[(df["Weight"] >= min) & (df["Weight"] <= max)]

        if by_weight.empty:
            print("\nNo result found!")
        else:
            print(f"\nFilter by weight {min}-{max}:")
            print(by_weight)
    
    except ValueError:
        print("Must enter a whole number greater than zero...")

# This one just prints out the whole data frame... pretty simple...
def show_full_roster(df):
    print("\nFull Roster:")
    print(df)

# Filters dataframe based on last name user enters
def filter_last_name(df):
    while True:
        last_name = input("\nEnter last name to filter by: ").capitalize()
        if last_name != "":
            break
        
    # Checks for the last name at the end of the string
    filter_name = df[df["Player Name"].str.endswith(last_name, na=False)
]
    if filter_name.empty:
        print("\nNo result found...")
    else:
        print(f"\nFilter by {last_name}:")
        print(filter_name)

