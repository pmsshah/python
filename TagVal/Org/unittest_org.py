import unittest
import org

class TestStringMethods(unittest.TestCase):

	#1 - upper case
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	#2 - upper case
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	#3 - split
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)
			
	#4 - global addition from org
	def test_global_addition(self):
		sum = org.addition(10,20)
		self.assertEqual(sum,30)

	#5- create item and make sure it created right.
	def test_item_creation(self):
		item = org.Item(1,"Item1", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		expectedresult = "ID: 1, Name: Item1, Type: My Item1, Size: Home, TimeStamp: My?, Location: TXT, UserComment: 11, AComment: 1201, Tag0: Open, Tag1: Personal, Tag2: Tag2, Tag3: Tag3, Tag4: Tag4, Tag5: Tag5";
		self.assertEqual(expectedresult,item.retprint());

	#6- create two same items and compare should be 1
	def test_item_compare_same(self):
		item1 = org.Item(1,"Item1", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		item2 = org.Item(1,"Item1", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		self.assertEqual(item1.compare(item2), 1);

	#7- create two same items and compare should be 0
	def test_item_compare_diffrent(self):
		item1 = org.Item(1,"Item1", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		item2 = org.Item(1,"Item2", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		self.assertEqual(item1.compare(item2), 0);

	#8- ItemMap.describe utility functions.
	#	When I list the cols, it should match the cols list.
	def test_itemMap_descibe(self):
		cols=org.ItemMap.describe();
		expectedcollist = "ItemId,Name,Comment,AIComment,Tag0,Tag1,Tag2,Tag3,Tag4,Tag5,Location,Type,TimeStamp,Size";
		mycollist = ",".join(cols);
		self.assertEqual(expectedcollist, mycollist);

	#8- ItemMap.describe utility functions.
	#	When I list the cols, it should match the cols list.
	def test_itemMap_descibe(self):
		cols=org.ItemMap.describe();
		expectedcollist = "ItemId,Name,Comment,AIComment,Tag0,Tag1,Tag2,Tag3,Tag4,Tag5,Location,Type,TimeStamp,Size";
		mycollist = ",".join(cols);
		self.assertEqual(expectedcollist, mycollist);

	#9- ItemMap.addItem utility functions.
	#	Create a Item with -1 id, add it to the table.
	#	rowcount must be 1.
	#	also make sure to delete the row and 
	def test_itemMap_addItem(self):
		totcount = org.ItemMap.listall(False);	# get intial count
		item1 = org.Item(-1,"Item1", 11, "1201", "Open",  "Personal", "T2", "T3", "T4", "T5", "TXT", "My Item1", "My?", "Home");
		retval = org.ItemMap.addItem(item1);		# add item and confirm one added.
		self.assertEqual(retval, 1);

		retval = org.ItemMap.listall(False);	# get new count
		self.assertEqual(retval, totcount+1);	# confirm total count +1
		
		retval = org.ItemMap.delItemMyItem(item1)	# delete the item
		self.assertEqual(retval, 1);		# confirm only one deleted.

		retval = org.ItemMap.listall(False);
		self.assertEqual(retval, totcount);	# confirm total count is same.

	#10- 	delete all <-1 rows
	#	Import test file with <-1 ids
	#	Export all <-1 records to file
	#	compare two files, must be same.
	def test_itemMap_importExport(self):
		org.ItemMap.delItemQry(' where ItemId < -1');		#not sure how many, let's clean up
		org.ItemMap.importItems("testfile/items.import.csv");	#22 records must be inserted.
		retval = org.ItemMap.listqry(' where ItemId < -1', False);	# get new count
		self.assertEqual(retval, 22);				# confirm total count 22
		org.ItemMap.exportItems("testfile/items.export.csv", '  where ItemId < -1 order by ItemId DESC');	#get all -1 rows to export.
		retval = org.myfilecmp('testfile/items.export.csv', 'testfile/items.import.csv'); # must be true.
		self.assertEqual(retval, True);				# confirm file is same

	#11- 	delete all <-1 rows
	#	Import test file with <-1 ids
	#	Export all <-1 records to file
	#	compare two files, must be same.
	def test_itemMap_updateExport(self):
		org.ItemMap.delItemQry(' where ItemId < -1');		#not sure how many, let's clean up
		org.ItemMap.importItems("testfile/items.import.csv");	#22 records must be inserted.
		retval = org.ItemMap.listqry(' where ItemId < -1', False);	# get new count
		self.assertEqual(retval, 22);				# confirm total count 22
		org.ItemMap.exportItems("testfile/update.export.1.csv", '  where ItemId < -1 order by ItemId DESC');	#get all -1 rows to export.
		retval = org.myfilecmp('testfile/update.export.1.csv', 'testfile/items.import.csv'); # must be true.
		self.assertEqual(retval, True);				# confirm file is same
		org.ItemMap.importupdateItems("testfile/update.import.csv");	#Import updateed file, 3 new, 3 updated file.
		retval = org.ItemMap.listqry(' where ItemId < -1', False);	# get new count
		self.assertEqual(retval, 25);				# confirm total count 25
		org.ItemMap.exportItems("testfile/update.export.2.csv", ' where ItemId < -1 order by ItemId DESC');
		retval = org.myfilecmp('testfile/update.export.2.csv', 'testfile/update.import.csv'); # must be true.
		self.assertEqual(retval, True);				# confirm file is same


if __name__ == '__main__':
    unittest.main()