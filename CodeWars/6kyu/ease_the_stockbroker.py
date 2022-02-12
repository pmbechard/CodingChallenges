"""
Ease the StockBroker
https://www.codewars.com/kata/54de3257f565801d96001200
"""


def balance_statement(lst):
    print(lst)
    bad_orders = []
    good_orders= []
    buy = 0
    sell = 0
    for order in lst.split(', '):
        order = order.split(' ')
        if len(lst) > 0 and len(order) == 4 and order[1].isnumeric() and len(order[2].split('.')) == 2 \
                and (order[3] == 'S' or order[3] == 'B'):
            good_orders += [order]
        else:
            bad_orders += [order]
    for good_order in good_orders:
        if good_order[3] == 'B':
            buy += round(int(good_order[1]) * float(good_order[2]))
        else:
            sell += round(float(good_order[1]) * float(good_order[2]))
    result = f"Buy: {buy} Sell: {sell}"
    if len(lst) > 0 and bad_orders:
        result += '; ' + f'Badly formed {len(bad_orders)}: '
        for bad_order in bad_orders:
            bad_order = str(bad_order).replace('[', '').replace(']', '').replace("'", ''). replace(',', '')
            result += bad_order + ' ;'
        return result
    return result
