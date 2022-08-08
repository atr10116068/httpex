import random

gid=["1696182045","1696182046","1696182047","1696182048","1696182049"]
imb=["karena","ketika","saat","dan","melihat","mendengar"]
game={
    '1696182045': ['satria','terkejut','saya','berenang'],
    '1696182046': ['aku','lompat','host','menendangnya'],
    '1696182047': ['budi','ngupil','aku','sedih'],
    '1696182048': ['andi','makan','posa','lari'],
    '1696182049': ['budi','reflek','radi','berenang'],
    }

disp=f"{game[random.choice(gid)][0]} {game[random.choice(gid)][1]} {random.choice(imb)} {game[random.choice(gid)][2]} {game[random.choice(gid)][3]}"
print(disp)
