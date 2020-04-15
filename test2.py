import itertools
saidai = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for v in itertools.permutations(list, 9):
    top1 = v[0]*100
    top2 = v[1]*10
    top3 = v[2]
    top = top1 + top2 + top3
    bot1 = v[3]*100
    bot2 = v[4]*10
    bot3 = v[5]
    bot = bot1 + bot2 + bot3
    ans1 = v[6]*100
    ans2 = v[7]*10
    ans3 = v[8]
    ans = ans1 + ans2 + ans3
    shiki = top + bot
    if(shiki == ans):
        if(saidai < ans):
            listA = []
            listA.append(top)
            listA.append(bot)
            saidai = ans
    continue
print(listA[0])
print(listA[1])
print(saidai)