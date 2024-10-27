import json
import re
import gensim
import nltk
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis

database = 'database_packs/training_v1/joint_poems_v1.jsonl'

# Load JSONL file
with open(database, "r", encoding="utf-8") as f:
    poems = [json.loads(line)["text"] for line in f]

# Preprocess text
stop_words = set(stopwords.words("english"))
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\W+', ' ', text.lower())  # Remove punctuation
    tokens = word_tokenize(text)
    return [word for word in tokens if word not in stop_words and len(word) > 2]

# Tokenize and prepare documents
processed_poems = [preprocess_text(poem) for poem in poems]

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_poems)
corpus = [dictionary.doc2bow(poem) for poem in processed_poems]

# Train LDA model
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=7, random_state=42, passes=10, alpha='auto', per_word_topics=True)

# Visualize topics
lda_vis = gensimvis.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(lda_vis)