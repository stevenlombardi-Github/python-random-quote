import random 

def primary():
  #print("Keep it logically awesome!!!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd1 = random.randint(0,last)
  rnd2 = random.randint(0,last)
#  if '\n' in quotes[rnd1]:
#       print("there is a newline in here")
  print(quotes[rnd1].rstrip("\n"))
  print(quotes[rnd2].rstrip("/n"))

if __name__== "__main__":
  primary()
