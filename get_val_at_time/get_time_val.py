"""
get val at a given time

"""

import datetime

some_dict = {
    "A": [('2016-05-22 01:00:00', 'apple'), ('2016-05-22 03:00:00', 'aubergine'), ('2016-05-22 05:00:00', 'aliens')],
    "B": [('2016-05-22 10:00:00', 'banana'), ('2016-05-22 12:00:00', 'blueberry'), ('2016-05-22 15:00:00', 'bumpkin')],
    "C": [('2016-05-22 18:00:00', 'cherry')],
}


def get_val_at_time(some_time, some_key, some_dict):

    some_time = datetime.datetime.strptime(some_time, '%Y-%m-%d %H:%M:%S')

    # let's get the list of vals
    vals = some_dict.get(some_key, None)

    for i in range(len(vals)):
        time = datetime.datetime.strptime(vals[i][0], '%Y-%m-%d %H:%M:%S')

        if vals and len(vals) <= 1:
            if time >= some_time:
                return None  # the time specified pre-dates the key
            else:
                return vals[i][1]
        else:
            if time >= some_time:
                return vals[i - 1][1]

    return vals[-1][1]

my_val = get_val_at_time('2016-05-22 19:00:00', 'C', some_dict)
print "my_val: ", my_val
