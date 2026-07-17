from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd
sentences = [
    "Hello, world! This is a test sentence.",
    "Let's see how it tokenizes.",
    "This is another sentence for testing.",
    "NLP is fun and interesting!"
    ]
df = pd.DataFrame({'Text' : sentences})
hashvec = HashingVectorizer(n_features = 15, norm = None, alternate_sign = True)
print(hashvec.fit_transform(df.Text).toarray())