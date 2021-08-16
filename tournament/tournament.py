class TeamEntry:
    def __init__(self):
        self.wins = self.losses = self.draws = 0

    def get_scores(self):   # return tuple: (MP, W, D, L, P)
        return (self.wins + self.losses + self.draws,
                self.wins, self.draws, self.losses,
                3 * self.wins + 1 * self.draws)


class Tournament:
    def __init__(self):
        self.teams = {}
    
    def add_result(self, ta, tb, result):
        if ta not in self.teams:
            self.teams[ta] = TeamEntry()
        if tb not in self.teams:
            self.teams[tb] = TeamEntry()

        if result == 'draw':
            self.teams[ta].draws += 1
            self.teams[tb].draws += 1
            return
        
        if result == 'loss':
            ta, tb = tb, ta     # swap places and count as a win
        
        self.teams[ta].wins += 1
        self.teams[tb].losses += 1

    def all_results(self):      # return dict: {teamname : (MP, W, D, L, P)}
        return {team : self.teams[team].get_scores() for team in self.teams}


def tally(rows):
    tourn = Tournament()
    for row in rows:
        ta, tb, res = row.split(';')
        tourn.add_result(ta, tb, res)
    results = tourn.all_results()
    table_rows = [('Team', ('MP', 'W', 'D', 'L', 'P'))]
    table_rows += [ (t, sc) for t, sc in 
            sorted(results.items(), key=lambda x: x[1][4], reverse=True)]
    
    disp_results = []
    for row in table_rows:
        row_head = row[0]
        row_data = row[1]
        disp_row = row_head.ljust(32)[:30]
        for item in row_data:
            disp_row += ' | ' + str(item).rjust(2)
        disp_results.append(disp_row)

    return disp_results

            