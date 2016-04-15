#! usr\bin\env python
'''
This python script will be useful for interactively handling objects (currently fasta files)
This python script is designed to be run within a windows console running python 2.7

Note: In order to make the script work better, make sure that the Windows console has 'Quick 
Edit' and Insert Mode' options selected. This can be done by:

- Right clicking on the address bar at the top of the Windows console
- Clicking on the 'Properties' option from the menu
- Going to the 'Options' tab
- Clicking on the white boxes under the 'Edit options' field to fill them both with ticks

Now the text which pops up in the console can easily be highlighted by holding down the left 
mouse button and dragging the cursor across the desired text. Once the text is highlighted, the 
'ENTER' button can be pressed to copy this text. Afterwards, a simple right click will paste 
the copied text directly into the the console. Then ENTER can be pressed again, in order for 
the python interpreter to work on this text
'''

# First we set up variables to easily define paths of every file
import sys
import os.path
from Bio import SeqIO
__location__= os.path.realpath(os.path.join(\
os.getcwd(), os.path.dirname(__file__)))

# Warning. Mash2 and Mash3 must be local. Otherwise, their contents grow forever
mash=[]
junk=[]


for filename in os.listdir(__location__):
		junk.append(filename)
# For vertical listing use  '\n'.join(ls)   and	 ','.join(str(v) for v in ls)
# The following values have static roles 
answer0= 'single_contigs.fasta'
fullPATH1=  (os.path.join(__location__, filename))
target=SeqIO.to_dict(SeqIO.parse(fullPATH1,'fasta'))
default='S.AUREUS_CONTIG_ASSEMBLY'

# The following values will be part of an infinite(dynamic) loop
attr= '_seq'
spot=0
answer1= 'save'


#   dictextract(answer0,default,attr,spot,answer1)
def dictextract(filename,KEY,attribute,nth,logic):
# Warning. Function wont work without getting an object through parsing of a file
		try:
				path=   (os.path.join(__location__, filename))
				zone=SeqIO.to_dict(SeqIO.parse(path,'fasta'))
		except:
				print "Filename incorrect or file does not exits!!!"
				sys.exit()
		print "<List of zone dictionary keys>\n",\
		','.join(str(v) for v in zone.keys())

		chosen= zone[KEY]
		# We can now view the properties of our chosen dictionary
		dict_x=chosen.__dict__
		print '\n<Chosen dictionary keys>\n','\n'.join(dict_x.keys())

		mash2= []
		def extractor(on):
				item= dict_x[on]
				mash2.append(item)
		extractor(attribute)
		print '\n<Key contents>\n',mash2

		# Position-based extractor function 
		mash3=[]
		def positioner():
				def getitem(n):
						n=int(n)
						position=mash2[n]
						mash3.append(position)
				print 
				getitem(nth)
				print '<Updated content list>\nMYlist: ',mash3,'\nLength:',\
				len(mash3),'\n'
		positioner()
		# At this point, we have reached the bottom of our tree
		# Now we need to create and option to recall functions and add more items
		# While also creates an infinite loop

		extractor(attribute)
		fullPATH2=  (os.path.join(\
		__location__, 'auto_key_results.txt'))
		# Final value recorder function
		def junkman(trash):
				# Small loop to get values based on positions
				scope= range(0,(len(trash)),1)
				f=open(fullPATH2,'wb')
				for i in scope:
						touched= trash[scope[i]]
						f.write(str(touched)+'\n')
		junkman(mash3)

begin=raw_input('\nAutomatic or manual selection mode?[A/M]:')

if begin == 'A':
		print '\n<Single selection mode engaged>\n'
		dictextract(answer0,default,attr,spot,answer1)


