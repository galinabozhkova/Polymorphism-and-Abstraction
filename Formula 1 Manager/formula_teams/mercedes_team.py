from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    PETRONAS = {1: 1000000, 3: 500000}
    TEAMVIEWER = {5: 100000, 7: 50000}
    EXP_PER_RACE = 200000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = - self.EXP_PER_RACE

        for key, value in self.PETRONAS.items():
            if key == race_pos:
                revenue += self.PETRONAS[key]

        for key, value in self.TEAMVIEWER.items():
            if key >= race_pos:
                revenue += self.TEAMVIEWER[key]
                break

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

