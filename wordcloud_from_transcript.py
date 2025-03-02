from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import defaultdict
from PIL import Image
import numpy as np
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate a word cloud from a transcript.')
parser.add_argument('--input', type=str, required=True, help='Path to the input text file.')

# Parse arguments
args = parser.parse_args()

# Assign arguments to variables
input_file = args.input

file_path = input_file

# open the file in read mode
with open(file_path, 'r') as file:
    # read the contents of the file
    file_contents = file.read()

# Initialize a dictionary to hold the lines for each speaker
speakers = defaultdict(list)

# Split the file contents into lines
lines = file_contents.split('\n')

# Iterate through each line and categorize by speaker
for line in lines:
    if line.startswith('['):
        speaker, text = line.split(']: ', 1)
        speakers[speaker].append(text)

# Extract the texts for each speaker
trump_texts = speakers['[Trump']
zelenskyy_texts = speakers['[Zelenskyy']
vance_texts = speakers['[Vance']

# Combine common word I generally exclude the texts for each speaker into a single string
additional_stopwords = { "fuck", "sex", "bang", "seggs", "finished", "come","came", #dirty words
                        "Cal", "drink", "alcohol", "drinks",
                        "m","ve",'year','years','and', 'but', 'if', 'or', "got",
                        'became','day','because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
                        'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 
                        'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 
                        'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 
                        'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 
                        'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', "d", 'can', 'will',
                          'just', 'don', 'should', 'now','hate','beer','wasn', "put", "re",
                          "ll", "didn"}

stopwords = set(STOPWORDS).union(additional_stopwords)

# Create my image mask and folor array
mask_array = np.array(Image.open("usa_flag.png").convert("L"))
mask_array = np.where(mask_array > 128, 255, 0)

# Load the color image and resize it to match the canvas dimensions.
color_image = Image.open("usa_flag.png").convert("RGB")
color_array = np.array(color_image)

# Create the image color generator from the resized color image.
image_colors = ImageColorGenerator(color_array)


# Generate the word cloud without a custom color function.
wc = WordCloud(background_color="white",
               mode="RGBA",
               mask=mask_array,
               stopwords=stopwords,
               width=1600,
               height=1600,
               min_font_size=10,
               max_words=2000,
               repeat=True
              ).generate(" ".join(trump_texts).join(vance_texts))

# Recolor the word cloud using the image's color scheme.
wc_recolored = wc.recolor(color_func=image_colors)

wc.to_file("usa_flag_wordcloud.png")

def two_color_flag_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # Swap coordinates if necessary:
    y, x = position  # now treating the first element as y (vertical) and second as x (horizontal)
    if y < (wc.height / 2):
         return "rgb(0, 91, 187)"  # Blue for top half
    else:
         return "rgb(255, 213, 0)"  # Yellow for bottom half

mask_array = np.array(Image.open("ukraine_flag.png").convert("L"))
#mask_array = np.where(mask_array > 128, 255, 0)

# Assume transformed_mask is already created with the desired shape.
# Also assume stopwords, font, and final_frequencies are defined.

# Load the color image and resize it to match the canvas dimensions.
color_image = Image.open("ukraine_flag.png").convert("RGB")
#color_image = color_image.resize((1600, 1600), Image.Resampling.LANCZOS)
color_array = np.array(color_image)

# Generate the word cloud without a custom color function.
wc = WordCloud(background_color="white",
               mode="RGBA",
               mask=mask_array,
               stopwords=stopwords,
               width=1600,
               height=1600,
               min_font_size=10,
               max_words=2000,
               repeat=True,
               max_font_size=100,
               prefer_horizontal=1.0,
              ).generate(" ".join(zelenskyy_texts))

# Create the image color generator from the resized color image.
image_colors = ImageColorGenerator(color_array)

# Recolor the word cloud using the image's color scheme.
wc_recolored = wc.recolor(color_func=two_color_flag_color_func)

wc.to_file("ukraine_flag_wordcloud.png")