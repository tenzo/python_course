from typing import Callable, List


def mean(values: List[float]) -> float:
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    return values[int(len(values) // 2)]


def aggregate(aggregation_function: Callable, values: List[float]):
    return aggregation_function(values)


if __name__ == '__main__':
    values = [3.4, 5.6, 3.2, 5.6, 8.9, 9.0, 10.2]

    print(f'Aggregated with mean: {aggregate(mean, values)}')
    print(f'Aggregated with median: {aggregate(median, values)}')
