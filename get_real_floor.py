import random

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

def elevator(elevator_floor):
    for i in int(elevator_floor - 1):
        if i==13:
            continue
        else:
            print("now passing floor "+str(i))
            continue

elevator(4)
elevator(9)
elevator(24)
elevator(-20)

def stairs(stairs_floor):
    for i in int(stairs_floor):
        if i>0:
            print("heavi"+(i*"er")+" breathing")
        if i==0:
            print("your destination is on this floor, why are you taking the stairs?")

stairs(6)
stairs(0)
stairs(77)

def vent(rooms_to_travel):
    if rooms_to_travel<=2:
        print("you've traveled successfully")
        i=random.randrange(1)
        if i<0.5:
            print("you've been found!")
        else:
            print("you've made it!")