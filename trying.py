win = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
       'devil', 'lightning', 'gun']
win2 = win * 2
print(win2)
winners = {}
z = 1
for x in win:
    winners[x] = win2[z:z + 7]
    z += 1

for k in winners:
    print(k, winners[k])
