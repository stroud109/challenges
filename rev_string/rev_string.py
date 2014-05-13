# reverse a string in python


def rev_string(some_string):
    print some_string[::-1]


def rev_string2(some_string):

    some_list = list(some_string)

    for i in range(len(some_string) / 2):

        temp = some_list[i]
        print 'temp', temp
        some_list[i] = some_list[len(some_list) - 1 - i]
        print 'some_list[i]', some_list[i]
        some_list[len(some_list) - 1 - i] = temp
        print 'some_list[-i]', some_list[-i]

    print ''.join(some_list)

rev_string('desserts')
rev_string2('123456')
