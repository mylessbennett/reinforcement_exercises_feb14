trains = [
    {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
    {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
    {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
    {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
    {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
    {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
    ]
#--------------------------------------------------------------------------------------------------------------
# Save the direction of train 111 into a variable.
#--------------------------------------------------------------------------------------------------------------
direction_t111 = trains[7]['direction']
print(direction_t111)
#--------------------------------------------------------------------------------------------------------------
# Save the frequency of train 80B into a variable.
#--------------------------------------------------------------------------------------------------------------
freq_t80B = trains[5]['frequency_in_minutes']
print(freq_t80B)
#--------------------------------------------------------------------------------------------------------------
# Save the direction of train 610 into a variable.
#--------------------------------------------------------------------------------------------------------------
direction_t610 = trains[2]['direction']
print(direction_t610)
#--------------------------------------------------------------------------------------------------------------
# Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.
#--------------------------------------------------------------------------------------------------------------
north_trains = []

for i in range(0,len(trains)):
    if trains[i]['direction'] == 'north':
        north_trains.append(trains[i]['train'])

print(north_trains)
#--------------------------------------------------------------------------------------------------------------
# Do the same thing for trains that travel east.
#--------------------------------------------------------------------------------------------------------------
east_trains = []

for i in range(0, len(trains)):
    if trains[i]['direction'] == 'east':
        east_trains.append(trains[i]['train'])

print(east_trains)
#--------------------------------------------------------------------------------------------------------------
# You probably just ended up rewriting some of the same code. Move this repeated code into a function that accepts
# a direction and a list of trains as arguments, and returns a list of just the trains that go in that direction.
# Call this function once for north and once for east in order to DRY up your code.
#--------------------------------------------------------------------------------------------------------------
direction = 'south'

def train_direction(list_of_trains, direction):
    new_list = []
    for i in range(0, len(list_of_trains)):
        if list_of_trains[i]['direction'] == direction:
            new_list.append(list_of_trains[i]['train'])
    return new_list

dir = train_direction(trains, direction)
print(directions)
#--------------------------------------------------------------------------------------------------------------
# Pick one train and add another key/value pair for the first_departure_time. For simplicity, assume the first train
 # always leave on the hour. You can represent this hour as an integer: 6 for 6:00am, 12 for noon, 13 for 1:00pm, etc.
#--------------------------------------------------------------------------------------------------------------
trains[4]['first_departure_time'] = 8
print(trains)

#--------------------------------------------------------------------------------------------------------------
# Now we want to (programmatically) make a new dictionary where the train frequencies are the keys and the values
 # are a list of train names, like so: python { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] }
#--------------------------------------------------------------------------------------------------------------
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

trains_by_frequency = {}

for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)
