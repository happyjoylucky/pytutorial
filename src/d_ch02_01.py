import json

path='/Users/supernova/Downloads/usagov_bitly_data2012-12-31-1356995459'
# a = open(path).readline()

# for line in open(path):
#     records = json.loads(line) 

records = [json.loads(line) for line in open(path) ]

# records = []
# for line in open(path):
#     records.append(json.loads(line))

# print(records[0])
print(records[0]['tz'])