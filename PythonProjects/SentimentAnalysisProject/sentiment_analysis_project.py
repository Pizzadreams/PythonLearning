from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch #extract results 
from bs4 import BeautifulSoup #extract data, navigate the DOM
import requests #get data from site
import re # create regex function to extract comments
import os

tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

# Pass through a prompt to our tokenizer, and get the classification
tokens = tokenizer.encode("This is terrible. What is going on with this? My day has been ruined.", return_tensors="pt")


# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Pass token to model
result = model(tokens)
print(result.logits)
