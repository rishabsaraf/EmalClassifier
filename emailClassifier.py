"""
@author: rishabsaraf93
"""
from sklearn import svm
from scipy import io

import os
import numpy
import getVocabList
import processEmail


def emailFeatures(word_indices = []) :

    #featureLength
    N = 1899

    x = [0] * N
    for i in range(len(word_indices)) :
        x[ word_indices[i] ] = 1
    
    return x


def main() :

    path = os.getcwd()
    path = os.path.join(path,'dataSets')

# ===============  Part 1 ====================
    #  To use an SVM to classify emails into Spam v.s. Non-Spam, we first need
    #  to convert each email into a vector of features. In this part, we
    #  implement the preprocessing steps for each email. 

    f = open(os.path.join(path,"emailSample1.txt"),'r')
    email_contents = f.read()
    f.close() 

    print(email_contents)

    word_indices = processEmail.processEmail(email_contents)
    features = emailFeatures(word_indices)
    
    print('Word Indices :\n')
    print(word_indices, "\n")


#=============  Part 2  =======================
    # Print Stats

    print('Length of feature vector: %d\n'  % len(features))
    print('Number of non-zero entries: %d\n' % sum(features))



# =============  Part 3  ======================

    #  In this section, we will train a linear classifier to determine if an
    #  email is Spam or Not-Spam.


    print('\n\nRunning SVM on training set...')

    mat = io.loadmat(os.path.join(path,'spamTrain.mat'))

    X = mat['X']
    y = mat['y']
    
    y = numpy.ravel(y)

    model = svm.SVC(C = 0.1, kernel='linear')
    model.fit(X, y)

    p = model.predict(X)

    accuracy = model.score(X, y)
    accuracy *= 100.0

    print('\nTraining Accuracy: %.2f' % accuracy)
   
#================ Part 4 ========================

    # Xtest and ytest are the env. variables
    mat = io.loadmat(os.path.join(path,'spamTest.mat'))

    XTest = mat['Xtest']
    yTest = mat['ytest']
    
    yTest = numpy.ravel(yTest)

    p = model.predict(XTest)

    accuracy = model.score(XTest,yTest)
    accuracy *= 100.0

    print('\nTest Accuracy: %.2f' % accuracy)
   
#================ Part 5 ============================
    #  Since the model we are training is a linear SVM, we can inspect the
    #  weights learned by the model to understand better how it is determining
    #  whether an email is spam or not. The following code finds the words with
    #  the highest weights in the classifier. Informally, the classifier
    #  'thinks' that these words are the most likely indicators of spam.
    

    print('\nTop spam predictors (keywords) \n')

    z = model.coef_
    z = numpy.ravel(z)

    vocabList = getVocabList.getVocabList()

    dic = {}
    for i in range(len(z)) :
        dic[ vocabList[i] ] = z[i]

    cnt = 0
    for w in sorted(dic, key=dic.get, reverse=True):
      if cnt == 15 :
          break 
      cnt = cnt + 1
      print('{0:10} - {1:10f}'.format(w, dic[w]))

    print('\n\n')

# ============ Part 6: Test a sample Email =====================
    #  Now that we have trained the spam classifier, we can use it on our own
    #  emails! 
    #  The following code reads in one of these emails and then uses our 
    #  learned SVM classifier to determine whether the email is Spam or 
    #  Not Spam
    
    f = open(os.path.join(path, "spamSample1.txt"),'r')
    email_contents = f.read()
    f.close() 

    print('Sample Email : ')
    print(email_contents)

    word_indices = processEmail.processEmail(email_contents)
    
    features = emailFeatures(word_indices)
    X = emailFeatures(word_indices);
    
    p = model.predict(X)

    print('\nEmail Processed\n\nSpam Classification: %d\n' % p);
    print('(1 indicates spam, 0 indicates not spam)\n\n');



if __name__  == "__main__" :
    main()

