"""
Word to initial number
https://www.codewars.com/kata/5bb148b840196d1be50000b1
"""


def convert(st):
    if not st:
        return 0
    elif len(st) == 1:
        return 1
    st_list = list(st.lower())
    for i in st_list:
        while st_list.count(i) > 1:
            st_list.reverse()
            st_list.remove(i)
            st_list.reverse()
    letters_dict = {}
    counter = 0
    for letter in st_list:
        letters_dict[str(counter)] = letter
        counter += 1
    copy_dict = letters_dict.copy()
    try:
        letters_dict['0'], letters_dict['1'] = copy_dict['1'], copy_dict['0']
    except KeyError:
        pass
    for k, v in letters_dict.items():
        st = st.lower().replace(v, k)
    return int(st)
