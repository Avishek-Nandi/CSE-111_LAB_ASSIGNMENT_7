# Solution to Task 7

class Football:

    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' + self.__team


class Player(Football):

    def __init__(self, team_name, name, role, goals, matches):
        super(Player, self).__init__(team_name, name, role)
        self.ratio = 0
        self.goals = goals
        self.matches = matches

    def calculate_ratio(self):
        self.ratio = self.goals/self.matches

    def print_details(self):
        print(f'{self.get_name_team()}')
        print(f"Role: {self.role}")
        print(f'Total Goal: {self.goals}, Total Played:{self.matches}')
        print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earning: {(self.goals * 1000) + (self.matches * 10)}K")


class Manager(Football):

    def __init__(self, team_name, name, role, win):
        super(Manager, self).__init__(team_name, name, role)
        self.win = win

    def print_details(self):
        print(f'{self.get_name_team()}')
        print(f"Role: {self.role}")
        print(f"Total Win: {self.win}")
        print(f"Match Earning: {(self.win * 1000)}K")


if __name__ == "__main__":
    player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
    player_one.calculate_ratio()
    player_one.print_details()
    print('------------------------------------------')
    manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
    manager_one.print_details()
