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

def real_basement(basement):
    basement_new=0
    if i>basement>-13:
        basement_new = basement+1
    if basement<13:
        basement_new = basement+2
    if basement==-13:
        basement_new = "there is no basement -13"
    print(basement_new)
