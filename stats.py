
import json

MainStatPlayers= {}
totalplayer = []
MainStatPlayers = {'puntret_tds': 0, 'Player_name': 'Tom Brady', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 286, 'rushing_tds': 0, 'fumbles': 7, 'passing_yds': 4551, 'receiving_yds': 0, 'HalfPPR': 286.0, 'passing_2pt': 2, 'rushing_yds': 28, 'receiving_2pt': 0, 'Player_id': '00-0019596', 'receptions': 0, 'passing_tds': 32, 'passing_ints': 8}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers = {'puntret_tds': 0, 'Player_name': 'Drew Brees', 'receiving_tds': 0, 'Player_pos': 'QB', 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 252, 'rushing_tds': 2, 'fumbles': 5, 'passing_yds': 4338, 'receiving_yds': 0, 'HalfPPR': 252.0, 'passing_2pt': 0, 'rushing_yds': 12, 'receiving_2pt': 0, 'Player_id': '00-0020531', 'receptions': 0, 'passing_tds': 23, 'passing_ints': 8}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Larry Fitzgerald', 'receiving_tds': 6, 'Player_pos': "WR", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 260, 'rushing_tds': 0, 'fumbles': 1, 'passing_yds': 21, 'receiving_yds': 1156, 'HalfPPR': 205.5, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 1, 'Player_id': '00-0022921', 'receptions': 109, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Ben Roethlisberger', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 256, 'rushing_tds': 0, 'fumbles': 3, 'passing_yds': 4259, 'receiving_yds': 0, 'HalfPPR': 256.0, 'passing_2pt': 2, 'rushing_yds': 47, 'receiving_2pt': 0, 'Player_id': '00-0022924', 'receptions': 0, 'passing_tds': 28, 'passing_ints': 14}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Philip Rivers', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 255, 'rushing_tds': 0, 'fumbles': 8, 'passing_yds': 4515, 'receiving_yds': 0, 'HalfPPR': 255.0, 'passing_2pt': 0, 'rushing_yds': -2, 'receiving_2pt': 0, 'Player_id': '00-0022942', 'receptions': 0, 'passing_tds': 28, 'passing_ints': 10}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Benjamin Watson', 'receiving_tds': 4, 'Player_pos': "TE", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 135, 'rushing_tds': 0, 'fumbles': 1, 'passing_yds': 0, 'receiving_yds': 522, 'HalfPPR': 104.5, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 0, 'Player_id': '00-0022943', 'receptions': 61, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Alex Smith', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 292, 'rushing_tds': 1, 'fumbles': 2, 'passing_yds': 4042, 'receiving_yds': 0, 'HalfPPR': 292.0, 'passing_2pt': 0, 'rushing_yds': 355, 'receiving_2pt': 0, 'Player_id': '00-0023436', 'receptions': 0, 'passing_tds': 26, 'passing_ints': 5}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Aaron Rodgers', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 129, 'rushing_tds': 0, 'fumbles': 1, 'passing_yds': 1675, 'receiving_yds': 0, 'HalfPPR': 129.0, 'passing_2pt': 0, 'rushing_yds': 126, 'receiving_2pt': 0, 'Player_id': '00-0023459', 'receptions': 0, 'passing_tds': 16, 'passing_ints': 6}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Frank Gore', 'receiving_tds': 1, 'Player_pos': "RB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 167, 'rushing_tds': 3, 'fumbles': 3, 'passing_yds': 0, 'receiving_yds': 245, 'HalfPPR': 152.5, 'passing_2pt': 0, 'rushing_yds': 961, 'receiving_2pt': 0, 'Player_id': '00-0023500', 'receptions': 29, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Darren Sproles', 'receiving_tds': 0, 'Player_pos': "RB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 18, 'rushing_tds': 0, 'fumbles': 1, 'passing_yds': 0, 'receiving_yds': 73, 'HalfPPR': 14.5, 'passing_2pt': 0, 'rushing_yds': 61, 'receiving_2pt': 0, 'Player_id': '00-0023564', 'receptions': 7, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Matt Cassel', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 2, 'rushing_tds': 0, 'fumbles': 2, 'passing_yds': 162, 'receiving_yds': 0, 'HalfPPR': 2.0, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 0, 'Player_id': '00-0023662', 'receptions': 0, 'passing_tds': 1, 'passing_ints': 2}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Ryan Fitzpatrick', 'receiving_tds': 0, 'Player_pos': "QB", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 73, 'rushing_tds': 0, 'fumbles': 0, 'passing_yds': 1103, 'receiving_yds': 0, 'HalfPPR': 73.0, 'passing_2pt': 0, 'rushing_yds': 76, 'receiving_2pt': 0, 'Player_id': '00-0023682', 'receptions': 0, 'passing_tds': 7, 'passing_ints': 3}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Vernon Davis', 'receiving_tds': 3, 'Player_pos': "TE", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 121, 'rushing_tds': 0, 'fumbles': 2, 'passing_yds': 0, 'receiving_yds': 648, 'HalfPPR': 99.5, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 0, 'Player_id': '00-0024221', 'receptions': 43, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Marcedes Lewis', 'receiving_tds': 5, 'Player_pos': "TE", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 87, 'rushing_tds': 0, 'fumbles': 0, 'passing_yds': 0, 'receiving_yds': 318, 'HalfPPR': 75.0, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 1, 'Player_id': '00-0024243', 'receptions': 24, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Brandon Marshall', 'receiving_tds': 0, 'Player_pos': "WR", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 33, 'rushing_tds': 0, 'fumbles': 0, 'passing_yds': 0, 'receiving_yds': 154, 'HalfPPR': 24.0, 'passing_2pt': 0, 'rushing_yds': 0, 'receiving_2pt': 0, 'Player_id': '00-0024334', 'receptions': 18, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())
MainStatPlayers ={'puntret_tds': 0, 'Player_name': 'Delanie Walker', 'receiving_tds': 3, 'Player_pos': "TE", 'rushing_2pt': 0, 'kickret_tds': 0, 'PPR': 173, 'rushing_tds': 1, 'fumbles': 2, 'passing_yds': 0, 'receiving_yds': 807, 'HalfPPR': 136.0, 'passing_2pt': 0, 'rushing_yds': -2, 'receiving_2pt': 0, 'Player_id': '00-0024389', 'receptions': 74, 'passing_tds': 0, 'passing_ints': 0}
totalplayer.append(MainStatPlayers.copy())




#load dic into json file
'''r = json.dumps(totalplayer)
fp = open('test.json', 'a')

# write to json file
fp.write(r)

# close the connection
fp.close()'''