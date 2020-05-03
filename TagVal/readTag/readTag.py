#!/usr/bin/python
"""
read file readTag-alltag.txt and reformat based on levels.

"""
	
def readTag(file1):
	#print ("==>", " - ",file1);
	line1=[];
	with open(file1) as fp1:
		for line in fp1:
			line=line.strip();
			if(line == ""):
				continue;
			line1.append(line);

	line1.sort();
	prvline="";
	prvlinewords=[];
	for i, line in enumerate(line1): 
		if(line == prvline):
			continue;
		#print(i+1,"==>"+line);
		prvline=line;
		linewords = line.split("\t");
		prvlen = len(prvlinewords);
		#print("\t", i, end='');
		for j, word in enumerate(linewords): 
			if(word in prvlinewords[j:]):
				for k in range(len(word)):
					print("-", end='');
				print(">", end='');
				continue;
			print("-"+word, end='');
		print("");
		#print("linewords\t\t", len(linewords), linewords);
		#print("prvlinewords\t\t", len(prvlinewords), prvlinewords);
		prvlinewords=linewords;

def main():
	if True: # Add Items
		readTag("readTag-alltag.txt");

if __name__ == '__main__':
    main()
