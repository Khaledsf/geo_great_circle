import re

def validate_lat_long(string):
    """Validates if the string is in the format 'float, float'."""
    pattern = r'^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*$'
    return re.match(pattern, string) is not None

def dd_to_minutes_seconds(coordinates):
	# dd_raw = '-41.40338, 2.17403'
	if validate_lat_long(coordinates):
		print('Coordinates are valid!')
	else:
		print('''coordinates are NOT valid! \n 
			Please ensure that the format is as in the example below:\n 
			EX: 41.40338, 2.17403 \n 
			Note: For South latitude or West longitude, add \'-\' in front of coordinate value.
			''')
		return
		

	dd_list = []
	dd = dd_raw.split(',')
	dd_list.append(float(dd[0].strip()))
	dd_list.append(float(dd[1].strip()))

	lat_minutes = int((float(abs(dd_list[0])) - int(abs(dd_list[0]))) * 60)
	lat_seconds =  round((((float(abs(dd_list[0])) - int(abs(dd_list[0])))) * 60 - lat_minutes) * 60, 1) 
	lat_cardinality = ''
	if int(dd_list[0]) > 0:
	    lat_cardinality = 'N'
	else:
	    lat_cardinality = 'S'
	latitude = f'{int(abs(dd_list[0]))}°{lat_minutes}\'{lat_seconds}\"{lat_cardinality}'

	lon_minutes = int((float(abs(dd_list[1])) - int(abs(dd_list[1]))) * 60)
	lon_seconds =  round((((float(abs(dd_list[1])) - int(abs(dd_list[1])))) * 60 - lon_minutes) * 60, 1)
	lon_cardinality = ''

	if int(dd_list[1]) > 0:
	    lon_cardinality = 'E'
	else:
	    lon_cardinality = 'W'
	longitude = f'{int(abs(dd_list[1]))}°{lon_minutes}\'{lon_seconds}\"{lon_cardinality}'
	return(latitude, longitude)
	
# test with coordinates. 
# print(dd_to_minutes_seconds('-41.40338, 2.17403'))


def minutes_seconds_to_dd(coordinates):
	lis = []
	for i in re.split(r'\D+',coordinates):
	    lis.append(re.sub("\D", "", i))

	for i in coordinates:
	    if i in ['N','n','S','s']:
	        lis.insert(3, i.upper())
	    elif i in ['E','e','W','w']:
	        lis[7] = i.upper()
	lat_deg,lat_minutes,lat_sec,lat_card,lon_deg,lon_minutes,lon_sec,lon_card = lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7]
	return(str(int(lat_deg) + round((int(lat_minutes) * 60 + int(lat_sec)) / 3600, 4))+'°' + ' ' + lat_card + ', ' + str(int(lon_deg) + round((int(lon_minutes) * 60 + int(lon_sec)) / 3600, 4))+'°' + ' ' + lon_card)

coordinates = '40° 45\' 11" N, 73° 58\'59" W'
# test with coordinates. 
print(minutes_seconds_to_dd(coordinates))
































