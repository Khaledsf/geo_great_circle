from geo_great_circle import calculate_great_circle


# parse input to determine if it is dd or min-sec.
type_of_action  = input('If you want calculate distance between two points enter 1\nif you want to convert coordiantes enter 2\n')
point_a = ''
point_b = ''
if type_of_action == '1':
    print('You are calculating distance\nenter coordinates of point A')
    point_a = input('Point A:')
    point_b = input('Point B:')
else:
    print('you chose to use degree, minutes, and seconds')

calculate_great_circle(point_a, point_b)

