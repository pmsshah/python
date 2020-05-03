#!/usr/bin/python

"""
read directory tree and read all files.
"""
import os
from pathlib import Path
from datetime import datetime
import time

class FileUtil:
	'Hold all File, Folder Utils' 
	# many things from https://realpython.com/working-with-files-in-python/

	#def __init__(self):
		#conn = sqlite3.connect(dbname) # connect to database

	@classmethod
	def convert_date(cls, timestamp):
		d = datetime.utcfromtimestamp(timestamp)
		formated_date = d.strftime('%d %b %Y')
		return formated_date
    
	@classmethod
	def convert_time(cls, timestamp):
		year,month,day,hour,minute,second=time.localtime(timestamp)[:-3];
		return ("%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))

	@classmethod
	def wrapquate(cls, str):
		if(str.find(",") != -1):
			str_tmp=('"%s"'%(str));
			return str_tmp;
		return str;

	@classmethod
	def fileList(cls, path=".", headeron=False):   # list all files from current location
		basepath = Path(path)
		files_in_basepath = basepath.iterdir()
		print (("ItemId,Name,Path,CompltePath,Tag0,Tag1,Tag2,Tag3,Tag4,Tag5,Location,Type,CTimeStamp,MTimeStamp,ATimeStamp,Size,Comment,AIComment","")[not headeron])

		for item in files_in_basepath:
			newfilename=FileUtil.wrapquate(item.name);
			newpath=FileUtil.wrapquate(path);
			newfullfile=FileUtil.wrapquate(path+"/"+item.name);
			
			info = item.stat()
			filetype="File"
			filesize=info.st_size
			if item.is_dir():
				filetype="Folder"
				filesize=0
			#print("File:"+newfullfile+",", FileUtil.convert_date(info.st_ctime), ",", FileUtil.convert_date(info.st_mtime), ",", FileUtil.convert_date(info.st_atime), ",", info.st_size)
			#print("File:"+newfullfile+",", FileUtil.convert_time(info.st_ctime), ",", FileUtil.convert_time(info.st_mtime), ",", FileUtil.convert_time(info.st_atime), ",", info.st_size)
			print(","+newfilename+","+newpath+","+newfullfile+","+",,,,,,Work,"+filetype+",",info.st_ctime, ",",info.st_mtime, ",",info.st_atime, ",", filesize,",,");
			if item.is_dir():
				FileUtil.fileList(path+"/"+item.name);

def main():
	if True: # Add Items
		FileUtil.fileList(".", True);
		#os.rename("my file,1,2,name.txt","my file-1-2-name.txt");
		#mystr="my file,1,2,name.txt";
		#print ("1:",mystr);
		#mystr1=mystr.replace(",","-");
		#print ("2:",mystr1);
		
if __name__ == '__main__':
    main()
