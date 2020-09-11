from token import *
import os
import json


# Exemple of a Talismane parsed file:
# Each file presents 10 columns 



class Context ():

    def __init__ (self, file):
        
        self.sentences = []
        self.number_of_sentences = 0
        self.presence_of_citation = False
        
        file_name = os.path.basename(file) # use the file name to recover the id
        split_file_name = file_name.split('-')
        #current_context['id'] = split_file_name[0]+'-'+split_file_name[1]
        # alternative = have an id variqable
        context_id = split_file_name[0]+'-'+split_file_name[1]
        self.id = context_id
        

        with open (file, 'r', encoding='utf-8') as working_file:
            stanza_doc = json.load (working_file)

            self.number_of_sentences = len(stanza_doc)
            for sentence in stanza_doc:
                stored_sentence = []
                for stanza_token in sentence:              

                    token = Token() 
                
                    token.index = stanza_token['id']
                    token.wordForm = stanza_token['text']
                    token.lemma = stanza_token['lemma'] 
                    token.pos = stanza_token['xpos']
                    token.upos = stanza_token['upos']
                    if 'feats' in stanza_token:
                        token.feature = stanza_token['feats']
                    token.governor = stanza_token['head']
                    token.dependency = stanza_token['deprel']

                    stored_sentence.append(token)

                    if token.wordForm =='CITATION': # Identify if there is a citation in the contexts 
                        self.presence_of_citation = True
                self.sentences.append (stored_sentence)




