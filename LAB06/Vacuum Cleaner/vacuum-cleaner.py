#vaccuum cleaner problem

#1 = unclean state of the room
#0 = clean state of the room

vaccuum = 'a'
cost = 0

start = {
    'a': 1, 'b': 1
}

goal = {
    'a': 0, 'b': 0
}

while( start != goal ):

  if vaccuum=='a' and start['a']==1:
    cost = cost + 1
    vaccuum = 'b'
    start['a']=0
    cost = cost + 1
    print("room 'a' cleaned and vc moves to room 'b'")

  elif vaccuum=='a' and start['a']==0:
    vaccuum = 'b'
    cost = cost + 1
    print("vc moves to room 'b'")

  elif vaccuum=='b' and start['b']==1:
    cost = cost + 1
    vaccuum = 'a'
    start['b']=0
    cost = cost + 1
    print("room 'b' cleaned and vc moves to room 'a'")

  elif vaccuum=='b' and start['b']==0:
    vaccuum = 'a'
    cost = cost + 1
    print("vc moves to room 'b'")

print("cost:", cost)

