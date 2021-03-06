# CitaNeg
Project developped during an intership at Laboratoire d'Informatique Gaspard Monge. This work is connected to the research project Cita&amp;Re.



# README

## Part I. buildingDataset

### DESCRIPTION:

This code contains ten scripts.
- dataset.py
- readerAthar.py
- readerCFC.py
- readerConcit.py
- readerIMS.py
- readerDFKI.py
- readerLiu.py
- readerXML.py
- seekCitationsText.py
- main.py


### FUNCTION:

The function of the scripts is twofold: 
- to pre-process individual datasets to retrieve citation contexts and their respective metadata;
- to create a new dataset combining all the individual datasets.


### HOW TO USE THE SCRIPTS:

- Download the folder BuildingDataset.
- Download the  corresponding subsets to create the new corpus (Teufel et al., 2006; Athar, 2011; Dong & Schäfer, 2011; Jochim & Schütze, 2012; Hernández-Alvárez, 2015; Liu, 2017). It is possible to use other subset with a few adjustments in the script.
- Each subset should be in their respective folder; the  folder must have the same name as the subset (ATHAR, DFKI, LIU, CFC, IMS, Concit). In case of including different subsets, use the same procedure.
- To run the code, when using Linux, type the command line: 

python3 main.py path_to_the_orignal_datasets path_to_the_results_folder 
 
### HOW TO ADD NEW DATASETS:

To create a new dataset using other individual subsets, follow the steps below:
- add the new individual subset to the folder where the other subsets are located.
Modifications to the script:
- create a new class of the type "reader"; the new class could be called "readerNewSubsetName";
- if the new subset to be added is in txt/csv format, follow the sytle of the classes "readerAthar", "readerDFKI" and "readerDFKI"; if the new subset in in xml format, follow the style of the classes "readerConcit", "readerIMS" and "readerCFC"; 
- if the new subset presents a different format (for example, json), adapt the code to treat this respective format; (XML readers can be a good source of inspiration as they also treat structured data)
- it is possible to add a <cite></cite> tag to the citation; if citations are not annotated and regular expressions are necessary to find them, use the class seekCitationsText;  
- modifications to the main code (add the lines below):
	from readerNewSubsettName import *
	NewSubsetName = NewSubsetNameReader()
	citanegDataset.append (NewSubsetName.read (os.path.join(input_folder,'NewSubsetName')))

### RESULTS:

The script produces 5 files:
- citaneg_untrimmed.csv: dataset containing all citation contexts, including repetitions (before data cleaning)
- citaneg.csv: dataset containing all citaion contexts but without repetitions (after data cleaning)
- citaneg_by_len.csv: dataset containing all citaion contexts but without repetitions (after data cleaning) and selected according to the length (contexts that have between 30 and 550 characters); the length of contexts can be changed
- citaneg_mul_pol.csv: contexts that present multiple polarities (i.e. multiple labels)
- duplicates.txt: file containing the repeated contexts


-------------------------------------------------------------------------------------------------------------------------------------------


## part II. preProcessingDataset

These scripts represent an intermediate phase. It involves two independent scripts:

1. first_stats.py
This script calculates the percentage of contexts containing a negative citation for each subset and in total. To run this code, use the path to the dataset file to be analyzed and the path to the resulting file, adding the name of the last one. The command line is the following:

			python3 first_stats path_to_the_dataset_file path_to_the_resulting_file_including_its_name
### Result
- A csv file containing the results of the statistical analysis.
It is necessary to run the script for every dataset that you want to have analyzed.

2. selecting1000.py
This script produces a training dataset and a testing dataset. Tre training dataset contains 500 "negative" contexts and 500 "other" contexts. The testing dataset contains the remaining "negative" contexts and the same amount of "other" contexts. To run this code, use the path to the dataset file to be treated (it is recommended to use the CitaNeg dataset without duplicates and whose context lengths range from 30 to 550), the path to the resulting file (training_dataset), and the path to the resulting file (testing_dataset) adding the name of the last ones. The command line is the following:

		python3 selecting1000 path_to_the_dataset_file path_to_the_result_file_training_dataset path_to_the_result_file_testing_dataset

