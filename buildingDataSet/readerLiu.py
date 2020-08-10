import glob
import csv 
import re 
from seekCitationsInText import seekCitations

class liuReader ():
    def read (self, path):
    # This function processes the Liu dataset.
    # Dataset format: csv
    # Size: 1 single file   
    # The function takes one parameter: a  path to a folder containing a .csv file. 
    

        context_list = []

        for concrete_file in glob.glob(path):  
            with open(concrete_file) as csv_object: 
                csv_reader = csv.reader(csv_object, delimiter = ',') 
                next (csv_reader) # skip the first line (headers)
                for row in csv_reader:
                    dataset = {}                        # Empty dictionary to store the data
                    dataset['dataSource'] = 'Liu'
                    dataset['contextID'] = row[0]
                    dataset['paperID'] = "NA"
                    citeContext = re.sub('_comma_', ',',row[2])  # Replace the expression _comma_ par a real comma (,)
                    dataset['citeContext'] = seekCitations (citeContext)
                    #dataset['citeContext'] = citeContext
                    dataset['originalLabel'] = row[1]
                    if dataset['originalLabel'] == '0':
                        dataset['polarity'] = "1"       # Create a new label for polarity
                    else:
                        dataset['polarity'] = "0"
                    context_list.append(dataset)

        return (context_list, [])