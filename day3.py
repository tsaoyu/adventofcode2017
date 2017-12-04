data = 289326
n = 1
upper_range = 1

while upper_range < data:
    n += 2
    upper_range = n ** 2

lower_range = (n-2) ** 2
num_range = upper_range - lower_range

quad = ((data - lower_range) / (num_range/4))

if 0 < quad <=1:
    coor = (0, data - lower_range)
elif 1 < quad <=2:
    coor = (data - (lower_range + num_range/4), n-1)
elif 2 < quad <=3:
    coor = (n-1, data - (lower_range + 2*num_range/4))
else:
    coor = (0, upper_range- data)


centre_coor = ((n-1)/2, (n-1)/2)

print(abs(coor[0] - centre_coor[0]) + abs(coor[1] - centre_coor[1]))
