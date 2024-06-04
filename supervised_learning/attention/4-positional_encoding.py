import numpy as np

def positional_encoding(max_seq_len, dm):

    '''
        max_seq_len : number of words in a sentence
    '''

    PE = np.zeros(shape=(max_seq_len,dm)) 
    '''
        Each word makes a row and each word has an embedding of dimension dm
        a matrix of same dimension as embeddings
    '''

    print(PE)# just to see

    pos =np.arange(max_seq_len)
    pos.reshape(max_seq_len,1) 
    '''
        We want it to be a 1-D array of position of words from 0up to max length,
        Without reshaping it becomes a multi-D array
    '''

    print(pos[1])
    for i in range(max_seq_len):
        for j in range(0,dm,2):

            denominator = 10000**(j/dm)

            PE[i,j] = np.sin(pos[i]/denominator)

            PE[i,j+1] = np.cos(pos[i]/denominator)

    return PE


print(positional_encoding(30,512))