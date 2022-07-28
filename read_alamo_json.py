import json

pf = open('data/9300_profile.json')
ppf = open('data/9300_profile_position.json')
profile = json.load(pf)
profile_position = json.load(ppf)

# This exchanges a single quote for nothing.
translation = {39: None}

f = open('data/9300_profile_lines.json', "w")
columns = profile_position['columns'] + profile['columns'][1:]
f.write(str(columns).translate(translation)+'\n')

index = 0
dive = profile_position['data'][index]

for dive_point in profile['data']:
    if dive[0] == dive_point[0]:
        row = dive + dive_point[1:]
        f.write(str(row).translate(translation)+'\n')
    else:
        index = index + 1
        dive = profile_position['data'][index]
        row = dive + dive_point[1:]
        f.write(str(row).translate(translation)+'\n')
f.close()


