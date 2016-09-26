import string, random

f = open("occupations.csv","r")

s = f.read().strip().split("\r\n")

d = {}

# transfer to dictionary
for line in s:
    key = line.rsplit(",",1)[0].rsplit(",",1)[0]
    key = string.strip(key,'\"') # remove double quotes
    l = []
    l.append(line.rsplit(",",1)[0].rsplit(",",1)[1])
    l.append(line.rsplit(",",1)[1])
    value = l
    d[key] = value

del d["Job Class"]
del d["Total"]

# convert values to float nums
for key in d:
    d[key] = float(d[key])

def random_job():
    random_num = random.random()*100
    threshold = 0.0
    for key in d:
        threshold += d[key]
        if random_num < threshold:
            return key
    return "Other"

def get_dict():
    return d
for i in range(20):
    print random_job()
