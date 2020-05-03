#!/usr/bin/python

import sqlite3  #SQL Lite import, DB connections.
import csv 	# to import, export csv files.

class Item:
	# hold one item and total item count.
	# let you update the item, individual para, set/get.
	# print the item.

	'Common base class for all Item' 
	ICount = 0 # class variable.
	Tag0 = ["Open", "Close"]
	Tag1 = ["Tag1", "Personal", "Work", "Education"]
	Tag2 = ["Tag2", "Home", "Finance", "Fun", "Projects", "Meeting", "Mgmt", "Subject", "Technology", "Quick Check"]
	Tag3 = ["Tag3"]
	Tag4 = ["Tag4"]
	Tag5 = ["Tag5"]
	

	def __init__(self, id="", name="", u_comment="", ai_comment="", tag0="Open", tag1="", tag2="", tag3="", tag4="", tag5="", location="", type="", timestamp="", size=0):
		self.ItemId=id			#id of the item.
		self.Name=name			#name of the item.
		self.Size=size			#size of file
		self.TimeStamp=timestamp	#timestamp
		self.Location=location		#Where the item is located, in garage, in refrigerator, in complete path,  iPhone, flash drive, cloud etc. 
		self.Type=type			#Washing machine, screwdriver- add picture.
		self.Comment=u_comment	#Your comments, what you think about this item.
		self.AIComment=ai_comment	#System will scan documents, and put more meaningful details.
		#print ("Tag0:", tag0)
		#print ("Tag1:", tag1)
		self.Tag0=tag0 if (tag0 in Item.Tag0) else "Tag0"	#Must be Open or Close
		self.Tag1=tag1 if (tag1 in Item.Tag1) else "Tag1"	#Must be Tag1
		self.Tag2=tag2 if (tag2 in Item.Tag2) else "Tag2"	#Must be Tag2
		self.Tag3=tag3 if (tag3 in Item.Tag3) else "Tag3"	#Must be Tag3
		self.Tag4=tag4 if (tag4 in Item.Tag4) else "Tag4"	#Must be Tag4
		self.Tag5=tag5 if (tag5 in Item.Tag5) else "Tag5"	#Must be Tag5

	def displayCount(self):
		print ("Total Item %d" % Item.ICount)
	

	def print(self):
		print ("\tID: {}, Name: {}, Type: {}".format(self.ItemId,self.Name, self.Type))
		print ("\tSize: {}, TimeStamp: {}, Location: {}".format(self.Size, self.TimeStamp, self.Location))
		print ("\tUserComment: {}, AComment: {}".format(self.Comment, self.AIComment))
		print ("\tTag0: {}, Tag1: {}, Tag2: {}, Tag3: {}, Tag4: {}, Tag5: {}\n".format(self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5))

	def retprint(self):
		return ("ID: {}, Name: {}, Type: {}, Size: {}, TimeStamp: {}, Location: {}, UserComment: {}, AComment: {}, Tag0: {}, Tag1: {}, Tag2: {}, Tag3: {}, Tag4: {}, Tag5: {}".format(self.ItemId,self.Name, self.Type, self.Size, self.TimeStamp, self.Location, self.Comment, self.AIComment, self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5))

	def compare(self, item1):
		selfstr = self.retprint();
		newstr = item1.retprint();
		if (selfstr == newstr):
			return 1;
		return 0;

