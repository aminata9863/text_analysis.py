from textblob import TextBlob

# Анализируем тональность текста
text = "I love this product! It's the best thing ever."
sentiment = TextBlob(text).sentiment.polarity

# Выводим результат
if sentiment > 0:
    print("Positive sentiment")
elif sentiment < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
