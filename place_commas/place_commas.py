"""
write a function that takes an integer input and
formats it as a string with commas placed as thousands separators

for example: format_number(1234) -> "1,234"
1000
formatted_num = 0, counter = 1
formatted_num = 00, counter = 2
formatted_num = 000,1 counter = 3
formatted_num = 000,11 counter = 1
rev_string
"""


def place_commas(some_num):

    num_list = list(str(some_num))

    if len(num_list) < 4:
        return str(num_list)  # return string

    else:
        with_commas = []
        counter = 0
        while len(num_list) > 0:
            last_num = num_list.pop(-1)
            if counter == 3:
                with_commas.append(',')
                with_commas.append(last_num)
                counter = 1
            else:
                with_commas.append(last_num)
                counter += 1

        comma_str = ''.join(with_commas)

    return comma_str[::-1]

print place_commas(1000000000)  # should return 1,000,000,000
