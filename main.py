passwords = open("Passwords.csv", "r").read().split('\n')

count1 = 0
count2 = 0

for row in passwords:
    entries = str(row).split(' ')
    if int(entries[0].split('-')[0]) <= entries[2].count(entries[1][0]) <= int(entries[0].split('-')[1]):
        count1 += 1
    if (entries[2][int(entries[0].split('-')[0])-1] + entries[2][int(entries[0].split('-')[1])-1]).count(entries[1][0]) == 1:
        count2 += 1
print("Part1 Count:\t", count1)
print("Part2 Count:\t", count2)
