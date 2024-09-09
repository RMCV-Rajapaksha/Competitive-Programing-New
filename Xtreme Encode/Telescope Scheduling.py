num_star = int(input())
star_list = []
for n in range(num_star):
    star = [int(x) for x in input().split()]
    if len(star_list) == 0:
        star_list.append([star])
    else:
        for i in range(len(star_list)):
            intersect = False
            for j in range(len(star_list[i])):
                lower = star_list[i][j][0]
                upper = star_list[i][j][1]
                if not (lower > star[1] or upper < star[0]): #no intersection
                    intersect = True
                    break
            if not intersect:
                star_list[i].append(star)
        star_list.append([star])

best = 0
for i in range(len(star_list)):
    total = 0
    for j in range(len(star_list[i])):
        total += star_list[i][j][2]
    if total > best:
        best = total

print(best)