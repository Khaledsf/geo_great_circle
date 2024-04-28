import math

def calculate_great_circle(point_a, point_b):
	# coordinates = input('Please paste full coordinates:\n')
	# coordinates = '-41.40338, 2.17403'
	lat_a = float(point_a.split(',')[0])
	lat_b = float(point_b.split(',')[0])
	lon_a = float(point_a.split(',')[1])
	lon_b = float(point_b.split(',')[1])

	delta_lon, delta_lon = 0,0
	if (lat_a > 0 and lat_b < 0) or (lat_a < 0 and lat_b > 0):
	    delta_lat = abs(lat_a) + abs(lat_b)
	elif (lat_a > 0 and lat_b > 0) or (lat_a < 0 and lat_b < 0):
	    delta_lat = abs(abs(lat_a) - abs(lat_b))
	if (lon_a > 0 and lon_b < 0) or (lon_a < 0 and lon_b > 0):
	    if abs(lon_a) + abs(lon_b) > 180:
	        delta_lon = 360 - (abs(lon_a) + abs(lon_b))
	    else:
	        delta_lon = abs(lon_a) + abs(lon_b)
	elif (lon_a > 0 and lon_b > 0) or (lon_a < 0 and lon_b < 0):
	    delta_lon = abs(abs(lon_a) - abs(lon_b))
	# delta_lon = abs(lon_a - lon_b)
	earth_radius_km = 6371
	hav_theta = math.sin(math.radians(delta_lat/2))**2 + math.sin(math.radians(delta_lon/2))**2 * math.cos(math.radians(lat_a)) * math.cos(math.radians(lat_b))
	angle_theta = 2 * math.degrees(math.asin(math.sqrt(hav_theta)))
	distance = round(math.radians(angle_theta) * earth_radius_km, 2)

	print(delta_lat)
	print(delta_lon)
	print(f'hav_theta:  ',hav_theta, 'rad')
	print('Angle Tetha:', f'{angle_theta}', 'deg')
	print('The distance is:', f'{distance}', 'Km')