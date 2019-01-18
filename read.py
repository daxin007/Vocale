import numpy as np
import os


# Define our example directories and files

PATH = os.getcwd()

def getDatafile(file_dir):

	test_list = []
	test_label = [] 
	valide_list = []
	valide_label = []
	train_list = []
	train_label = []
	#定义存放各类别数据和对应标签的列表，列表名对应你所需要分类的列别名

	file_list = []   #liste des files de wav
	dic_list = [] # dictionnaire de base des données
	path_list=os.listdir(file_dir)

	for wav_dir in path_list:
		name = wav_dir.split(sep='.')
		if(len(name) == 1) :
			for wav in os.listdir(file_dir+'/'+wav_dir): 
				name_wav = wav.split(sep='.')
				if(len(name_wav) == 2 and name_wav[1] == 'wav' ):
					file_list.append(wav_dir+'/'+wav)
					if not(wav_dir in dic_list):
						dic_list.append(wav_dir)

	print(len(file_list))
	print(dic_list)

	index = {}
	for i in range(len(dic_list)):
		index[dic_list[i]] = i
	#Creates the reverse table that maps labels names to their index	
		
	print(index)

	for line in open('testing_list.txt','r'):
		test_list.append(line.strip('\n'))
		label = line.strip('\n').split(sep='/')[0]
		test_label.append(index[label])


	for line in open('validation_list.txt','r'):
		valide_list.append(line.strip('\n'))
		label = line.strip('\n').split(sep='/')[0]
		valide_label.append(index[label])


	for line in file_list:
		if not (line in test_list ):
			if not (line in valide_list):
				train_list.append(line)
				train_label.append(index[label])

	return index, train_list, train_label, valide_list, valide_label, test_list, test_label








