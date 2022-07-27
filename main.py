
def get_time_presence(data: list):
    time = list(map(lambda x, y: [x, y], data[::2], data[1::2]))
    return time


def appearance(intervals):
    lesson = intervals['lesson']
    intervals = get_time_presence(intervals['pupil']) + get_time_presence(intervals['tutor'])

    for i, interval in enumerate(intervals):
        intervals[i] = cut(lesson, interval)
    intervals.sort()
    total = 0
    for i, current_interval in enumerate(intervals):
        for follow_interval in intervals[i + 1:]:
            if current_interval[1] <= follow_interval[0]:
                break
            print(current_interval, "⋂", follow_interval)
            total += get_len(current_interval, follow_interval)
    return total


def cut(borders, interval):
    if interval[1] <= borders[0] or borders[1] <= interval[0]:  # Интервал за пределами урока
        return [0, 0]
    if borders[1] < interval[1]:  # Откусываем справа
        return [interval[0], borders[1]]

    if borders[0] > interval[0]:  # Откусываем слева
        return [borders[0], interval[1]]
    return interval


def get_len(a, b):
    return min(a[1], b[1]) - max(a[0], b[0])


tests = [
    {'data': {'lesson': [3, 10],
              'pupil': [3, 4, 5, 6, 7, 11],
              'tutor': [1, 4, 6, 12]},
     'answer': 4
     },
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
{'data': {'lesson': [702800, 706400],
              'pupil': [702789, 704500, 702807, 704542, 704512, 704513, 704564, 705150,
                        704581, 704582, 704734, 705009, 705095, 705096, 705106, 706480,
                        705158, 705773, 705849, 706480, 706500, 706875, 706502, 706503,
                        706524, 706524, 706579, 706641],
              'tutor': [700035, 700364, 702749, 705148, 705149, 706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':

    print(appearance(tests[2]['data']))
    '''
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    '''