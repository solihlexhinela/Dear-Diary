from rich.console import Console
from rich.panel import Panel

console = Console()
class Authentification:
  def __init__(self, username, pin, landing):
    self.username = username
    self.pin = pin
    self.landing = landing

  def __str__(self):
    return f"WELCOME BACK {self.username}"

  @classmethod
  def get(cls):
    username = input("Username: ")
    pin = int(input("Pin: "))
    return cls(username, pin)

 #validate username
  @property
  def username(self):
    return self._username
  @username.setter
  def username(self, username):
    if not username:
      raise ValueError("Enter username to proceed")
    self._username = username

  def pin(self):
    return self._pin
  def pin(self, pin):
    if pin not in ["123"]:
      raise ValueError("Invalid password")
    self._pin = pin

  #calander tracker for days journaled
  def landing(self):
    content = (
      "Streak: 🔥 0 Days\n" 
      "[1] Write today's Entry\n"
      "[2] Past entries\n"
      "[3] Exit"
    )

    panel = Panel(
      content,
      title = "Dear Diary"
    )
    console.print(panel)

def main():
  authentification = Authentification.get()
  print(authentification)

if __name__=="__main__":
  main()


"""

choose = int(input("Enter your choice to proceed: "))
if choose == 1:
  console.rule("NEW ENTRIES", characters="~")

"""