elif begin == 'M':
# Redefined variables with logic
		jump= raw_input('\nWhich data extraction mode would you like? (single/multi): ') 
		if jump == 'single':
				def dictextract2():
						# This version of the function requires only raw_inputs
						print '\n<List of available files>\n\n','\n'.join(junk)
						# filename
						'''
						Now we can define a large function to interactively handle out objects.
						This is for the single file extraction mode which includes choosing a 
						single key out of the dictionary that is produced from the file, and 
						then extracting the desired amount of values from it. Remember that any 
						return value used in a function give final function value. Looks like I 
						will have to create many large functions.
						'''
						try:
								answer2=raw_input('\nEnter filename:')
								fullPATH2=  (os.path.join(__location__, answer2))
								target2=SeqIO.to_dict(SeqIO.parse(fullPATH2,'fasta'))
						except:
								print "Filename incorrect or file does not exits!!!"
								sys.exit()

						print "\n<List of global variables>\n",sorted(globals())
						print "\nCreate empty 'mash' list"
						if 'mash' in globals():
								mash == []
								print '-Present'
						else:
								print "Error: No empty 'mash' list detected\n"
								sys.exit()
								print "Create filled 'key' dictionary"
						if 'target' in globals():
								if target2 == []:
										print "Error: Empty 'target' detected"
										sys.exit()
								else:
										print '-Present\n'

										print "<List of target dictionary keys>\n",\
										','.join(str(v) for v in target2.keys())

						# Maintenance. Default is first key amongst sorted keys
						# key
						chosen=[]
						keyNAME= raw_input('\nNow enter key name: ')
						chosen= target2[keyNAME]

						# We can now view the properties of our chosen dictionary key
						dict_x=chosen.__dict__
						print '\n<Chosen dictionary options>\n',dir(dict_x)

						print '\n<Chosen dictionary key attributes>\n','\n'.join(dict_x.keys())

						# Finally we can extract contents of our desired key values to files
						# The extractor function appends desired values with mash2
						# Maintenance
						attr2= raw_input('\nChoose a key attribute: ')
						mash2= []
						def extractor(on):
								item= dict_x[on]
								mash2.append(item)
								return mash2
						extractor(attr2)

						print '\n<Key contents>\n',mash2

						# This function uses list positions to call desired functions
						# We can add a function after it to return mash3's set values, for later use 


						# Position-based extractor function 
						mash3=[]
						def positioner():
								print '\nMYlist: ',mash3,'\nLength:',len(mash3),'\n'
								def getitem(n):
										n=int(n)
										position=mash2[n]
										mash3.append(position)
										return mash3
								print
								# Maintenance
								spot2= raw_input('Select content position (0,1,2...): ')
								getitem(spot2)
								print '\n<Key contents>\n',mash2
						print '\n<Updated content list>\n\nMYlist: ',mash3,'\nLength:',\
						len(mash3),'\n'

						positioner()
						# At this point, we have reached the bottom of our tree
						# Now we need to create and option to recall functions and add more items
						# While also creates an infinite loop
						if begin == 'A':
								extractor(attr2)

								fullPATH3=  (os.path.join(\
								__location__, 'single_key_results.txt'))

								# Final value recorder function
								def junkman(trash):
								# Small loop to get values based on positions
										scope= range(0,(len(trash)),1)
										f=open(fullPATH3,'wb')
										for i in scope:
												touched= trash[scope[i]]
												f.write(str(touched)+'\n')
												f.close()

						elif begin == 'M':
								while True:
										# Maintenance
										answer3=raw_input('Add more info? (Yes[y]/No[n]: ')
										if answer3=='y':
												print '\n<Chosen dictionary keys>\n','\n'.join(dict_x.keys())
												mash2= []
												try:
														# Maintenance
														# attr2
														attr2= raw_input('\nChoose a key attribute: ')
														extractor(attr2)
												except:
														print 'Try again'
														sys.exit()
												print '\n<Key contents>\n',mash2
												positioner()
										# Just a copied the above here, with slight alterations 
										elif answer3=='n':
												fullPATH3=  (os.path.join(\
														__location__, 'single_key_results.txt'))
												# Final value recorder function
												def junkman(trash):
												# Small loop to get values based on positions
														scope= range(0,(len(trash)),1)
														f=open(fullPATH3,'wb')
														for i in scope:
																touched= trash[scope[i]]
																f.write(str(touched)+'\n')

												junkman(mash3)
												print
												sys.exit('END OF THE LINE')
										else:
												print 'Error'
												sys.exit()
						else:
								print 'Error'
								sys.exit()

				dictextract2()

		elif jump == 'multi':
				fullPATH4= (os.path.join(__location__,'multiple_key_results.txt'))
				folder= (os.path.join(__location__,'all_fasta_output'))
				if not os.path.exists(folder):
						os.makedirs(folder)
				print '\n<Output will be stored in the following location>\n\n',folder
# Having obtained storage space, we can now create an output and link it with this location

# The dictextract3 function should be similar to dictextract2
# Differences should be seen in two general areas
# 1- All dictionary records must be selected instead of just one 
# 2- Multiple files must be created for storing record specific data (i.e. after 'key' is selected)

# Need to define new:
				def dictextract3():
						print '\n<List of available files>\n\n','\n'.join(junk)
						try:
								answer4=raw_input('\nEnter filename:')
								fullPATH4=  (os.path.join(__location__, answer4))
								target4=SeqIO.to_dict(SeqIO.parse(fullPATH4,'fasta'))
						except:
								print "Filename incorrect or file does not exits!!!"
								sys.exit()
						answer5=[]
						mash4=  []
						mash5=  []
						chosen= []
						for v in target4.keys():
							chosen.append(v)
						try:
								print "\n<Top ten 'chosen' objects>\n",chosen[0:10]
						except:
								sys.exit()
						# Note that, at this point, a single record is selected to list key attributes
						# This assumes that all key attributes in our records are the same
						neat=sorted((target4['NODE_271_length_65_cov_151.984619']).__dict__)
						print '\n<The chosen dictionary key attributes>\n\n','\n'.join(neat)
						print

						'''
						We will be using extractor2 to get a key value out of the first record given that the record isn't empty. We will then define a variable with
						this chosen key, and return all of the records
						'''
						
						def dictextractF(on):
							for i in target4:
								asdf=target4[i]
								# Very useful little function here
								# Allows for attribute calling using strings
								mash4.append(getattr(asdf,on))
								return mash4
						# Maintenance
						attr3=raw_input('What attribute?: ')
						dictextractF(attr3)
						print mash4
						'''
						Figure out a way to create mutiple file names
						We can get names of all nodes in a list and then create iteration
						Iteration can make multiple files and take inputs
						Inputs can be defined based on target4 key contents
						And Bob's your uncle...
						'''
						all_names= target4.keys()
						print '\nall_names:\t',all_names.__class__
						print 'totat filenames:\t',len(all_names)
						buffer=[]
						
						# In the end, I should be left with exactly 230 files

						for n in all_names:
								# Cheeky formating...
								answer5= 'all_fasta_output/%s.txt' % (n)
								hope=(os.path.join(__location__, answer5))
								"""
								# This is where the magic happens
								def junkman(trash):
										scope= range(0,(len(trash)),1)
										f=open(hope,'wb')
										for i in scope:
												touched= trash[scope[i]]
												f.write(str(touched)+'\n')
								"""
								# There we go! All I needed was a dictionary!!!
								g=((target4[n]).__dict__)
								buffer= str(g[attr3])
								# Warning. A lot of overwriting will be taking place here
								with open(hope, 'wb') as temp_file:
										temp_file.write(buffer)

				dictextract3()   
		else:
				print '\nTry again'
				sys.exit()
else:
		print 'Try again'
		sys.exit()
