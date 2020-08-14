import context

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


   ## General feature 3 (GF3): presence of the words lack, fail and failure and their synonyms (nouns and verbs)
def findingFail (context): 
    
    list_of_words = ['fail', 'lack', 'failure', 'deficit', 'deficiency', 'inadequancy', 'insufficiency', 'scantiness', 'scarceness', 'scarcity', 'shortage', 'malfunction']
   
    for token in context.token_list:
        if token.lemma in list_of_words:            
            return '1'
    
    return '0'


features = {'GF1' : findingNumberOfSentences, 
            'GF2' : findingContextsWithCitations,
            'GF3' : findingFail}