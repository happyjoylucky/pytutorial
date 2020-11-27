import json
from collections import defaultdict, Counter

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else :
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] +=1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]



path='/Users/supernova/Downloads/usagov_bitly_data2012-12-31-1356995459'

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

counts = get_counts(time_zones)
print(counts['America/Bogota'])
# print(counts)
# print(len(time_zones))
print(top_counts(counts))

counts2 = get_counts2(time_zones)
print(counts2['America/Bogota'])
print(top_counts(counts2))

counts3 = Counter(time_zones)
print(counts3['America/Bogota'])
print(counts3.most_common(10))

