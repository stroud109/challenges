"""
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time

For now, let's assume that the time/value pairs are appended to the list in chronological order,
so the oldest times will be at the beginning of the list and the newest times will be at the end of the list.

Let's also assume these lists could be rather long ;)
"""

import datetime

some_dict = {
    "A": [('2016-05-22 01:00:00', 'apple'), ('2016-05-22 03:00:00', 'aubergine'), ('2016-05-22 05:00:00', 'aliens')],
    "B": [('2016-05-22 10:00:00', 'banana'), ('2016-05-22 12:00:00', 'blueberry'), ('2016-05-22 15:00:00', 'bumpkin')],
    "C": [('2016-05-22 18:00:00', 'cherry')],
}


def get_value_at_time(some_dict, key, time_string):

    # if the key is not in the dict, raise an exception
    if not some_dict[key]:
        raise KeyError

    def _format_datetime(some_time_string):
        return datetime.datetime.strptime(some_time_string, "%Y-%m-%d %H:%M:%S")

    # make sure the time is a datetime object so we can compare times
    time_input = _format_datetime(time_string)

    # if time_input pre-dates the first key in the ordered list, return N/A
    if time_input < _format_datetime(some_dict[key][0][0]):
        return None

    # if there's only 1 tuple in the ordered list and time_input is more recent than the key, return the value
    elif len(some_dict[key]) < 2:
        key_time = _format_datetime(some_dict[key][0][0])
        if time_input >= key_time:
            return some_dict[key][0][1]  # set the value in the orginal string format

    # iterate through the list to find the most recent time that pre-dates time_input
    else:
        value = None
        for i in xrange(len(some_dict[key])):
            time, value = some_dict[key][i]
            key_time = _format_datetime(time)
            # if the time_put is older than a given time, return the time value in the tuple before it
            if time_input <= key_time:
                value = some_dict[key][i - 1][1]
                break

        return value


print get_value_at_time(some_dict, "A", "2016-05-22 02:00:00")
