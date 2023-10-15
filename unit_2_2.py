class Player:
  def print(self):
    print("The player is playing cricket.")

class Batsmen(Player):
  def play(self):
    print("The batsmen is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is Bowling.")

batsmen = Batsmen()
bowler = Bowler()
  