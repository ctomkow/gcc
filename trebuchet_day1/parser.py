

sample_data = 'kpzfgp1xdo7nesixfour4ninefourfour'


def find_from_left(line: str) -> int:

    if not isinstance(line, str):
        raise TypeError('line must be a string')
    for s in line:
        if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(s)


print(find_from_left(sample_data))