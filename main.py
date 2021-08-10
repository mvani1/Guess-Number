import art
import game_data
import random
from replit import clear

print(art.logo)
seen = {}
# print(random.choice(game_data.data))
def pick_one(one = None):
  data = random.choices(game_data.data,k=1)
  while one != None and one == data[0]:
    data = random.choices(game_data.data,k=1)
  return data
score = 0
one = pick_one()[0]
while True:
  two = pick_one(one)[0]
  
  name1,follower_count1,description1,country1 = one['name'],one['follower_count'],one['description'],one['country']
  name2,follower_count2,description2,country2 = two['name'],two['follower_count'],two['description'],two['country']

  print(f"A...... {name1}, {description1}, {country1}")
  print(art.vs)
  print(f"\nB...... {name2}, {description2}, {country2}")

  a_is_greater = input("Guess who has more followers? 'A' or 'B' \n").lower() == 'a'
  score +=1
  if a_is_greater and follower_count1 >= follower_count2:
    continue
  elif not a_is_greater and follower_count1 <= follower_count2:
    one = two
  else:
    print(f"Sorry that was wrong. Final Score: {score - 1}")
    break
  clear()

