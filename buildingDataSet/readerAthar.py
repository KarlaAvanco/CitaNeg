import glob
import re

class atharReader ():
    def read (self, path):
    # This function processes the Athar dataset.
    # Dataset format: txt
    # Size: 1 single file
    # The function takes one parameter: a path to a folder containing a .txt file.
    
        context_list = []

        for concrete_file in glob.glob(path):  
            with open (concrete_file) as file:       # Open the data set file
                for line in file:
                    if re.search(r'^\w', line):              # Exclude the first lines which contain metadata
                        dataset = {}                        # Empty dictionary to store the data
                        tokenized_line = line.split('\t')   # Tokenize the lines to find and store the different information
                        dataset['dataSource'] = 'Athar'
                        dataset['contextID'] = tokenized_line[0].strip()
                        dataset['paperID'] = tokenized_line[1].strip()
                        dataset['citeContext'] = tokenized_line[3].strip()
                        dataset['originalLabel'] = tokenized_line[2].strip()
                        if dataset['originalLabel'] == 'n':    
                            dataset['polarity'] = "1"       # Create a new label for polarity
                        else:
                            dataset['polarity'] = "0"
                        
                        context_list.append(dataset)

        return (context_list, [])

           