class ItemMap:
	# let you hold/add each item right place by key:tags
	# let you search item by tag or part of name.
	# ?? How about store item in list.
	#	then add item index based on key:tag map
	#	also add item to name base list to regular expression. Name string stored two times??
	# 1-Connect to DB
	# 2-Add to DB
	# 3-List to DB
	'Hold all Items' 
	conn=sqlite3.connect('myorg.db')
	
	#def __init__(self, dbname='myorg.db'):
		#conn = sqlite3.connect(dbname) # connect to database
		
	@classmethod
	def describe(cls):	# list all the columns of the table.
		ColList=[]
		query = cls.conn.execute("pragma table_info('Item')") # This line performs query and returns json result
		for row in query:
			#print ("\t", row[1], "\n")
			ColList.append(row[1])
		return ColList

	@classmethod		# provide way to delete.
	def delItemQry(cls, query=""):
		sqlstmt = "DELETE FROM Item"+query;
		#print (sqlstmt, "\n")
		cur=cls.conn.cursor()
		query = cur.execute(sqlstmt)
		cur.close()
		cls.conn.commit();
		myrowcount = cur.rowcount;
		return myrowcount;

	@classmethod
	def delItemMyItem(cls, item):
		return cls.delItem(item.ItemId);
		
	@classmethod		# provide way to delete.
	def delItem(cls, Id="", Name="", Comment="", AIComment="", Tag0="", Tag1="", Tag2="", Tag3="", Tag4="", Tag5="", Location="", Type="", TimeStamp="", Size=0):
		sqlstmt = "DELETE FROM Item"
		where = []
		params = {}

		if Id != "":
			where.append("ItemId = :Id")
			params['Id'] = Id
		if Name != "":
			where.append("Name = :Name")
			params['Name'] = Name
		if Comment != "":
			where.append("Comment = :Comment")
			params['Comment'] = Comment
		if AIComment != "":
			where.append("AIComment = :AIComment")
			params['AIComment'] = AIComment
		if Tag0 != "":
			where.append("Tag0 = :Tag0")
			params['Tag0'] = Tag0
		if Tag1 != "":
			where.append("Tag1 = :Tag1")
			params['Tag1'] = Tag1
		if Tag2 != "":
			where.append("Tag2 = :Tag2")
			params['Tag2'] = Tag2
		if Tag3 != "":
			where.append("Tag3 = :Tag3")
			params['Tag3'] = Tag3
		if Tag4 != "":
			where.append("Tag4 = :Tag4")
			params['Tag4'] = Tag4
		if Tag5 != "":
			where.append("Tag5 = :Tag5")
			params['Tag5'] = Tag5
		if Location != "":
			where.append("Location = :Location")
			params['Location'] = Location
		if Type != "":
			where.append("Type = :Type")
			params['Type'] = Type
		if TimeStamp != "":
			where.append("TimeStamp = :TimeStamp")
			params['TimeStamp'] = TimeStamp
		if Size != 0:
			where.append("Size = :Size")
			params['Size'] = Size
		if where:
			sqlstmt = '{} WHERE {}'.format(sqlstmt, ' AND '.join(where))

		#print (sqlstmt, "\n")
		cur=cls.conn.cursor()
		query = cur.execute(sqlstmt,params)
		cur.close()
		cls.conn.commit();

		myrowcount = cur.rowcount;
		if myrowcount != 1:
			print("record delete fail:", myrowcount);
		return myrowcount;	
		
	@classmethod		#list on screen with filter
	def list(cls, Id="", Name="", Comment="", AIComment="", Tag0="", Tag1="", Tag2="", Tag3="", Tag4="", Tag5="", Location="", Type="", TimeStamp="", Size=0):
		sqlstmt = "SELECT * FROM Item"
		where = []
		params = {}

		if Id != "":
			where.append("ItemId = :Id")
			params['Id'] = Id
		if Name != "":
			where.append("Name = :Name")
			params['Name'] = Name
		if Comment != "":
			where.append("Comment = :Comment")
			params['Comment'] = Comment
		if AIComment != "":
			where.append("AIComment = :AIComment")
			params['AIComment'] = AIComment
		if Tag0 != "":
			where.append("Tag0 = :Tag0")
			params['Tag0'] = Tag0
		if Tag1 != "":
			where.append("Tag1 = :Tag1")
			params['Tag1'] = Tag1
		if Tag2 != "":
			where.append("Tag2 = :Tag2")
			params['Tag2'] = Tag2
		if Tag3 != "":
			where.append("Tag3 = :Tag3")
			params['Tag3'] = Tag3
		if Tag4 != "":
			where.append("Tag4 = :Tag4")
			params['Tag4'] = Tag4
		if Tag5 != "":
			where.append("Tag5 = :Tag5")
			params['Tag5'] = Tag5
		if Location != "":
			where.append("Location = :Location")
			params['Location'] = Location
		if Type != "":
			where.append("Type = :Type")
			params['Type'] = Type
		if TimeStamp != "":
			where.append("TimeStamp = :TimeStamp")
			params['TimeStamp'] = TimeStamp
		if Size != 0:
			where.append("Size = :Size")
			params['Size'] = Size
		if where:
			sqlstmt = '{} WHERE {}'.format(sqlstmt, ' AND '.join(where))

		print (sqlstmt, "\n")
		cur=cls.conn.cursor()
		query = cur.execute(sqlstmt,params)

		myrowcount = 0;
		for row in query:
			item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]) #Item(ID, Name, Comment, AIComment, Tag0, Tag1, Tag2, Tag3, Tag4, Tag5, Location, Type, TimeStamp, Size)
			item.print()
			myrowcount+=1;
			print ("myrowcount:", myrowcount, "\n");
		cur.close()
		return myrowcount;

	@classmethod
	def listall(cls, printon=True):
		myrowcount = 0;
		query = cls.conn.execute("select * from Item") # This line performs query and returns json result
		if False:
			for row in query:
				item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]) #Item(ID, Name, Comment, AIComment, Tag0, Tag1, Tag2, Tag3, Tag4, Tag5, Location, Type, TimeStamp, Size)
				item.print()
			
		if printon:
			ColList=ItemMap.describe()
			for row in query:
				myrowcount+=1;
				print("\n")
				for i, val in enumerate(row): 
				    print ("\t", ColList[i], " : ", val) 
			print ("Total row count: ", myrowcount);
		else:
			for row in query:
				myrowcount+=1;

		return myrowcount;
		
	@classmethod
	def listqry(cls, query="", printon=True):
		myrowcount = 0;
		sqlstmt = "select * from Item" + query;
		query = cls.conn.execute(sqlstmt) # This line performs query and returns json result
		if printon:
			ColList=ItemMap.describe()
			for row in query:
				myrowcount+=1;
				print("\n")
				for i, val in enumerate(row): 
				    print ("\t", ColList[i], " : ", val) 
			print ("Total row count: ", myrowcount);
		else:
			for row in query:
				myrowcount+=1;

		return myrowcount;

	@classmethod
	def addItem(cls, item):
		sqlstmt = """insert into Item ( ItemId, Name, Comment, AIComment, Tag0, Tag1, Tag2, Tag3, Tag4, Tag5, Location, Type, TimeStamp, Size) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
		cur=cls.conn.cursor()
		query = cur.execute(sqlstmt, (item.ItemId, item.Name, item.Comment, item.AIComment, item.Tag0, item.Tag1, item.Tag2, item.Tag3, item.Tag4, item.Tag5, item.Location, item.Type, item.TimeStamp, item.Size)) # This will insert item
		cur.close()
		cls.conn.commit();
		myrowcount = cur.rowcount;
		if myrowcount != 1:
			print("record insert fail:", myrowcount);
		return myrowcount;	

	@classmethod
	def getItem(cls, item):
		# find the item based on ItemId.
		# if not found add the item
		# if found, get table item and compare with file item.
		# if there is change, delete the table item and add file item


		sqlstmt = "SELECT * FROM Item"
		where = []
		params = {}

		Id = item.ItemId
		if Id != "":
			where.append("ItemId = :Id")
			params['Id'] = Id
		if where:
			sqlstmt = '{} WHERE {}'.format(sqlstmt, ' AND '.join(where))

		#print (sqlstmt, "\n")
		
		cur=cls.conn.cursor()
		query = cur.execute(sqlstmt,params)
		myrowcount=0
		dbItem=None;
		for row in query:
			dbItem = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]) #Item(ID, Name, Comment, AIComment, Tag0, Tag1, Tag2, Tag3, Tag4, Tag5, Location, Type, TimeStamp, Size)
			#dbItem.print()
			myrowcount+=1
		cur.close()
		if myrowcount>1:
			print ("multiple rows?", myrowcount);
		return dbItem;

	@classmethod	# import items from Csv file.
	def importupdateItems(cls, filename="items.import.csv"):
		fields = [] 
		cols = []
		with open(filename, 'r') as csvfile: 
			csvreader = csv.reader(csvfile) 
			for i, row in enumerate(csvreader): 
				if i==0:
					#print('Fields are: ', i, ', '.join(field for field in row))
					#cols = []
					#[cols.append(col) for col in row];
					#for j, col in enumerate(cols): 
						#print('Cols are: ', j, ', ', col, "\n");
					continue;
				else:
					item1=Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]);
					item2=ItemMap.getItem(item1);
					if item2 is None:
						ItemMap.addItem(item1);
						#print("Add: ", i);
						continue;
					#print("Compare/replace: ", i, item1.compare(item2));
					if (item1.compare(item2)==1):
						continue;
					#print("Replace: ",i);
					ItemMap.delItemMyItem(item2);
					ItemMap.addItem(item1);
					#ItemMap.updateItem(item1)

	@classmethod	# import items from Csv file.
	def importItems(cls, filename="items.import.csv"):
		fields = [] 
		cols = []
		with open(filename, 'r') as csvfile: 
			csvreader = csv.reader(csvfile) 
			for i, row in enumerate(csvreader): 
				if i==0:
					#print('Fields are: ', i, ', '.join(field for field in row))
					#cols = []
					#[cols.append(col) for col in row];
					#for j, col in enumerate(cols): 
						#print('Cols are: ', j, ', ', col, "\n");
					continue;
				else:
					#print('Rows are: ', i, ', '.join(col for col in row));
					#print ("nothing\n");
					#print('Rows are: ', i, ', '.join(col for col in cols), "\n");
					#print(cols[0],cols[1],cols[2],cols[3],cols[4],cols[5],cols[6],cols[7],cols[8],cols[9],cols[10],cols[11],cols[12],cols[13]);
					item1=Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]);
					#item1.print();
					ItemMap.addItem(item1)
		
	@classmethod	# export items to Csv file.
	def exportItems(cls, filename="items.export.csv", query=""):
		fields = ItemMap.describe();	# get list of fields.
		with open(filename, 'w') as csvfile: 
			csvwriter = csv.writer(csvfile) 
			csvwriter.writerow(fields) 
			query = cls.conn.execute('select * from Item' + query) # This line performs query and returns json result
			for row in query:
				csvwriter.writerow(row);

    
def addition(val1, val2):
	return val1+val2

def myfilecmp(file1, file2):
	#print ("==>", " - ",file1, " - ", file2);
	line1=[];
	with open(file1) as fp1:
		for line in fp1:
			line=line.strip();
			if(line == ""):
				continue;
			line1.append(line);

	line2=[];
	with open(file2) as fp2:
		for line in fp2:
			line=line.strip();
			if(line == ""):
				continue;
			line2.append(line);

	#print(len(line1),len(line2));
	if(len(line1) != len(line2)):
		return False;
	
	#line1.sort();
	#line2.sort();
	for i, val in enumerate(line1): 
		#print (i, "\n",val, "\n", line2[i]);
		if(val != line2[i]):
			return False;

	return True;

def main():
	if True: # Add Items
		ItemMap.delItemQry(' where ItemId < -1');
		ItemMap.importItems("testfile/items.import.csv");
		ItemMap.exportItems("testfile/update.export.1.csv", ' where ItemId < -1 order by ItemId DESC');
		ItemMap.importupdateItems("testfile/update.import.csv");
		ItemMap.exportItems("testfile/update.export.2.csv", ' where ItemId < -1 order by ItemId DESC');
		
	if False: # List Items
		ItemMap.list()

	if False: # List Items
		ItemMap.listall()

	if False: # Delete Items
		ItemMap.list()
		#Id = input("Enter your input: ")
		Id=""
		ItemMap.delItem(Id)

	if False: # Import the file
		ItemMap.importItems("testfile/items.import.csv")

	if False: # Import the file
		ItemMap.exportItems()

	if False: # Import the file
		ItemMap.updateItems()

if __name__ == '__main__':
    main()

"""

Multi Line Comments
Done: 
	class Item, init, print.
	class ItemMap, utility additem in table, list.
	delete all rows - Done
	Export all rows - Done
	Import all rows - Done.
	Import only changes - Pending.
To Do:
	1- Implement Rest Get API, then add filer
	2- Implement 
"""