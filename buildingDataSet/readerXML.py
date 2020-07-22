import glob, os, re, sys, requests, csv
from xml.dom import minidom

# Helper functions -------------------------------------------------
#get text from nodes
def displayNodeText(node):
    if node.childNodes.length == 0:
        data = ""
        try: 
            data = node.data
        except:
            pass
        return data
    else:
        text=""
        for child in node.childNodes:
            text += displayNodeText(child)
        return text

# get the text without sequences of whitespaces
def cleanText(text):
   # start by removing line breaks
            table = text.split("\n")
            result = ""
            for line in table:
                line = re.sub ('\t','', line) # remove tabulation
                regex = "(.*) [ ]+(.*)"
                res = re.search(regex,line)
                while res:
                    line = res.group(1)+" "+res.group(2)
                    res = re.search(regex, line)
                result += line
            return result


#Main class (XML reader)----------------------------------------

class XMLreader ():
    def __init__ (self):
        # This function initializes the object attributes.
        # These attributes refer to the different tags used in each xml dataset.
        
        self.current_file_name = ''
        


    def read (self, path):
    #This function processes the datasets in xml format.
    #Treatment: verify if the contexts presents more than one polarity.
    #Contexts that have multiple polarities are stored in a different dataset.
    #The function takes one parameter: a path to a folder containing .xml files.
    
        context_list = []
        multiple_polarities_list = []
        
                
        # The file list contains all the path information (not only the filename,
        # but also the directory)
        file_list = self.getFilesList (path)
        for file in file_list: 
            self.current_file_name = file
            root_node = minidom.parse(file)
            #my_text = displayNodeText(root_node)
            #print(clean_text)

            # variable to store dataset source
            name_of_datasource = self.getDataSourceName ()
            
            # variable to get the paper id
            paperID = self.getPaperId (root_node)
            paper_Id_text = self.getPaperId (root_node)
                
            # variable to get the citations
            # the tag that represents the citation varies according to the different datasets
            contexts = root_node.getElementsByTagName(self.getContextTag ())
            # display the contexts
            for context in contexts:
                citations = context.getElementsByTagName(self.getCitationTag())
                citation_OK = True # boolean to check if the context contains a citation
                partial_list = [] # temporary list to store the contexts 
                has_multiple_polarities = False
                context_not_analysed_yet = True
                
                for each_citation in citations:
                    dataset = {} 
                    dataset['paperID'] = paper_Id_text # store the id of the paper in the dictionary
                    dataset['dataSource'] = name_of_datasource # store the name of the dataset source  in the dictionary
                    try:
                        originalLabel = each_citation.attributes[self.getOriginalLabelTag()].value
                        dataset['originalLabel'] = originalLabel # store the original label in the dictionary
                        
                        # treat the labels to obtain the polarities (0,1)
                        if self.isNegativePolarity (originalLabel): 
                            dataset['polarity'] ='1'
                        else:
                            dataset['polarity'] ='0'
                            
                        #verify if there are multiple polarities in a single context
                        if context_not_analysed_yet:
                            previous_polarity = dataset['polarity'] 
                            context_not_analysed_yet = False
                        if previous_polarity != dataset['polarity']:
                            has_multiple_polarities = True

                            previous_polarity = dataset['polarity']

                        # get the id of a citation
                        contextId = each_citation.attributes[self.getContextIdTag ()].value   
                        dataset['contextID'] = contextId

                        # get the text of each context
                        cleanedText = cleanText(displayNodeText(context))
                        dataset['citeContext'] = cleanedText
                        
                    except:
                        citation_OK = False
                        pass
            
                    if citations.length != 0 and citation_OK:
                        partial_list.append(dataset) # store the contexts that have multiple citations 
                
                if not has_multiple_polarities:
                    if len(partial_list) != 0 :
                        context_list.append (partial_list[0]) # store contexts that have a single polarity
                                                                # if there are multiple citations and onle a single polarity
                                                                # we retain the context once (when we obtain the first polarity)
                else:
                    multiple_polarities_list+=partial_list # store contexts that have multiple citations
                                                                # and multiple polarities in a different list
                                                                  # retain the contexts as many timaes as there are different polarities
        #returned_lists = {}
        #returned_lists['complete'] = context_list
        #returned_lists['multiple polarities'] = multiple_polarities_list
        #return returned_lists
        return (context_list, multiple_polarities_list)
    
   
            