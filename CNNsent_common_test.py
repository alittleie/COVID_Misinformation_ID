import pandas as pd

import nltk
import gensim
import string
from gensim import corpora, models,similarities
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation, Flatten, Conv2D, MaxPool1D, MaxPool2D, Conv1D,Conv2D,GlobalAveragePooling1D, AvgPool1D
from nltk.stem.lancaster import LancasterStemmer
from tensorflow.keras.callbacks import  TensorBoard
import datetime

st = LancasterStemmer()

array_text = []
binary = []
sent = []
df = pd.read_excel(r"C:\Users\mxr29\OneDrive\Desktop\Twitter Geo\INVALID_Common_Test_Full_INVALID.xlsx", sheet_name='Sheet1')
print(df.head())
dc= df['Text']
dd= df['Mis']
print(dd)
for s in range(len(dd)):
    if dd.iloc[s] == 0 or dd.iloc[s] == .5 or dd.iloc[s] == 1 :
        binary.append(0)
    else:
        binary.append(1)
tok_dc = [nltk.word_tokenize(str(sent)) for sent in df['Text']]
tok_clean = []

stoplist = set('for a of the and to in'.split())
for i in range( len (tok_dc)):
    list_hold = []
    for o in range(len(tok_dc[i])):
        if tok_dc[i][o] not in string.punctuation  and "/" not in tok_dc[i][o] and tok_dc[i][o] != 'https' :
           list_hold.append(tok_dc[i][o])

    tok_clean.append(list_hold)


tok_dc = tok_clean
size = 50
modelw = gensim.models.Word2Vec(tok_dc, size= size)

length_text = len(tok_dc)
max_length = 0

for i in range(length_text):

        length_word = len(tok_dc[i])

        if max_length < length_word:

            max_length = length_word




for i in range(length_text):

        length_word = len(tok_dc[i])
        array_shape = np.zeros(((max_length), (size)))
        hold = []
        for t in range (length_word):
            # try:
            #     stem = st.stem(tok_dc[i][t])
            #     print(1)
            # except:
            word = tok_dc[i][t]
            word = word.lower()
            try:

                var = modelw.wv[word]
                # print(word)

            except KeyError as e:
                # print('BAD_WORD_CATCH:')
                # print(word)
                try:
                    sno = nltk.stem.SnowballStemmer('english')
                    stem = sno.stem(tok_dc[i][t])
                    # print(stem)
                    var = modelw.wv[stem]
                    print('fix')

                except:


                    var = [0,1]
            # #stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
            #              "you", "your", "yours", "yourself", "yourselves", "he",
            #              "him", "his", "himself", "she", "her", "hers", "herself",
            #              "it", "its", "itself", "they", "them", "their", "theirs",
            #              "themselves", "what", "which", "who", "whom", "this", "that",
            #              "these", "those", "am", "is", "are", "was", "were", "be",
            #              "been", "being", "have", "has", "had", "having", "do",
            #              "does", "did", "doing", "a", "an", "the", "and", "but", "if",
            #              "or", "because", "as", "until", "while", "of", "at", "by", "for",
            #              "with", "about", "against", "between", "into", "through",
            #              "during", "before", "after", "above", "below", "to", "from", ""
            #             "up", "down", "in", "out", "on", "off", "over", "under", "again",
            #              "further", "then", "once", "here", "there", "when", "where", "why",
            #              "how", "all", "any", "both", "each", "few", "more", "most", "other",
                #          "some", "such", "no", "nor", "not", "only", "own", "same",
                #          "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                #          "should", "now"]
            # if word in stopwords:
            #     var =[0,1]
                #print("Get rid of that stopword!")
            if len(var) != 2:

                hold.append(var)
                array_shape[t,:] =  np.array([var])


        array_text.append(array_shape)


dx = np.asarray(array_text)
print(dx.shape)


dy = np.asarray(binary)
from sklearn.model_selection import train_test_split as tts
xtrain,xtest,ytrain,ytest = tts(dx,dy,test_size=.2, random_state= 101, stratify= dy )


model = Sequential( )
model.add(Conv1D(max_length, 3 , input_shape =(max_length,size) ))
model.add(Activation("sigmoid"))
model.add(AvgPool1D(pool_size=3))
#model.add(Dropout(0.2))

model.add(Conv1D(max_length, 3 ))
model.add(Activation("sigmoid"))
model.add(MaxPool1D(pool_size=3))
model.add(Dropout(0.2))

model.add(Conv1D(max_length, 2 ))
model.add(Activation("sigmoid"))
model.add(AvgPool1D(pool_size=2))
model.add(Dropout(0.2) )

model.add(Conv1D(max_length, 2 ))
model.add(Activation("sigmoid"))
model.add(MaxPool1D(pool_size=2))
model.add(Dropout(0.2))
#model.add(GlobalAveragePooling1D())


model.add(Flatten())
model.add(Dense(max_length))
model.add(Activation("sigmoid"))
model.add(Dropout(0.3))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss ="binary_crossentropy",
              optimizer='adam',
              metrics=[['accuracy'],
                       [tf.keras.metrics.TruePositives(thresholds=None, name=None, dtype=None)],
                       [tf.keras.metrics.FalsePositives(thresholds=None, name=None, dtype=None)],
                       [tf.keras.metrics.FalseNegatives(thresholds=None, name=None, dtype=None)],
                       [tf.keras.metrics.TrueNegatives(thresholds=None, name=None, dtype=None)],
                       ]

              )
log_dir="Users\mxr29\logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
model.fit(xtrain,ytrain, verbose= 2 , validation_data=(xtest, ytest), batch_size=25, epochs= 100,callbacks = [tensorboard_callback] )

model.save(r'C:\Users\mxr29\OneDrive\Desktop\Twitter Geo\ML Models\cnn_test')

