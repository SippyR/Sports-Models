import nbastatpy as nba
import openpyxl as px
import pandas as pd

def get_data():
    playerData = pd.read_excel('NBAData.xlsx', sheet_name='Player Per Game Table')
    teamData = pd.read_excel('NBAData.xlsx', sheet_name='Team Per Game Stats Table')
    teamAdvData = pd.read_excel('NBAData.xlsx', sheet_name='Team Advanced Stats Table')
    teamAdvData = teamAdvData.drop(index=0)
    teamAdvData.columns = teamAdvData.iloc[0]
    teamAdvData = teamAdvData[1:]
    teamAdvData = teamAdvData.reset_index(drop=True)
    return playerData, teamData, teamAdvData

def create_player_by_team(playerData):
    playerByTeam = playerData.groupby('Team').agg({'Player': lambda x: list(x)})
    return playerByTeam

def create_team_data(teamData, teamAdvData):
    teamData = teamData.merge(teamAdvData, on='Team')
    return teamData

def create_schedule_df():
    october_2025 = pd.read_excel('NBAData.xlsx', sheet_name='October Schedule Table')
    november_2025 = pd.read_excel('NBAData.xlsx', sheet_name='November Schedule Table')
    december_2025 = pd.read_excel('NBAData.xlsx', sheet_name='December Schedule Table')
    january_2026 = pd.read_excel('NBAData.xlsx', sheet_name='January Schedule Table')
    february_2026 = pd.read_excel('NBAData.xlsx', sheet_name='February Schedule Table')
    march_2026 = pd.read_excel('NBAData.xlsx', sheet_name='March Schedule Table')
    april_2026 = pd.read_excel('NBAData.xlsx', sheet_name='April Schedule Table')
    schedule_df = pd.concat([october_2025, november_2025, december_2025, january_2026, february_2026, march_2026, april_2026], ignore_index=True)
    schedule_df = schedule_df.drop_duplicates()
    return schedule_df

def create_model(playerData, teamData, teamAdvData, schedule_df):
    # Placeholder for model creation logic
    # This is where you would implement your machine learning model using the dataframes
    pass

def main():
    playerData, teamData, teamAdvData = get_data()
    print(playerData.head())
    print(teamData.head())
    print(teamAdvData.head())

    playerByTeam = create_player_by_team(playerData)
    print(playerByTeam.head())
    schedule_df = create_schedule_df()
    print(schedule_df.head())


if __name__ == "__main__":
    main()