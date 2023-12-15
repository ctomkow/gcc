

sample_data = 'kpzfgp1xdo7nesixfour4ninefourfour'


def parse_from_left(line: str) -> str:

    if not isinstance(line, str):
        raise TypeError('line must be a string')
    for s in line:
        if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return s


print(parse_from_left(sample_data))
