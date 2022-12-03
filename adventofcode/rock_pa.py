# ===============>finding the score of rock paper sessor=========>
# given the  text file input

with open("rock_pa.txt", "r") as file:
    file_read = file.readlines()
A = 1
B = 2
C = 3
X = 1
Y = 2
Z = 3
draw = 3
lost = 0
win = 6
total = 0
# =================for cal part 01===========
for i in file_read:
    if i[0] == "A" and i[2] == "X":
        total = total + X + draw
    if i[0] == "A" and i[2] == "Y":
        total = total + Y + win
    if i[0] == "A" and i[2] == "Z":
        total = total + Z + lost
    if i[0] == "B" and i[2] == "X":
        total = total + X + lost
    if i[0] == "B" and i[2] == "Y":
        total = total + Y + draw
    if i[0] == "B" and i[2] == "Z":
        total = total + Z + win
    if i[0] == "C" and i[2] == "X":
        total = total + X + win
    if i[0] == "C" and i[2] == "Y":
        total = total + Y + lost
    if i[0] == "C" and i[2] == "Z":
        total = total + Z + draw
total = 0
# =================for cal part 02===========
for i in file_read:
    if i[0] == "A" and i[2] == "X":
        total = total + 3 + 0
    if i[0] == "A" and i[2] == "Y":
        total = total + 1 + 3
    if i[0] == "A" and i[2] == "Z":
        total = total + 2 + 6
    if i[0] == "B" and i[2] == "X":
        total = total + 1 + 0
    if i[0] == "B" and i[2] == "Y":
        total = total + 2 + 3
    if i[0] == "B" and i[2] == "Z":
        total = total + 3 + 6
    if i[0] == "C" and i[2] == "X":
        total = total + 2 + 0
    if i[0] == "C" and i[2] == "Y":
        total = total + 3 + 3
    if i[0] == "C" and i[2] == "Z":
        total = total + 1 + 6
# print("testing it ==========>")
