print ("Hello, Python!")

if True:
   print ("True")
else:
   print ("False")
  
age=15
print(('adult', 'kid')[True])
print({True: 'kid', False: 'adult'}[age < 20])
print(((age < 20) and ['kid'] or ['adult'])[0])
print('kid' if age < 18 else 'adult')
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')

Tag0 = ["Open", "Close"]
inTag0="x"
OutTag0=inTag0 if (inTag0 in Tag0) else "Open"	#Must be Open or Close
print(inTag0, OutTag0);

print ("I am in") if (OutTag0 in Tag0) else None
print (("Print Me Always","")[False])
print (("Print Me Always","")[not True])
