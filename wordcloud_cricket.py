from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
from PIL import Image
import numpy as np

TXT_FILE = Path.cwd() / "cricket.txt"

# Read text
text = open(TXT_FILE, mode="r", encoding="utf-8").read()
stopwords = STOPWORDS

# Load your custom mask image
mask_image = np.array(Image.open("ipl24.png"))

wc = WordCloud(
    background_color="white",
    stopwords=stopwords,
    height=2000,
    width=1000,
    mask=mask_image,
    contour_width=3,
    contour_color='black',
    max_words=200,           # Limit the number of words
    max_font_size=80,        # Adjust the maximum font size
    prefer_horizontal=0.9,  # Adjust horizontal/vertical preference
)

wc.generate(text)

# Store to file
wc.to_file("wordcloud_output1.png")

# Display the WordCloud with the shape
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()