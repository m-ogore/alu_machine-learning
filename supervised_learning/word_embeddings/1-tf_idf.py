import numpy as np

def tf_idf(sentences, vocab=None):

    word_list = [sentence.lower().split() for sentence in sentences]

    if vocab: 
        extracted = []
        for words in word_list:
            
            for word in words:
                
                if word in vocab:
                    print(word)
                    extracted.append(word)
    print(extracted)

    tf = np.zeros(len(sentences), len(set(extracted)))

    #print(all_words)
        
        #[[word for word in words if word in vocab] for words in words_list]
    
    f = len(vocab)
    s = len(sentences)

    
    # idf = []
    # tf = []
    # unique_word_list = set(word_list)

    # if vocab:
    #     if word in vocab

    # for sentence in sentences:
    #     words = sentence.split()
    #     unique_words = set(words)
    #     unique_all.extend(unique_words)

    #     for unique_word in unique_words:
    #         word_count = words.count(unique_word)
    #         tf.append(word_count / len(words))

    # unique_all = set(unique_all)
    
    # word_sentences_count = {}
    
    # for sentence in sentences:
    #     for uniqueword in set(sentence.split()):
    #         if uniqueword in unique_all:
    #             word_sentences_count[uniqueword] = word_sentences_count.get(uniqueword, 0) + 1

    # idf = [s / count if count > 0 else 0 for count in word_sentences_count.values()]

    # tfidf_matrix = np.array(tf) * np.array(idf)

    return word_list, vocab
    
sentences = ["Holberton school is Awesome!",
             "Machine learning is awesome",
             "NLP is the future!",
             "The children are our future",
             "Our children's children are our grandchildren",
             "The cake was not very good",
             "No one said that the cake was not very good",
             "Life is beautiful"]
vocab = ["awesome", "learning", "children", "cake", "good", "none", "machine"]
E, F = tf_idf(sentences, vocab)
# print(E)
# print(F)