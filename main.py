
import nfldb
import psycopg2
import numpy as np
from bs4 import BeautifulSoup
from urllib import urlopen
import operator

import json
def sortplayers(totalplayer):
    totalplayer[:] = [d for d in totalplayer if d.get('CV') != 0]
    totalplayer[:] = [d for d in totalplayer if d.get('pprADP') > 0]
    totalplayer[:] = [d for d in totalplayer if d.get('TotalPointsppr') > 0]

    totalplayer.sort(key=operator.itemgetter('CV'))
    count = 0
    for x in totalplayer:

        totalplayer[count]['RankCV'] = count + 1
        count += 1

    totalplayer.sort(key=operator.itemgetter('TotalPointsppr'), reverse= True)
    count = 0
    for x in totalplayer:

        totalplayer[count]['Rankppr'] = count + 1

        try:
            totalplayer[count]['OverallRank'] = int(totalplayer[count]['RankCV'])*.4 + int(totalplayer[count]['ExpertRank'])*.6
            totalplayer[count]['OverallRank'] = round(totalplayer[count]['OverallRank'],2)
            totalplayer[count]['CombinedVsADP'] = float(totalplayer[count]['pprADP']) -  float(totalplayer[count]['OverallRank'])

        except ValueError:
            count += 1
            continue
        count += 1



    totalplayer.sort(key=operator.itemgetter('OverallRank'))



def getplayers(MainStatPlayers, totalplayer):
    for p in q.as_aggregate():
        if str(p.player.position) in ['QB', 'RB', 'WR', 'TE']:
            MainStatPlayers["Player_id"] = p.player_id
            MainStatPlayers["Player_name"] = p.player.full_name
            MainStatPlayers["Player_pos"] = str(p.player.position)
            MainStatPlayers["Player_Team"] = p.player.team

            main_stats( p.player.full_name, MainStatPlayers, PPR_ADP, HPPR_ADP)
            totalplayer.append(MainStatPlayers.copy())
            MainStatPlayers.fromkeys(MainStatPlayers, '0')





def HPPR_ADPscrape():
    nfl = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-cheatsheets.php'
    html = urlopen(nfl)
    soup = BeautifulSoup(html.read(), "lxml")
    table = soup.find('table', id="rank-data")

    HADPppr = []
    for row in table.find_all("tr")[3:]:  # skipping header row
        cells = row.find_all("td")
        try:
            dict = {"H_ExpertRank": cells[0].text, "Player_name": cells[2].find('a').contents[0].text,
                    "H_ADP": cells[9].text, "BYE": cells[4].text}
        except IndexError:
            continue
        HADPppr.append(dict)
        dict.fromkeys(MainStatPlayers, '0')

    return HADPppr


def PPR_ADPscrape():
    nfl = 'https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php'
    html = urlopen(nfl)
    soup = BeautifulSoup(html.read(), "lxml")
    table = soup.find('table', id="rank-data")

    ADPppr = []
    for row in table.find_all("tr")[3:]:
        cells = row.find_all("td")

        try:
            dict = {"ExpertRank": cells[0].text, 'Player_name': cells[2].find('a').contents[0].text,
                    "ADP": cells[9].text, "BYE": cells[4].text}
        except IndexError:
            continue

        ADPppr.append(dict)
        dict.fromkeys(dict, 0)

    ADPppr[:] = [d for d in ADPppr if d.get('ADP') > 0]
    return ADPppr


def main_stats( fullname, MainStatPlayers, PPR_ADP, HPPR_ADP):

    qry = '''SELECT
    (sum(passing_Tds) * 4       +                                               
    SUM(passing_yds) / 25       +                                              
    SUM(receiving_rec)          +                                             
    SUM(passing_int) * -1       +                                          
    SUM(rushing_tds) * 6        +                                           
    SUM(receiving_yds) / 10     +                                           
    SUM(receiving_tds) * 6      +                                          
    SUM(puntret_tds) * 6        +                                         
    SUM(fumbles_lost) * -1      +                                        
    (SUM(passing_twoptm) + SUM(rushing_twoptm) + SUM(receiving_twoptm)) * 2+
    SUM(fumbles_rec_tds) * 6    +                                       
    SUM(defense_sk)             +                                      
    SUM(defense_int) * 2        +                                    
    SUM(defense_frec) * 2       +                                    
    SUM(defense_int_tds) * 6    +                                   
    SUM(defense_frec_tds) * 6   +                                  
    SUM(defense_puntblk) * 6    +                                
    SUM(defense_safe) * 2       +      
                        
    (SUM(defense_fgblk) + SUM(punting_blk)) * 2 )                 as ppr


    FROM play_player
    JOIN game   USING (gsis_id)
    JOIN player USING (player_id)
    WHERE season_year = 2017
      AND season_type = 'Regular'
      AND full_name =%s
      
    GROUP BY game, week
    LIMIT 18  
        '''


    cursor.execute(qry, [fullname])
    result = cursor.fetchall()
    result = map(list, result)

    MainStatPlayers["TotalPointsppr"] = sum([pair[0] for pair in result])


    ppradp = filter(lambda person: person['Player_name'] == fullname, PPR_ADP)

    Hppradp = filter(lambda person: person['Player_name'] == fullname, HPPR_ADP)

    if (len(ppradp) == 0):
        print(MainStatPlayers["Player_name"])
    if (len(ppradp) > 0):
        try:
            MainStatPlayers["pprADP"] = float(ppradp[0]["ADP"])
        except ValueError:
            MainStatPlayers["pprADP"] = 0

        MainStatPlayers["ExpertRank"] = ppradp[0]["ExpertRank"]
        MainStatPlayers["BYE"] = ppradp[0]["BYE"]


    if len(result) != 16:
        for x in range(len(result),16):
            yo = []
            yo.append(0)
            result.append(yo)


    if np.mean(result) > 0:
        cv = lambda x: np.std(x) / np.average(x)
        var = np.apply_along_axis(cv, axis=0, arr=result)
        MainStatPlayers["CV"] = var[0]
        MainStatPlayers["AVG"] = np.mean(result)


MainStatPlayers = {
    'ExpertRank': '0',
    'BYE': '0',
    'Player_name': '0',
    'Player_Team':'0',
    'Player_pos': '0',
    'TotalPointsppr':'0',
    'pprADP': '0',
    'Player_id': '0',
    'AVG': '0',
    'CV': '0'}
totalplayer = []

if __name__ == "__main__":
    db = nfldb.connect()
    conn = psycopg2.connect("dbname=nfldb host=localhost port=5432 user=nfldb password=stefan")
    cursor = conn.cursor()
    q = nfldb.Query(db)

    q.game(season_year=2017, season_type='Regular')
    count = 0
    PPR_ADP = PPR_ADPscrape()
    HPPR_ADP = HPPR_ADPscrape()

    getplayers(MainStatPlayers,totalplayer)

    sortplayers(totalplayer)
    r = json.dumps(totalplayer)
    fp = open('data.json', 'a')
    fp.write(r)
    fp.close()