### Result
- training dataset: a csv file containing 1000 contexts (500 negative and 500 other).
- testing dataset: a csv file containing X contexts (the remaining negative contexts and the same amount of "other" contexts). 

3. adaptingCitaneg.py
This script transforms each citation context into a single .txt file and stores all these files in a folder. To run the script, use the path to the dataset file to be treated and the path to where the resulting folder should be stored. It is recommended to store it at the same location as the code to analyze the contexts (part III). The command line is the following:

			python3 adaptingCitaneg.py path_to_the_dataset_file path_to_the_resulting_folder

### Result
- a folder containing txt files (as amny files as there are contexts).


-------------------------------------------------------------------------------------------------------------------------------------------


## Part III - analyzingDataset

1. download the scripts:
- pipeline.py
- runningStanza.py 
- analyzingDataset (folder)

2. download the file specificities.csv (specificity score found using the software TXM)

3. create a folder to store the results obtained at this phase

4. Download Stanza if you have not done it yet. (See references below).


### HOW TO USE THE SCRIPTS:

1. pipeline.py
This script calls the two python codes below (running_stanza.py and analyzingDataset)
It is the only code you need to call; however, it is possible to call analyzingDataset separately, in case the contexts have already been parsed by Stanza.
To call the pipeline.py code, you will need the following paths:
(a) path to the folder where the script running_stanza.py is stored;
(b) path to the folder where the folder with contexts for parsing is stored (this folder is the result of the adaptingDataset.py script presented in Part II of this document);
(c) path to the folder where the parsed contexts will be stored;
(c) path to the folder of the analyzingDataset package;
(d) path to the folder where the results will be stored;
(e) path to the folder where the results for WEKA will be stored;
(g) path to folder where the dataset csv file is located (the dataset used in csv format);
(h) path to the specificites.csv file.

The command line is:

		python3 pipeline.py (a) (b) (c) (d) (e) (f) (g) (h) 

2. running_stanza.py
This script uses the software stanza to parse the contexts. TO use it, it is necessary to have the software installed. The code takes as input the folder that contains the txt files (1 context per file). The output is a folder that contains the parsed contexts (json format).

3. analyzingDataset


### FUNCTION
The function of the script is twofold:
- to identify features and apply rules to the contexts;
- to evaluate the results regarding precision, recall anf F score.


### DESCRIPTION 
The script to analyze the CitaNeg dataset comprises the following:
- 7 different codes, being three classes, two function modules and a main code.
It should be noted that the code stores the traits, features and rules as boolean functions that are stored conveniently into corresponding dictionaries. This allows applying individually each rule using its key in the corresponding dictionary.
This approach allowed minimising the number of classes that would have had a single method.

The codes are:

1. token.py
This code (class Token) stores the tokens that come from the Stanza parsed files.

2. contexts.py
This code (class Context) reads each Stanza parsed file, identifies the tokens, counts how many sentences there are in the context and verifies the presence of a citation.

3. features_module.py
This module presents a collection of functions to identify different negative features present in the contexts. The presence of the features is indicated by a boolean.

4. rules_module.py
This module presents a collection of functions to identify the patterns that constitute the different rules. The presence of the rule patters is indicated by a boolean.

5. newFeatures.py
This module create a function that creates functions. It turns each word from the specifities file into a new feature. This module can be used to add other kinds of features (e.g. list of regex, list of n-grams, etc.).

6. evaluator.py
This function (class Evaluator) stores the results from the features and rules modules in a dictionary which takes the id of the context as key. Also, the text of the context and the original polarity, both coming from the CitaNeg dataset file, are stored in this dictionary. The text of the context is useful to analyze the rules result and the original polarity to verify precision and recall.
This class also applies the rules and features and evaluates their results (result of a single rule/feature). 
Finally, the class exports the results under csv format.

