en_news = int(input())
en_news_roll = set(map(int, input().split()))
fr_news = int(input())
fr_news_roll = set(map(int, input().split()))
print(len(en_news_roll.symmetric_difference(fr_news_roll)))
