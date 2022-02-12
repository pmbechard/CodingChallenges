"""
Snail
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
"""


def snail(snail_map):
    print(list(reversed(snail_map)))
    results = []
    while snail_map:
        results += snail_map[0]
        snail_map.remove(snail_map[0])
        for i in range(0, len(snail_map)):
            if snail_map[i] == snail_map[-1]:
                snail_map[i] = list(reversed(snail_map[i]))
                results += snail_map[i]
                snail_map.remove(snail_map[i])
            else:
                results.append(snail_map[i][-1])
                del snail_map[i][-1]
        for i in range(0, len(snail_map)):
            results.append(list(reversed(snail_map))[i][0])
            del list(reversed(snail_map))[i][0]
    return results