7. main.py
The main code opens the directory where the Talismane parsed files are stored. It allows to apply the features/rules and evaluate them by calling the class Evaluator.


### HOW TO USE THE SCRIPT
The script takes three inputs and produces three outputs.
(a) input 1: directory with the Stanza parsed files
(b) input 2: CitaNeg dataset (csv file)
(c) input 3: a file with specificic scores produced by the software TXM (csv file)
(d) output: results table in two versions, rules and features (csv files)
(e) output: results file adapted for WEKA (csv file)

It is possible to use the scripts independently, if the contexts have already been parsed. In other words, this package can be used without the pipeline.py. Use the command line below and the path to the respective folders/files:

		python3 main.py (a) (d) (e) (b) (c)


### HOW TO ADD NEW RULES OR FEATURES
To add new rules, traits or features:
- create a new function for the rule or trait in the rule_module class and/or the new feature in the feature_module class;
- add the name of the new rule, trait or feature to the dictionary (identifier of the rule/feature as dict key and name of the function as dict value) at the end of the respective model;
- modify the main code: add the new rule, trait or feacture to the respective list in the main code (rule_index, trait_index, feature_index).



-------------------------------------------------------------------------------------------------------------------------------------------

## REFERENCES:

1. Corpus CFC
S.Teufel, A.Siddharthan, D.Tidhar. (2006). Automatic classification of citation function. Proceedings of EMNLP-06, Sydney, Australia, 103-110.
Dataset available at : https://www.cl.cam.ac.uk/~sht25/CFC.html 

2. Corpus DFKI
Dong, C., Schäfer, U. (2011). Ensemble-style Self-training on Citation Classification. Proceedings of the 5th International Joint Conference on Natural Language Processing, 623–631.
Dataset available at : https://aclbib.opendfki.de/repos/trunk/citation_classification_dataset/ 

3. Corpus Athar
Athar, Awais.(2011. Sentiment Analysis of Citations using Sentence Structure-Based Features. Proceedings of the ACL 2011 Student Session, Portland, OR, USA, 81-87.
Dataset available at : https://cl.awaisathar.com/citation-sentiment-corpus/ 

4. Corpus IMS
Charles Jochim, Hinrich Schütze (2012). Towards a Generic and Flexible Citation Classifier Based on a Faceted Classification Scheme. Proceedings of the 24th International Conference on Computational Linguistics (COLING 2012). 
Dataset available at : https://www.ims.uni-stuttgart.de/en/research/resources/corpora/ims-citation-corpus/ 

5. Corpus CONCIT
Hernández Álvarez, M. (2015). Concit-Corpus : Context Citation Analysis to learn Function, Polarity and Influence.
Dataset available at : https://rua.ua.es/dspace/handle/10045/47416 

6. Corpus Liu
Liu, Haixia. (2017).Sentiment Analysis of Citations Using Word2vec.
Dataset available at : https://github.com/liuhaixiachina/Sentiment-Analysis-of-Citations-Using-Word2vec/blob/master/data/foreval/sentiment-012.csv

7. Stanza NLP
Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason Bolton and Christopher D. Manning. 2020. Stanza: A Python Natural Language Processing Toolkit for Many Human Languages. In Association for Computational Linguistics (ACL) System Demonstrations. 2020. 
Stanza NLP available at: https://stanfordnlp.github.io/stanza/

8. TXM
Heiden, S. (2010b). The TXM Platform: Building Open-Source Textual Analysis Software Compatible with the TEI Encoding Scheme. In Ryo Otoguro, Kiyoshi Ishikawa, Hiroshi Umemoto, Kei Yoshimoto, Yasunari Harada (Ed.), 24th Pacific Asia Conference on Language, Information and Computation - PACLIC24 (p. 389-398). Institute for Digital Enhancement of Cognitive Development, Waseda University, Sendai, Japan. 
TXM available at: http://textometrie.ens-lyon.fr/?lang=en
