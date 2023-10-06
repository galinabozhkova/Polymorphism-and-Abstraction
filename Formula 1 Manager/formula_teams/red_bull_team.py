from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    ORACLE = {1: 1500000, 2: 800000}
    HONDA = {8: 20000, 10: 10000}
    EXP_PER_RACE = 250000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = - self.EXP_PER_RACE

        for key, value in self.ORACLE.items():
            if key == race_pos:
                revenue += self.ORACLE[key]

        for key, value in self.HONDA.items():
            if key >= race_pos:
                revenue += self.HONDA[key]
                break

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
