def maxProfit(prices):
    # maximum subarray of the change in prices
    if len(prices) <= 1:
        return 0

    max_profit = 0
    temp_profit = 0

    for i in range(1, len(prices)):
        if temp_profit > 0:
            temp_profit += prices[i] - prices[i-1]
        else:
            temp_profit = prices[i] - prices[i-1]
        max_profit = max(temp_profit, max_profit)
    return max_profit



    # max_profit = 0
    # diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    #
    # temp_profit = 0
    #
    # for i in range(len(diff)):
    #     if temp_profit > 0:
    #         temp_profit += diff[i]
    #     else:
    #         temp_profit = diff[i]
    #     max_profit = max(temp_profit, max_profit)
    #
    # return max_profit


if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]) == 5)
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]) == 0)
    print(maxProfit([7,6,4,3,1]))
    print(maxProfit([1]) == 0)
    print(maxProfit([1]))
    print(maxProfit([1, 2]) == 1)
    print(maxProfit([1,2]))