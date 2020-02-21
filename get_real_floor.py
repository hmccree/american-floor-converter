def real_floor(floor):
    floor_new=0
    if 1<floor<13:
        floor_new = floor-1
    if floor<=0:
        floor_new = floor
    if floor>13:
        floor_new = floor-2
    if floor==13:
        floor_new = "there is no floor 13"
    print(floor_new)

real_floor(3)
real_floor(7)
real_floor(20)
real_floor(1)
real_floor(-6)