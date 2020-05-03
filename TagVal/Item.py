#!/usr/bin/python
"""
Basic Item class.
Only used by unittest
"""
class Item:
	# hold one item

	def __init__(self, ItemId="", Name="", Path="", CompletePath="", NewFileName="",
		NewTags="", Tag0="", Tag1="", Tag2="", Tag3="", Tag4="", Tag5="", 
		LocationPlace="", ItemType="",
		CreateTimeStamp="", ModifyTimeStamp="", AccessTimeStamp="", Size="",
		UserComment="", AIComment="", Final="", FinalDate=""):

		self.ItemId = ItemId;
		self.Name = Name;
		self.Path = Path;
		self.CompletePath = CompletePath;
		self.NewFileName = NewFileName;
		self.NewTags = NewTags;
		self.Tag0 = Tag0;
		self.Tag1 = Tag1;
		self.Tag2 = Tag2;
		self.Tag3 = Tag3;
		self.Tag4 = Tag4;
		self.Tag5 = Tag5;
		self.LocationPlace = LocationPlace;
		self.ItemType = ItemType;
		self.CreateTimeStamp = CreateTimeStamp;
		self.ModifyTimeStamp = ModifyTimeStamp;
		self.AccessTimeStamp = AccessTimeStamp;
		self.Size = Size;
		self.UserComment = UserComment;
		self.AIComment = AIComment;
		self.Final = Final;
		self.FinalDate = FinalDate;
		
	def print(self):
		print ("\tID: {}, Name: {}, Path: {}, CompletePath: {}, NewFileName: {}".format(self.ItemId,self.Name,self.Path,self.CompletePath,self.NewFileName));
		print ("\tNewTags: {},Tag0: {}, Tag1: {}, Tag2: {}, Tag3: {}, Tag4: {}, Tag5: {}\n".format(self.NewTags,self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5));
		print ("\tLocationPlace: {}, ItemType: {}, Size: {}".format(self.LocationPlace,self.ItemType, self.Size));
		print ("\tFinal: {}, FinalDate: {}, CreateTimeStamp: {}, ModifyTimeStamp: {}, AccessTimeStamp: {}".format(self.Final,self.FinalDate,self.CreateTimeStamp,self.ModifyTimeStamp, self.AccessTimeStamp));
		print ("\tUserComment: {}, AIComment: {}".format(self.UserComment,self.AIComment));

	def lineprint(self):
		#return ("ID: {}, Name: {}, Type: {}, Size: {}, TimeStamp: {}, Location: {}, UserComment: {}, AComment: {}, Tag0: {}, Tag1: {}, Tag2: {}, Tag3: {}, Tag4: {}, Tag5: {}".format(self.ItemId,self.Name, self.Type, self.Size, self.TimeStamp, self.Location, self.Comment, self.AIComment, self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5))
		return ("ItemId: {}, Name: {}, Path: {}, CompletePath: {}, NewFileName: {}, NewTags: {}, Tag0: {}, Tag1: {}, Tag2: {}, Tag3: {}, Tag4: {}, Tag5: {}, LocationPlace: {}, ItemType: {}, CreateTimeStamp: {}, ModifyTimeStamp: {}, AccessTimeStamp: {}, Size: {}, UserComment: {}, AIComment: {}, Final: {}, FinalDate: {}".format(self.ItemId,self.Name,self.Path,self.CompletePath,self.NewFileName,self.NewTags,self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5,self.LocationPlace,self.ItemType,self.CreateTimeStamp,self.ModifyTimeStamp,self.AccessTimeStamp,self.Size,self.UserComment,self.AIComment,self.Final,self.FinalDate));
		
	def csvprint(self):
		return ("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.ItemId,self.Name,self.Path,self.CompletePath,self.NewFileName,self.NewTags,self.Tag0,self.Tag1,self.Tag2,self.Tag3,self.Tag4,self.Tag5,self.LocationPlace,self.ItemType,self.CreateTimeStamp,self.ModifyTimeStamp,self.AccessTimeStamp,self.Size,self.UserComment,self.AIComment,self.Final,self.FinalDate));

	def csvheaderprint(self):
		return ("ItemId,Name,Path,CompletePath,NewFileName,NewTags,Tag0,Tag1,Tag2,Tag3,Tag4,Tag5,LocationPlace,ItemType,CreateTimeStamp,ModifyTimeStamp,AccessTimeStamp,Size,UserComment,AIComment,Final,FinalDate");


	def compare(self, item1):
		selfstr = self.lineprint();
		newstr = item1.lineprint();
		if (selfstr == newstr):
			return 1;
		return 0;


if __name__ == '__main__':
    main()
    


