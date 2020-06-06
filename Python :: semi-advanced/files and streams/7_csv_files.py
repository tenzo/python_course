import csv
from typing import List, Union


def save_csv(data: List[List], filename: str) -> None:
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for user_list in data:
            writer.writerow(user_list)


def read_csv(filename: str) -> List[List]:
    def transform_to_number(elem: str) -> Union[str, float, int]:
        result = elem
        try:
            if '.' in elem:
                result = float(elem)
            else:
                result = int(elem)
        except ValueError:
            pass
        return result

    data = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            row = [transform_to_number(elem) for elem in row]
            data.append(row)
    return data


if __name__ == '__main__':
    data = read_csv('userdata.csv')
    print(data)
