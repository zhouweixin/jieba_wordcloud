import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

roots = ['一带一路', '西部大开发', '互联网金融']
for root in roots:
	word2num = json.load(open(root + '.json', 'r'))
	wc = WordCloud(font_path='c:/Windows/Fonts/STFANGSO.ttf', width=1200, height=800, max_words=400, max_font_size=200, background_color='white')
	img = wc.fit_words(word2num)
	plt.figure(root)
	plt.imshow(img)
	plt.axis('off')
	img.to_file(root + '.png')


plt.show()
