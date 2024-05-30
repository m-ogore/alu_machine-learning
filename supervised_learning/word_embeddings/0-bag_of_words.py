import numpy as np

def bag_of_words(sentences, vocab=None):
    # Calculate the number of sentences
    s = len(sentences)
    
    # Calculate the vocabulary size
    if vocab is None:
        vocab = set(sentences[0].split())
    f = len(vocab)
    
    # Create the embeddings matrix
    embeddings = np.zeros((s, f))
    
    # Initialize the list of features
    features = list(vocab)
    
    # Iterate over each sentence
    for i, sentence in enumerate(sentences):
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate over each word in the sentence
        for word in words:
            # Check if the word is in the vocabulary
            if word in vocab:
                # Set the corresponding feature to 1
                j = features.index(word)
                embeddings[i, j] = 1
    
    return embeddings, features