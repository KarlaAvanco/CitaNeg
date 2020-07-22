from readerXML import *
from xml.dom import minidom


concitPaper = {
"A Fully Coreference-annotated Corpus of Scholarly Papers from the ACL Anthology.xml":"C12-2103",
"AccurateArgumentativeZoningwithMaximumEntropymodels.txt.xml":"W09-3603",
"AccurateInformationExtractionfromResearchPapersusingConditionalRandomFields.xml.xml":"N04-1042",
"Acoherencemodelbasedonsyntacticpatterns.txt.xml":"D12-1106",
"Adiscoursedrivencontentmodelforsummarisingscientificarticlesevaluatedinacomplexquestionansweringtask.txt.xml":"D13-1070",
"AHierarchical ClassifierApplied toMulti-way SentimentDetection.xml.xml":"C10-1008",
"AMaximumEntropyApproachtoNaturalLanguageProcessing.xml.xml":"J96-1002",
"AnalysisofSemanticClassesinMedicalTextforQuestionAnswering.txt.xml":"W04-0509",
"AnAnnotationSchemeforaRhetoricalAnalysisofBiologyArticles.txt.xml":"L04-1294",
"Anannotationschemeforcitationfunction.txt.xml":"W06-1312",
"AnAnnotationSchemeForInformationStatusInDialogue.xml.xml":"L04-1402",
"AnnotatingSemanticRelationsCombiningFactsAndOpinions.xml.xml":"W09-3027",
"AnnotationsforOpinionMiningEvaluationintheIndustrialContextofthe DOXAprojec.txt.xml":"L10-1290",
"AreTheseDocumentsWrittenfromDifferentPerspectives.txt.xml":"P06-1133",
"AssigningPolarityScorestoReviewsUsingMachineLearningTechniques.txt[No Cites].xml":"I05-1028",
"ASupervisedApproachforSentimentAnalysisusingSkipgrams.txt.xml":"W14-6904",
"Athreewayperspectiveonscientificdiscourseannotationforknowledgeextraction.txt.xml":"W12-4305",
"AutomaticDetectionofOpinionBearingWordsandSentences.txt.xml":"I05-2011",
"AutomaticExtractionofCitationContextsforResearchPaperSummarizationACoreferencechainbasedApproach.txt.xml":"W09-3611",
"AutomaticIdentificationofSentimentVocabularyExploitingLowAssociationwithKnownSentimentTerms.txt.xml":"W05-0408",
"BilingualSentenceAlignmentofaParallelCorpusbyUsingEnglishasaPivotLanguage.txt.xml":"W14-6902",
"CamtologyIntelligentInformationAccessforScience.txt.xml":"N10-2001",
"CoherentCitationBasedSummarizationofScientific Papers.txt.xml":"P11-1051",
"ContextEnhancedCitationSentimentDetection.txt.xml":"N12-1073",
"ContextEnhancedPersonalizedSocialSummarization.txt.xml":"C12-1075",
"CorpusandMethodforIdentifyingCitationsinNon-AcademicText.xml.xml":"L14-1027",
"Corpusannotationmethodologyforcitationclassificationinscientificliterature.txt.xml":"W14-6901",
"CoTrainingfor CrossLingualSentimentClassification.txt.xml":"P09-1027",
"DeeperSentimentAnalysisUsingMachineTranslationTechnology.txt.xml":"C04-1071",
"DetectionOfAgreementvsDisagreementInMeetingsTrainingWithUnlabeledData.xml.xml":"N03-2012",
"DetectionofImplicitCitationsforSentimentDetection.txt.xml":"W12-4303",
"DeterminingtheSentimentofOpinions.txt.xml":"C04-1200",
"DiscourseAnnotationWorkingGroupReport.txt.xml":"W07-1530",
"Discourselevelargumentationinscientificarticleshumanandautomaticannotation.txt.xml":"W99-0311",
"DiscourseLevelExplanatoryRelationExtractionfromProductReviewsUsingFirstOrderLogic.xml.xml":"D13-1097",
"DiscoveringtheDiscriminativeViewsMeasuringTermWeightsforSentimentAnalysis.txt.xml":"P09-1029",
"EfficientSupporVectorClassifiersforNamedEntityRecognition.xml.xml":"C02-1054",
"EmotionDetectionfromtextASurvey.txt.xml":" W14-6905",
"EmotionsfromTextMachineLearningforTextbasedEmotionPrediction.txt.xml":"H05-1073",
"ExaminingtheRoleofLinguisticKnowledgeSourcesin theAutomaticIdentificationandClassificationofReviews.txt.xml":"P06-2079",
"ExplorationsinAutomaticBookSummarization.txt.xml":"D07-1040",
"ExtractingAppraisalExpressions.txt.xml":"N07-1039",
"Extractingglossarysentencesfrom scholarlyarticles.txt.xml":"W12-3206",
"ExtractingProductFeaturesandOpinionsfromReviews.txt.xml":"H05-1043",
"FeatureSubsumptionfoOpinionAnalysis.txt.xml":"W06-1652",
"GeneralizedExpectationCriteriaforSemisupervisedLearningofConditionalRandomFields.xml.xml":"P08-1099",
"GetoutthevoteDeterminingsupportoroppositionfromCongressionalfloordebatetranscripts.xml.xml":"W06-1639",
"GraphBasedMultiTweetSummarizationusingSocialSignals.txt.xml":"C12-1104",
"GraphBasedMultiTweetSummarizationusingSocialSignals.txt_1.xml":"C12-1104",
"GuidingSemiSupervisionwithConstraintDrivenLearning.xml.xml":"P07-1036",
"IdentifyingAgreementandDisagreementinConversationalSpeechUseofBayesianNetworkstoModelPragmaticDependencies.xml.xml":"P04-1085",
"IdentifyingClaimedKnowledgeUdatesinBiomedicalResearchArticles.txt.xml":"W12-4302",
"IdentifyingInfluentialMembersoftheUSSenateUsingLexicalCentrality.txt.xml":"D07-1069",
"IdentifyingNonExplicitCitingSentencesforCitationBasedSummarization.txt.xml":"P10-1057",
"IdentifyingSectionsinScientificAbstractsusingConditionalRandomFields.xml.xml":"I08-1050",
"IdentifyingSourcesofOpinionswithConditionalRandomFieldsandExtractionPatterns.txt.xml":"H05-1045",
"IdentifyingtheEpistemicValueofDiscourseSegmentsinBiologyTextsprojectabstract.xml.xml":"W09-3742",
"ImprovedInformationStructureAnalysisofScientificDocumentsThroughDiscourseandLexicalConstraints.xml.xml":"N13-1113",
"ImprovedTextCategorisationForWikipediaNamedEntities.xml.xml":"U09-1015",
"IsUnlabeledDataSuitableForMulticlassSVM-basedWebPageClassification.xml.xml":"W09-2204",
"LanguageModelAdaptationforStatisticalMachineTranslationBasedonInformationRetrieval.xml.xml":"L04-1212",
"LanguageTechnologiesforSuicidePreventioninSocialMedia.xml":"W14-6903",
"Learning to Shift the Polarity of Words for Sentiment Classification.txt.xml":"I08-1039",
"LearningDependency-BasedCompositionalSemantics.xml.xml":"J13-2005",
"LearningExtractionPatternsforSubjectiveExpressions.txt.xml":"W03-1014",
"LearningFromCollectiveHumanBehaviortoIntroduceDiversityinLexicalChoice.txt.xml":"P11-1110",
"LearningSubjectiveLanguage.txt.xml":"J04-3002",
"Learningsubjectivenounsusingextractionpatternbootstrapping.txt.xml":"W03-0404",
"LearningtoClassifyEmailintoSpeechActs.txt.xml":"W04-3240",
"MakingHiddenMarkovModelsMoreTransparent.xml.xml":"W05-0106",
"Medstract-TheNextGeneration.xml.xml":"W11-0224",
"MetaKnowledgeAnnotationofBioEvents.txt.xml":"L10-1210",
"MethodMentionExtractionfromScientificResearchPapers.xml.xml":"C12-1074",
"ModelingCategoryStructuresWithAKernelFunction.xml.xml":"W04-2408",
"MorethanWords_SyntacticPackagingandImplicitSentiment.xml.xml":"N09-1057",
"OpinionGraphsforPolarityandDiscourseClassification.xml.xml":"W09-3210",
"PurposeandPolarityofCitationTowardsNLPbasedBibliometrics.txt.xml":"N13-1067",
"RediscoveringACLDiscoveriesThroughtheLensofACLAnthologyNetworkCitingSentences.txt.xml":"W12-3201",
"ReferenceScopeIdentificationinCitingSentences.txt.xml":"N12-1009",
"SeeingStarsExploitingClassRelationshipsforSentimentCategorizationwithRespectto RatingScales.txt.xml":"P05-1015",
"SummarisingLegalTextsSententialtenseandArgumentative Roles.txt.xml":"W03-0505",
"TheSentimentalFactorImprovingReviewClassificationviaHumanProvidedInformation.txt.xml":"P04-1034",
"ThumbsupSentimentClassificationusingMachineLearningTechniques.txt.xml":"W02-1011",
"TimestampedGraphsEvolutionaryModelsofTextfor MultiDocumentSummarization.txt.xml":"W07-0204",
"TopicwiseSentimentwiseorOtherwiseIdentifyingtheHiddenDimensionforUnsupervisedTextClassification.txt.xml":"D09-1061",
"WeaklySupervisedLearningforHedgeClassificationinScientificLiterature.xml.xml":"P07-1125"
}

