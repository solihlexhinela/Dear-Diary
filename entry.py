import csv
from datetime import datetime

from rich.console import Console
from rich.panel import Panel

console = Console()
class Authentification:
  def __init__(self, username, pin):
    self.username = username
    self.pin = pin

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
    if pin not in "123":
      raise ValueError("Invalid password")
    self._pin = pin

class Diary:
  #calander tracker for days journaled
  def show_menu(self):
    while True:
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

      choose = int(input("Enter your choice to proceed: "))
      try:
        match choose:
          case 1:
            console.rule("NEW ENTRIES", characters="~")  #line decorator

            entries = input("What's on your mind today😁 \n")
            time_stamp = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
            with open("entries.csv", "a", newline="") as file:
              writer = csv.DictWriter(file, fieldnames=["time_stamp","entries"])
              writer.writerow({"time_stamp":time_stamp,"entries": entries}) 

          case 2:
            console.rule("Previous Entries", characters="~", style="blue")

            entry = []
            with open("entries.csv", "r") as file:
              reader = csv.DictReader(file)
              for row in reader:
                entry.append({"entries": entry})
                print(row)

          case 3:
            break
          case _:
            print("Please Choose To Proceed") 
      except:
        ValueError("Please Enter 1-3 to continue")
          


        



def main():
  authentification = Authentification.get()
  print(authentification)
  my_diary = Diary()
  my_diary.show_menu()


if __name__=="__main__":
  main()









