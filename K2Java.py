#!/usr/bin/python
import sys
from os.path import join, dirname, abspath
import xlrd
import easygui as g 
import shutil
import xml.etree.ElementTree as ET
from shutil import copyfile
import os
import geral
import time

#############################################################################################################################
#Function: 	createConstructor
#Parameter: add; test_file_name; test_file_path;
#Return:	None
#
#SSS:		ABHP-APP-031
#############################################################################################################################
def createConstructor(add, test_file_name, test_file_path):

	lookup   = "public class "+test_file_name+" extends BaseTestSequence {\n"
	message  = "\tpublic "+add+" "+add+";"
	geral.writeIfNoExists(lookup, message, test_file_path)
	
	#add the initial condition
	lookup   = "\tpublic void initialCondition() throws TestError {"
	message  = "\t\t"+add+".init"+add+"();"
	geral.writeIfNoExists(lookup, message, test_file_path)
	
	#create object
	message  = "\t\t"+add+" = new "+add+"();"
	geral.writeIfNoExists(lookup, message, test_file_path)
#############################################################################################################################	
	
	
#############################################################################################################################
#Function: 	insertConstAndInit
#Parameter: xl_sheet; test_file_name; test_file_path;
#Return:	None
#
#SSS:		ABHP-APP-030
#############################################################################################################################
def insertConstAndInit(xl_sheet, test_file_name, test_file_path):

	num_cols = xl_sheet.ncols
	num_rows = xl_sheet.nrows  															
	
	# Iterate through columns index
	for col_idx in range(1, num_cols):    							

		if xl_sheet.cell_type(2, col_idx) == xlrd.XL_CELL_EMPTY:				#caso a primeira celula da coluna esteja vazia --> break
			break
		
		for row_idx in range(2, num_rows):  									# Iterate through rows
			cell_obj = xl_sheet.cell(row_idx, col_idx)  						# Get cell object by row, col

			if xl_sheet.cell_type(row_idx, col_idx) == xlrd.XL_CELL_EMPTY:		#caso a celula esteja vazia passa a proxima coluna
				break

			else:
				cell = xl_sheet.cell_value(row_idx, col_idx)
				f = open('./inputs/database/key_database.txt','r+')
				with f as file:	
					lines = file.readlines()
					for line in lines:
						if line.startswith(cell):
							data=line.split('.')
							add = data[len(data)-1]
							add = add.replace("\n", '')
							createConstructor(add, test_file_name, test_file_path)
#############################################################################################################################


#############################################################################################################################
#Function: 	createStepsList
#Parameter: test_file_path; number_steps;
#Return:	None
#
#SSS:		ABHP-APP-040
#############################################################################################################################
def createStepsList(test_file_path, number_steps):

	message = ""
	#create the message
	for i in range(1, number_steps+1):
		message = message + "\t\tstep{}();\n".format(i)

	lookup	= "\tpublic void executeTestcase() throws TestError {"
	update	= True  
	 
	geral.writeInFile(test_file_path, lookup, message, update);	
#############################################################################################################################


#############################################################################################################################
#Function: 	keywordExists
#Parameter: xl_sheet
#Return:	num_steps
#
#SSS:		ABHP-APP-010
#############################################################################################################################
def keywordExists(xl_sheet):

	num_cols = xl_sheet.ncols
	num_rows = xl_sheet.nrows  															
	num_steps = 0																#return the number os steps 

	# Iterate through columns index
	for col_idx in range(1, num_cols):    							

		if xl_sheet.cell_type(2, col_idx) == xlrd.XL_CELL_EMPTY:				#caso a primeira celula da coluna esteja vazia --> break
			break
		
		num_steps = num_steps +1

		for row_idx in range(2, num_rows):  									# Iterate through rows
			cell_obj = xl_sheet.cell(row_idx, col_idx)  						# Get cell object by row, col

			if xl_sheet.cell_type(row_idx, col_idx) == xlrd.XL_CELL_EMPTY:		#caso a celula esteja vazia passa a proxima coluna
				break

			else:
				cell = xl_sheet.cell_value(row_idx, col_idx)
				if cell in open("./inputs/database/key_database.txt").read():
					pass
				else: 
					g.msgbox("The keyword does not exist: "+str(cell), "Keyword Error")
					sys.exit()
	
	return num_steps
#############################################################################################################################


#############################################################################################################################
#Function: 	updateClassName
#Parameter: test_file_name; test_file_path;
#Return:	None
#
#SSS:		ABHP-APP-020
#############################################################################################################################
def updateClassName(test_file_name, test_file_path):
	
	lookup   = "public class TEMPLATE_JAVA extends BaseTestSequence {"
	message  = "public class "+test_file_name+" extends BaseTestSequence {\n"
	update 	 = False
	
	geral.writeInFile(test_file_path, lookup, message, update)
#############################################################################################################################


