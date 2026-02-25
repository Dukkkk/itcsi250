import json

with open('Lab3/schedule.json', 'r') as f:
    data = json.load(f)

location_count = {}

for item in data:
    location = item['khicheellekh_bair']
    location_count[location] = location_count.get(location, 0) + 1


most_common = max(location_count, key=location_count.get)
print("Hamgiin olon hicheel ordog bair(Lecture,Seminar,Lab):", most_common, location_count[most_common])


print("MUIS-iin bairnuud deer orj bui hicheeluudin too (Lecture,Seminar,Lab):")
for location in location_count:
    print(location, location_count[location])
#MUIS-iin bairnuudaas hamgiin ih hicheel ordog bair(Lecture,Seminar,Lab) ni 2-dugaar bair baina.