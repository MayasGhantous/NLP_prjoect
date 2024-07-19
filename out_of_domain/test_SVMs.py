from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from calculate_real_data import get_the_error_feature,get_the_function_words_feature,get_the_Unigram_feature
from calculate_real_data import get_the_sentence_length_feature, get_trigram_Feature,get_the_grammer_feature
from calculate_real_data import get_pos_trigram,get_CharTrigram_Tokens_Unigram_Spelling_Feature, get_Function_words_Pos_Trigram_Sentence_length_Feature
from calculate_real_data import get_grammer_spelling_features
from classification import create_NLI,create_binary,cereate_family,MODELS_LOCATION
import pandas as pd
from scipy.sparse import csr_matrix
from imblearn.under_sampling import RandomUnderSampler
import pickle