#############################################################################################################################
#Function: 	insertImports
#Parameter: cell; test_file_path;
#Return:	None
#
#SSS:		ABHP-APP-051
#############################################################################################################################
def insertImports(cell, test_file_path):

	file = open("./inputs/database/key_database.txt", 'r')
	package = "" 

	#Read the line that contain the keyword (in the same line we can see the package too "keyword\tpackage")
	#str_import contain the line with the correspondent keyword and package
	with file as fr:
		lines = fr.readlines()
		for line in lines:
			if line.startswith(cell):
				package=line.split("\t")
				break

	str_import = package[1].strip()
			
	#ADD the import to the java test						
	message   = "import "+str_import+";"
	
	#we need to be sure that we do not duplicate the import
	#if the java test already have the import nothing need to be done
	exists = geral.checkIfExists(test_file_path, message)

	if exists == False:
		lookup   	= "/*Standard and simops imports*/"	
		geral.writeInFile(test_file_path, lookup, message, True);
#############################################################################################################################


#############################################################################################################################
#Function: 	stepKeyword
#Parameter: xl_sheet; test_file_path; number_steps;
#Return:	None
#
#SSS:		ABHP-APP-050
#############################################################################################################################
def stepKeyword(xl_sheet, test_file_path, number_steps):

	#Starts to get all keywords
	num_rows = xl_sheet.nrows  
	num_cols = xl_sheet.ncols

	#create the message
	for current_step in range(1, number_steps+1, 1):

		keywords = []
		classes  = []
		
		col_idx = current_step		

		for row_idx in range(2, num_rows):  									# Iterate through rows
			cell_obj = xl_sheet.cell(row_idx, col_idx)  						# Get cell object by row, col	
			
			if xl_sheet.cell_type(row_idx, col_idx) == xlrd.XL_CELL_EMPTY:		#caso a celula esteja vazia passa a proxima coluna
				break

			else:
				cell = xl_sheet.cell_value(row_idx, col_idx)
				keywords.append(cell)
				f = open('./inputs/database/key_database.txt','r+')
				with f as file:	
					lines = file.readlines()
					for line in lines:
						if line.startswith(cell):
							data= line.split('.')
							add = data[len(data)-1]
							add = add.replace("\n", '')
							classes.append(add)
			
				
		fjava 			= open(test_file_path, 'r+')	
		msg_step 		= "\n\tpublic void step{}() throws TestError ".format(current_step) +"{\n\n"
		msg_printstep 	= "\t\tPrintLib.printStep(\"\");\n\n"
		msg_printact 	= "\t\tPrintLib.printActivity(\"\");\n"

		lookup   = "}"
	
		#write the steps in execTestCase
		with fjava as fr:
			lines = fr.readlines()
			fr.seek(0)
			fr.truncate()
			
			for line in lines:
				if line.startswith(lookup):
					new = msg_step + msg_printstep

					#add the keyword
					i = 1
					for words, word in zip(keywords,classes):
					
						msg_comment = "\t\t/* ----------------- Step {}".format(current_step) + " - Activity {}".format(i)+"---- */\n"
						new = new + msg_comment + msg_printact + "\t\t"+word+"."+words +"();\n\n" 
						i=i+1

					line = new + "\n\t}\n}"
				fr.write(line)


		for words in keywords:
		 	insertImports(cell, test_file_path)	
#############################################################################################################################


#############################################################################################################################
#Function: 	main
#Parameter: None
#Return:	None
#############################################################################################################################
def main():
	# Get the name of the test
	if(len(sys.argv) == 1):
		g.msgbox("Please, insert the name of the test!")
		sys.exit()

		
	test_file_name = sys.argv[1]
 	
	# Open the workbook --> excel file
	excel_test = xlrd.open_workbook('./inputs/keyword_tests/' + test_file_name + '.xls')

	# Goes directely to sheet that contains the test --> keyword table
	xl_sheet = excel_test.sheet_by_name('Test')

	# check if all keywords in the test exist or are well written
	# returns the number of steps
	num_steps =  keywordExists(xl_sheet);

	test_file_path = './Java_Tests/'+test_file_name+'.java'
	temp_file_path = './inputs/java_template/java_template.java'
	
	# create the java file test
	geral.createFile(test_file_path, temp_file_path);

	# Update the name of the java file
	updateClassName(test_file_name, test_file_path);

	# Insert Constructor and Initialization Conditions	
	insertConstAndInit(xl_sheet, test_file_name,test_file_path);

	# create step list
	createStepsList(test_file_path, num_steps);

	# Add each keyword
	stepKeyword(xl_sheet, test_file_path, num_steps);
	

if __name__== "__main__":
	start_time = time.time()
        main()
	print("|------------------------------------------------------------|")
	print("| Running time: %s seconds" % (time.time() - start_time))
	print("|------------------------------------------------------------|")

#############################################################################################################################













