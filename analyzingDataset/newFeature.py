from context import *
from evaluator import * 
import csv

def getWordsList (input_file):

    words_list = []

    with open(input_file, mode='r') as specificities_file:
            reader = csv.reader(specificities_file, delimiter=';')
            next(reader)
            for row in reader:

                if float(row[3]) >=2.0 and float(row[2]) >= 10.0: # get words whose specificity score is higher than 2.0 and whose
                    words_list.append(row[0])						# frequency is higher than 10



    #to be completed 
    return words_list

#We create a function that can create functions 
#createWordFormSearcher returns a function that will search in a context for a specific word form
#It can be called as many times as needed to create such functions and changing the word form that is sought
def createWordFormSearcher (word_form_searched):
    #declare the returned function 
    #note that the function only takes a context as a parameter. 
    #The word_form_searched is stored in the newly created function (closure)
    def searcher (context):
        for sentence in context.sentences:
            for token in sentence:
                if token.wordForm == word_form_searched :  
                    return '1'
        return '0'

    #and return it
    return searcher



