"""
@author: rishabsaraf93
"""
import re
import getVocabList

from stemming.porter2 import stem


def processEmail(email_contents = "") :
    """
    processes the email body to return the email in its root form
    """

    vocabList = getVocabList.getVocabList()
    word_indices = []

# ========================== Preprocess Email ===========================

    # Find the Headers ( \n\n and remove )
    # Uncomment the following lines if you are working with raw emails with
    # the full headers

    email_contents = str(email_contents)

    # Lower case
    email_contents = email_contents.lower()

    # Strip all HTML
    # Looks for any expression that starts with < and ends with > and replace
    # and does not have any < or > in the tag it with a space

    email_contents = re.sub('<[^<>]+>',' ', email_contents)


    # Handle Numbers
    # Look for one or more characters between 0-9
    # email_contents = regexprep(email_contents, '[0-9]+', 'number');

    email_contents = re.sub('[0-9]+','number', email_contents)

    # Handle URLS
    # Look for strings starting with http:// or https://

    email_contents = re.sub('(http|https)://[^\s]*','httpaddr', email_contents)

    # Handle Email Addresses
    # Look for strings with @ in the middle

    email_contents = re.sub('[^\s]+@[^\s]+','emailaddr', email_contents)

    # Handle $ sign

    email_contents = re.sub('[$]+','dollar', email_contents)

# ========================== Tokenize Email ===========================

    # Output the email to screen as well
   
    delimiters = ' ' , '@' ,' $', '|', '/', '#', '.', '-' ,':' ,'&', '*', '+', '=', '[', ']', '?',\
                 '!', '(', ')', '{', '}', ',' , "'", '"', '>', '_' ,'<', '|', ';' ,'%' , "\n", "\t"     

    regexPattern = '|'.join(map(re.escape, delimiters))

    dic = re.split(regexPattern, email_contents)
  
    for i in range (len(dic)) :
        if len(dic[i]) > 0 :
            
            dic[i] = re.sub('[^a-zA-Z0-9]', '', dic[i])
            dic[i] = stem(dic[i])

            for j in range (len(vocabList)):
                if dic[i] == vocabList[j] :
                    word_indices.append(j)
 
    return word_indices
