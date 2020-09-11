import context
import re
import rules_module 

### Functions to identify the different features present in a negative context
    ### General features
            
  
## General feature 1 (GF1): number of sentences in the contexts 
def findingNumberOfSentences (context):
    
    if context.number_of_sentences > 1: 
       return '1' # store the contexts that have multiple sentences in a dictionary
    else:
        return '0'


## General feature 2 (GF2): presence of a real citation in the contexts 
def findingContextsWithCitations (context): 

    if context.presence_of_citation: 
       return '1'
    else:
        return '0'

## General feature 3 (GF3): presence of the adverb not
def findingNot (context): 
    
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'not':            
                return '1'
            
    return '0'

## General feature 4 (GF4): presence of the conjunction but
def findingBut (context): 
    
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'but':            
                return '1'
           
    return '0'

## General feature 5 (GF5): presence of however
def findingHowever (context): 
    
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'however':            
                return '1'
            
    return '0'

## General feature 6 (GF6): presence of the words lack, fail and failure and their synonyms (nouns and verbs)
def findingFail (context): 
    
    list_of_words = ['fail', 'lack', 'failure', 'deficit', 'deficiency', 'inadequacy', 'insufficiency', 'scantiness', 'scarceness', 'scarcity', 'shortage', 'malfunction']
   
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma in list_of_words:        
                return '1'
                
    return '0'

## General feature 7 (GF7): presence of the verb outperform 
def findingOutperform (context): 
    
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'outperform':            
                return '1'
            
    return '0'

## General feature 8 (GF8): verify if the citation is the subject of the sentence
def citationIsSuj (context): 

    for sentence in context.sentences:
        for token in sentence:
            if token.wordForm == 'CITATION' and token.dependency =='nsubj':       
                return '1'
            
    return '0'

## General feature 9 (GF9): verify if the the subject is first person
def SujIsFirstPerson (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.pos == "PRP" and token.dependency == 'nsubj': 
                if token.checkFeature('Person','1'):           
                    return '1'
            
    return '0'

## General feature 10 (GF10): verify if the subject is third person
def SujIsThirdPerson (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.pos == "PRP" and token.dependency == 'nsubj': 
                if token.checkFeature('Person','3'):           
                    return '1'
            
    return '0'

## General feature 11 (GF11): verify if the noun 'method' is in the context
def FindingMethod (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'method':
                return '1'
            
    return '0'

## General feature 12 (GF12): verify if the words 'model' and 'modeling' are in the context
def FindingModel (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'model' or token.lemma =='modeling':    
                return '1'
            
    return '0'

## General feature 13 (GF13): verify if the noun 'approach' is in the context
def FindingApproach (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'approach' or token.lemma =='strategy'  or token.lemma =='technique':     
                return '1'
            
    return '0'

## General feature 14 (GF14): verify if the noun 'result' is in the context
def FindingResult (context): 
    for sentence in context.sentences:
        for token in sentence:
            if token.lemma == 'result' or token.lemma =='outcome':  
                return '1'
            
    return '0'

            
   
features = {'GF1' : findingNumberOfSentences, 
            'GF2' : findingContextsWithCitations,
            'GF3' : findingNot,
            'GF4' : findingBut,
            'GF5' : findingHowever,
            'GF6' : findingFail,
            'GF7' : findingOutperform,
            'GF8' : citationIsSuj,
            'GF9' : SujIsFirstPerson,
            'GF10' : SujIsThirdPerson,
            'GF11' : FindingMethod,
            'GF12' : FindingModel,
            'GF13' : FindingApproach,
            'GF14' : FindingResult}