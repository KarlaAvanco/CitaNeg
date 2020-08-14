from token import *
import os

class Context ():

    def __init__ (self, file):
        
        self.token_list = []
        self.number_of_sentences = 0
        self.presence_of_citation = False
        
        file_name = os.path.basename(file) # use the file name to recover the id
        split_file_name = file_name.split('-')
        #current_context['id'] = split_file_name[0]+'-'+split_file_name[1]
        # alternative = have an id variqable
        context_id = split_file_name[0]+'-'+split_file_name[1]
        self.id = context_id
        

        with open (file, 'r', encoding='utf-8') as working_file:
         
            for line in working_file: # Reading the lines in the parsed file
                line=line.rstrip("\n")
            
                if line == '':  # Identify the contexts that have multiple sentences
                    self.number_of_sentences +=1
               
                t=line.split("\t")  # split the lines in the columns 
                if len(t)==10: 

                    token = Token() 
                
                    token.index = t[0]
                    token.wordForm = t[1]
                    token.lemma = t[2] 
                    if token.lemma == '_': # When the parser does not recognizes the form, the lemma is presented as "_"
                        token.lemma = t[1] # In such cases, we replace the lemma par le form
                    else:
                        token.lemma = t[2]
                    #token['token_lemma']  = token_lemma == je n'en ai plus besoin
                    token.pos = t[3]
                    token.feature = t[5]
                    token.governor = t[6]
                    token.dependency = t[7]

                    self.token_list.append(token)

                    if token.wordForm =='CITATION': # Identify if there is a citation in the contexts 
                        self.presence_of_citation = True




