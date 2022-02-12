"""
Simple Fun #243: Perfect Team Of MinimalSize
https://www.codewars.com/kata/590a924c7dfc1a238d000047
"""

import itertools


def perfect_team_of_minimal_size(n, candidates):
    n_list = [i for i in range(n)]
    for candidate in candidates:
        if candidate == n_list:
            return 2
    else:
        counter = 2
        while counter <= len(candidates):
            combinations = list(itertools.combinations(candidates, counter))
            for combination in combinations:
                result = []
                for x in combination:
                    for y in x:
                        result.append(y)
                if set(result) == set(n_list):
                    return counter + 1
            counter += 1
    return -1