class concitReader (XMLreader): # Class to processes the concit dataset.
                                # Dataset format: xml
                                # Size: 1 folder with multiple files
    
    def __init__ (self):
        self.paperIdFromPath = {}
    
    def getFilesList (self, path):
        return_list = []
        list_of_file_names = list(concitPaper.keys())
        for filename in list_of_file_names:
            complete_path_name = os.path.join(path,filename)
            return_list.append (complete_path_name)
            #create a copy dictionary from complete path to save time 
            #looking for paper_ID
            self.paperIdFromPath [complete_path_name] = concitPaper[filename]
        return return_list

    def getPaperId (self, node):
    # This function processes the Concit dataset.
    # Treatment: get a paper id
    # The function takes one parameter: a xml node.
    # See getFilesList to see how PaperIdFromPath is built

        paper_Id_text = self.paperIdFromPath[self.current_file_name]
        return paper_Id_text
    
    #The following functions get the lables specific to the Concit dataset
    def getDataSourceName (self):
        return 'Concit'

    # focus on <context>
    def getContextTag (self):
        return 'context'

    # focus on <cite id="2" function="ack" polarity="pos">Light et al. (2004)</cite>
    def getCitationTag (self):
        return 'cite'

    def getOriginalLabelTag (self):
        return "polarity" 

    def getContextIdTag (self):
        return "id"

    def isNegativePolarity (self, label):
        return label == "neg" 
        
    