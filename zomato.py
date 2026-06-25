import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df_zomato = pd.read_csv('zomato.csv')

df_zomato['approx_cost(for two people)'] = df_zomato['approx_cost(for two people)'].astype(str)
df_zomato['approx_cost(for two people)'] = df_zomato['approx_cost(for two people)'].str.replace(',', '', regex=False)
df_zomato['approx_cost(for two people)'] = pd.to_numeric(df_zomato['approx_cost(for two people)'], errors='coerce')

df_zomato['rate'] = df_zomato['rate'].astype(str).str.replace('/5', '', regex=False)
df_zomato['rate'] = pd.to_numeric(df_zomato['rate'], errors='coerce')

df_zomato = df_zomato.dropna(subset=['location', 'cuisines', 'approx_cost(for two people)', 'rate'])

print(df_zomato.shape)

plt.style.use('ggplot')

loc_counts = df_zomato['location'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(loc_counts.index[::-1], loc_counts.values[::-1], color='teal')
plt.title('Where are most restaurants located?')
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df_zomato['rate'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Restaurant Ratings')
plt.show()

cuisines = " ".join(str(c) for c in df_zomato['cuisines'])
wordcloud_c = WordCloud(width=600, height=300, background_color="black", colormap="Greens", max_words=60).generate(cuisines)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_c, interpolation='bilinear')
plt.axis("off")
plt.show()