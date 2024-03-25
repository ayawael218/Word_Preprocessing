import nltk
import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words as nltk_words
from nltk.stem import WordNetLemmatizer


# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('words')

# URL of the webpage to extract text from
url = 'https://en.wikipedia.org/wiki/Natural_language_processing'

# Retrieve HTML content from the URL
response = requests.get(url)
html_content = response.text

# parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text from paragraphs and headings tags
text = ' '.join([tag.get_text() for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])

# Clean data by removing symbols and special characters
cleaned_text = re.sub(r'[^a-zA-Z0-9_\s]', '', text)

# Normalize text to lowercase
cleaned_text = cleaned_text.lower()

# Tokenize the text into words
words_list = word_tokenize(cleaned_text)

# Lemmatize each word to its base form
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_list]

# Get English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words from the text
filtered_words = [word for word in lemmatized_words if word not in stop_words]

# Get unique words from the list
unique_words = set(filtered_words)

english_words = set(nltk_words.words())

unique_words = [word for word in unique_words if len(word) < 3]

print("Unique English words:", unique_words)
