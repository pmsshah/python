import unittest
import Item

class TestItem(unittest.TestCase):

	#1- create one item and make sure line print same.
	def test_1_item_create(self):
		item = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		expectedresult = "ItemId: 1, Name: proj1.txt, Path: C:\My Doc\Work\Project\Proj1, CompletePath: C:\My Doc\Work\Project\Proj1\proj1.txt, NewFileName: , NewTags: , Tag0: Open, Tag1: Work, Tag2: Project, Tag3: Proj1, Tag4: , Tag5: , LocationPlace: Work, ItemType: TXT, CreateTimeStamp: 01012020, ModifyTimeStamp: 01022020, AccessTimeStamp: 01032020, Size: 0, UserComment: my proj file1, AIComment: ai ai proj file1, Final: 1, FinalDate: 01042020";
		self.assertEqual(expectedresult,item.lineprint());

	#2- create two same items and compare should be 1
	#@unittest.skip("skip")
	def test_2_item_compare(self):
		item1 = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		item2 = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		self.assertEqual(item1.compare(item2), 1);

	#3- create two diffrent items and compare should be 0
	#@unittest.skip("skip")
	def test_3_item_compare_diffrent(self):
		item1 = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		item2 = Item.Item(1,"proj2.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		self.assertEqual(item1.compare(item2), 0);

	#4- create one item and make sure cvs print same.
	def test_4_item_create(self):
		item = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		expectedresult = "1,proj1.txt,C:\My Doc\Work\Project\Proj1,C:\My Doc\Work\Project\Proj1\proj1.txt,,,Open,Work,Project,Proj1,,,Work,TXT,01012020,01022020,01032020,0,my proj file1,ai ai proj file1,1,01042020";
		self.assertEqual(expectedresult,item.csvprint());

	#4- create one item and make sure cvs header print same.
	def test_5_item_create(self):
		item = Item.Item(1,"proj1.txt", "C:\My Doc\Work\Project\Proj1", "C:\My Doc\Work\Project\Proj1\proj1.txt", "", "", "Open", "Work", "Project", "Proj1", "", "", "Work", "TXT", "01012020","01022020","01032020", 0, "my proj file1", "ai ai proj file1",1,"01042020");
		expectedresult = "ItemId,Name,Path,CompletePath,NewFileName,NewTags,Tag0,Tag1,Tag2,Tag3,Tag4,Tag5,LocationPlace,ItemType,CreateTimeStamp,ModifyTimeStamp,AccessTimeStamp,Size,UserComment,AIComment,Final,FinalDate";
		self.assertEqual(expectedresult,item.csvheaderprint());


def suite():
	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(TestItem))
	return test_suite;

if __name__ == '__main__':
	unittest.main()
   
#run python -m unittest Item_UTest.TestItem