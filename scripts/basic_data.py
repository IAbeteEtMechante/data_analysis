import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from tqdm.auto import tqdm #Progress Bars
from collections import namedtuple
from datetime import datetime
warnings.filterwarnings(action="ignore")

def add_unix_time(df, time_string_col):
	"""
	input:df and a column name corresponding to the time as a STRING
	output:time column replaced with unix_time
	"""
	time_zero = pd.to_datetime('1970-01-01')
	df[time_string_col] = pd.to_datetime(df[time_string_col], errors='coerce')
	df = df.dropna(subset=[time_string_col])
	df[time_string_col] = pd.to_datetime(df[time_string_col]).apply(lambda x: int((x - time_zero).total_seconds()))
	return df

def ntuples(df):
	"""
	In a notebook, when I write var. and press Tab, the names of all the variables
	 in the dataframe df will be displayed. 
	 Writing var.variable_1 is equivalent to writing 'variable_1'. 
	 So the following would work: df[var.variable_1]
	"""
	list_of_names = df.columns.values
	list_of_names_dict = {x:x for x in list_of_names}

	Varnames = namedtuple('Varnames', list_of_names) 
	return Varnames(**list_of_names_dict)

def keyswithmaxval(d):
	""" a) create a list of the dict's keys and values; 
		 b) return the key with the max value"""  
	MAX = max(d.values())
	result = []
	for key in d.keys():
		if d[key] == MAX:
			result.append(key)
	return result

	 