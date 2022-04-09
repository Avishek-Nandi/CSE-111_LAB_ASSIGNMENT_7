# Solution to Task 3

class Tournament:
    def __init__(self, name='Default'):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Cricket_Tournament(Tournament):

    def __init__(self, name="Default", teams=0, gametype="No type"):
        super(Cricket_Tournament,self).__init__(name)
        self.teams = teams
        self.gametype = gametype

    def detail(self):
        return f"Cricket Tournament Name: {self.get_name()}\nNumber of teams: {self.teams}\nType: {self.gametype}"


class Tennis_Tournament(Tournament):

    def __init__(self, name="Default", teams=0):
        super().__init__(name)
        self.teams = teams

    def detail(self):
        return f"Tennis Tournament Name: {self.get_name()}\nNumber of teams: {self.teams}"


if __name__ == "__main__":

    ct1 = Cricket_Tournament()
    print("-----------------------")
    ct2 = Cricket_Tournament("IPL", 10, "t20")
    print(ct2.detail())
    print("-----------------------")
    tt = Tennis_Tournament("Roland Garros", 128)
    print(tt.detail())


