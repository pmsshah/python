print ("Hello, Python!")
List = ["Open", "Close", "Home", 1, 2, 3]
tag = "Home1"
if (tag in List):
	print ("Yes in List")
newtag = tag if (tag in List) else "" # one line if statment
print ("New Tag:", newtag)

id1=1

print ("I am\n") if (id1!=2) else None

item1="Name"
item2="Name"

print ("Item are same \n") if (item1==item2) else None
item2="Name1"
print ("Item are not same \n") if (item1!=item2) else None

def mylongfun(id="", Name="", Path="", CompletePath="", NewFName="",
	NewTags="", Tag0="", Tag1="", Tag2="", Tag3="", Tag4="", Tag5="", 
	LocPlace="", ItemType="",
	CreateTimeStamp="", ModifyTimeStamp="", AccessTimeStamp="", Size="",
	UserComment="", AIComment="", Final="", FinalDate=""):
	print("My Long fun\n");


mylongfun();