CREATE TABLE "Item"
(
    [ItemId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(1024)  NOT NULL,
    [Comment] NVARCHAR(1024),
    [AIComment] NVARCHAR(1024),
    [Tags] NVARCHAR(1024),
    [Location] NVARCHAR(20) ,
    [Type] NVARCHAR(20) ,
    [TimeStamp] DATETIME,
    [Size] INTEGER,
    [LinkTo] INTEGER,
    FOREIGN KEY ([LinkTo]) REFERENCES "Item" ([ItemId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

curl http://127.0.0.1:5002/employees
curl http://127.0.0.1:5002/tracks
curl http://127.0.0.1:5002/employees/8

curl -X "POST" "http://127.0.0.1:5002/employees" \
     -i \
     -H 'Content-Type: application/json' \
     -d $'{
        "LastName": "Shah",
        "FirstName": "Piyush",
        "Title": "Head of QA",
        "ReportsTo": "Chris S",
        "BirthDate": "12121970",
        "HireDate": "12122010",
        "Address": "USA",
        "City": "World",
        "State": "USA",
        "Country": "USA",
        "PostalCode": "01122",
        "Phone": "1231231111",
        "Fax": "1231232222",
        "Email": "pshah@eagleinvsys.com"
}'

curl http://127.0.0.1:5002/employees/9

