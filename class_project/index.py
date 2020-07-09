# Following along Tim Roy's guided project

### Caleb's snippet of code 
'''
for name, state in records:
    value = index.setdefault(state, [])
    value.append(name)
'''


records = [
    ("Time", "Texas"),
    ('Adam', "Florida"),
    ("Austin", "Florida"),
    ("Kai", "South Carolina"),
    ("Jud", "Phoebos"),
    ("Eric", "utah"),
    ("Mandi", "Florida"),
    ("Emma", "Florida"),
    ("Anna", "Texas"),
    ("Leo", "New York"),
    ("Andrew", "Utah"),
]

# given a list of records, build an index 
# so we can quickly find everyone in a given state 

# Plan 
## Iterate through the tuples in our list 
## Build a dict as we go 
## Use state as keys and names as value 

### If state isn't in the dict, add it 
### Value: [name1, name2, name3]

### Possible value data structures: list, set, nest hashtable 
#### if nest hashtable, {state: {name: lastname}}


def build_index(records):
    index = {}

    # iterate through list 
    for name, state in records:

    ## for wach pair, check if the state is in the dict 
        if state in index:
    ### if so, append the name to list 
            index[state].append(name)
    ### if not, add the key and list (with name on it)

        else:
            index[state] = []
            index[state].append(name)

    return index


idx = build_index(records)

print(idx["Florida"])
