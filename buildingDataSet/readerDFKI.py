import glob
import re

class dfkiReader():
    def read (self,path):
    # This function processes the DFKI dataset.
    # Dataset format: txt
    # Size: 1 folder with 3 files
    # Treatment: produce a context id
    # The function takes one parameter: a path to a folder containing .txt files.
   
        context_list = []    
        previousID = ""
        repeat_counter = 1
        
        for concrete_file in glob.glob(path): 
            with open (concrete_file, 'r', encoding='latin-1') as input_file:
                for line in input_file:
                    dataset = {}                       # Empty dictionary to store the data
                    tokenized_line = line.split('\t')  # Tokenize the lines to find and store the different information
                    dataset['dataSource'] = 'DFKI'
                    cite = tokenized_line[0].strip() # Create a context id
                    if  cite == previousID:
                        repeat_counter += 1
                    else:
                        repeat_counter = 1
                    dataset['contextID'] = cite+'_'+str(repeat_counter)
                    dataset['paperID'] = cite.split('_')[0]
                    previousID = cite
                    textContext = tokenized_line[1].strip()
                    if re.findall(r'\( \)', textContext): # identify the citations
                        citeContext=re.sub('\( \)', '<cite>( )</cite>', textContext) # add the <cite> and </cite> tags around the citation
                    dataset['citeContext'] = citeContext
                    dataset['originalLabel'] = tokenized_line[5].strip()
                    if not dataset['originalLabel'] == "NULL": # exclude the contexts whose polarity is NULL
                        if dataset['originalLabel'] == 'Negative':
                            dataset['polarity'] = "1"       # Create a new label for polarity
                        else:
                            dataset['polarity'] = "0"
                                    
                        context_list.append(dataset)
        
        return (context_list, [])
