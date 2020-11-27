import json

path='/Users/supernova/Downloads/usagov_bitly_data2012-12-31-1356995459'

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

print(time_zones[:10])

