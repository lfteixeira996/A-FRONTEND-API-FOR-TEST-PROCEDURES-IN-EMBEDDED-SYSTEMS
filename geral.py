import os

#############################################################################################################################
#Function: 	createFile
#Parameter: test_file_path; temp_file_path
#Return:	None
#
#SSS:		ABHP-GERAL-010
#############################################################################################################################
def createFile(test_file_path, temp_file_path):

	#remove test even if exists
	os.system("rm -rf " + test_file_path);

	#open the template
	with open(temp_file_path) as fr:		
		with open(test_file_path, 'w') as fw:
			for line in fr:
				fw.write(line)	
#############################################################################################################################

#############################################################################################################################
#Function: 	writeInFile
#Parameter: test_file_path; lookup; message; update;
#Return:	None
#
#SSS:		ABHP-GERAL-020
#############################################################################################################################
def writeInFile(test_file_path, lookup, message, update):

	#open the file that will be updated
	f = open(test_file_path, 'r+')

	with f as fw:
		lines = fw.readlines()
		fw.seek(0)
		fw.truncate()
		for line in lines:
			if line.startswith(lookup):
				if update==True:
					line = line +"\n"+ message +"\n"	
				else:
					line =  message + "\n"						
			fw.write(line)
#############################################################################################################################

#############################################################################################################################
#Function: 	checkIfExists
#Parameter: test_file_path; message;
#Return:	None
#
#SSS:		ABHP-GERAL-030
#############################################################################################################################
def checkIfExists(test_file_path, message):
	
	#open the file that will be updated
	f = open(test_file_path, 'r+')
	
	#we need to be sure that we do not duplicate the construct
	exists = False
	with f as fr:
		lines = fr.readlines()
		for line in lines:
			if line.startswith(message):
				exists = True
				return exists	
	return exists
#############################################################################################################################

#############################################################################################################################
#Function: 	writeIfNoExists
#Parameter: lookup; message; test_file_path;
#Return:	None
#
#SSS:		ABHP-GERAL-040
#############################################################################################################################
def writeIfNoExists(lookup, message, test_file_path):	
	
	#we need to be sure that we do not duplicate the construct
	exists = checkIfExists(test_file_path, message)
	
	if exists == False:
		update = True
		writeInFile(test_file_path, lookup, message, update)
#############################################################################################################################
