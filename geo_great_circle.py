import math

lat_a = float(input('Enter Latitude A number: '))
lat_b = float(input('Enter Latitude B number: '))
lon_a = float(input('Enter Longitude A number: '))
lon_b = float(input('Enter Longitude B number: '))


delta_lat = abs(lat_a - lat_b)
delta_lon = abs(lon_a - lon_b)
earth_radius_km = 6371
hav_theta = math.sin(math.radians(delta_lat/2))**2 + math.sin(math.radians(delta_lon/2))**2 * math.cos(math.radians(lat_a)) * math.cos(math.radians(lat_b))
angle_theta = 2 * math.degrees(math.asin(math.sqrt(hav_theta)))
distance = round(math.radians(angle_theta) * earth_radius_km, 2)

print(f'hav_theta:  ',hav_theta, 'rad')
print('Angle Tetha:', f'{angle_theta}', 'deg')
print('The distance is:', f'{distance}', 'Km') 
