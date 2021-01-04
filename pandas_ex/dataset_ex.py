import requests
import pandas as pd

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

#response = requests.get(download_url)
#response.raise_for_status() #Check if the request is succesfull
#
#with open(target_csv_path,'wb') as file_to_write:
#    file_to_write.write(response.content)

nba = pd.read_csv("nba_all_elo.csv")
pd.set_option("display.max.columns",None)
pd.set_option("display.precision",2)

print(nba.head(),end = "\n\n")
#print(nba.info())
#print(nba["team_id"].value_counts())
#print(nba["fran_id"].value_counts())

print(nba.loc[nba["fran_id"] == "Lakers","team_id"].value_counts())

print("MNL played date ->")
print(nba.loc[nba["team_id"]=="MNL","date_game"].agg(("min","max")))

print(f"BOS Scored {nba.loc[nba['team_id']=='BOS','pts'].sum()}")

shape = pd.Series({"0": "cube", "1": "sphere"})
ball_type = pd.Series({"0": "rubik cube", "1": "ball","2":"tennis"})

ball_test = pd.DataFrame({
    "ball" : ball_type,
    "shape" : shape
    })

print(ball_test)

toys = pd.DataFrame([
    {"name": "ball", "shape": "sphere"},
    {"name": "Rubik's cube", "shape": "cube"}
])

print(nba[(nba["_iscopy"] == 0) (nba["pts"] > 100) &                (nba["opp_pts"] > 100) &                    (nba["team_id"] == "BLB")
                    ]
                    )
