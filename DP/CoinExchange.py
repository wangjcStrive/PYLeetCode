import sys


# d(i) = min{ d(i-vj)+1 }
# d(3) = min{ d(3-1)+1, d(3-3)+1 } // if d(3-1) and d(3-3) != 0
# example: target: 6, coinList:{1, 3, 5}


# allChangeResult = {0:0, 1:1}
# coinList = [5, 3, 1]

def coinExchange(coinList, target, knowCounts=None):
    if knowCounts == None:
        knowCounts = [0] * (target+1)
    if target in coinList:
        return 1
    if target in knowCounts:
        return knowCounts[target]

    # previous, i set minCount to sys.maxSize()
    minCount = target
    for value in [i for i in coinList if i < target]:
        subChange = 1 + coinExchange(target - value)
        if subChange < minCount:
            minCount = subChange
    knowCounts[target] = minCount
    return minCount


# code fro website
# 1. recursion
def coinsChangeRecursion(coinList, change):
    minCount = change
    if change in coinList:
        return 1
    for value in [i for i in coinList if i <= change]:
        count = 1 + coinsChangeRecursion(coinList, change-value)
        if count < minCount:
            minCount = count
    return minCount



def print_coins(change, last_used_coins):
    used_coins = []
    while change > 0:
        used_coins.append(str(last_used_coins[change]))
        change = change - last_used_coins[change]
    return ','.join(used_coins)


# 3. DP. 是从底向上的计算
def coins_changeDP(coin_values, change, min_counts=None, last_used_coins=None):
    """
    利用动态规划(Dynamic Programming)的思想实现零钱找零
    """
    if min_counts == None:
        min_counts = [0] * (change + 1)
    if last_used_coins == None:
        last_used_coins = [0] * (change + 1)

    for cents in range(change + 1):
        min_count = cents
        for value in [i for i in coin_values if i <= cents]:
            if 1 + min_counts[cents-value] < min_count:
                min_count = 1 + min_counts[cents-value]
                last_used_coins[cents] = value
        min_counts[cents] = min_count

    return min_counts[-1], print_coins(change, last_used_coins)


if __name__ == '__main__':
    coinList = [5, 3, 1]
    result = coins_changeDP(coinList, 6)
    print('%d' % result)



