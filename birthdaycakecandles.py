numCandles = int(input())

candles = [int(x) for x in input().split(' ')]

tallest = 0

for candle in candles:
    if candle > tallest or tallest == 0:
        tallest = candle

print(candles.count(tallest))
