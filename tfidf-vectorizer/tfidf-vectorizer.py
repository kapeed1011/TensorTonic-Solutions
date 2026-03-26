import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    per_document_token = [doc.lower().split() for doc in documents]
    
    vocab = sorted(set(word for doc in per_document_token for word in doc))
    vocab_index = {word: i for i, word in enumerate(vocab)}
    
    n = len(documents)
    v = len(vocab)
    
    tf_matrix = np.zeros((n, v))
    
    for i, doc_tokens in enumerate(per_document_token):
        for word in doc_tokens:
            word_index = vocab_index[word]
            tf_matrix[i, word_index] += 1
        
        if len(doc_tokens) > 0:
            tf_matrix[i] /= len(doc_tokens)
    
    df = np.sum(tf_matrix > 0, axis=0)
    idf = np.log(n / np.maximum(df, 1))
    
    tf_idf_matrix = tf_matrix * idf
    
    return tf_idf_matrix, vocab
    
