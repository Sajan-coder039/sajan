from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="sajan  sah"
wordcloud=WordCloud(width=200, height=200, background_color="white").generate(text)

plt.imshow(wordcloud, interpolation="quadric")
plt.axis("off")
plt.show()