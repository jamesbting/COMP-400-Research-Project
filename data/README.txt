Each row of the cleaned dataset should be 1150 long. headers.txt represents the headers for each row of 1150. 


champions-cleaned.json is a dictionary that converts the ordered list of champions to their name, and the champion ID used by Riot Games.
This is necessary for interprerting the ID's given by the recommendation system into champion names, and vice versa.


---------!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!---------
For all programs to work properly, you must download the following archive and extract it. You can download the archive from here:
https://mcgill-my.sharepoint.com/:u:/g/personal/james_ting_mail_mcgill_ca/Ef623xj_2p9Oux06Xig89tYBM_I3Hgmt4SZoefsrsoINWQ?e=baiMSp


Once extracted, there will be 2 files:
"pre-cleaning-dataset.csv" and "post-cleaning-dataset.csv"
These files should be put in the data folder without being renamend with all the other datasets to ensure that the programs work properly. 
The programs can still work if they are not, but it will be necessary to reconfigure each program. 

Here is a brief description of each file:
champions.json: A json file containing information about every champion in League Of Legends
champions-cleaned.json: A json file containing a key and ID for every champion in League of Legends. Use to map from champion keys to champion names to champion IDs and vice versa. 
filtered-dataset.csv: A CSV file containing all the champions and outcomes from all the unique matches that were collected and with correct length.
filtered-dataset-no-headers.csv: Same as above, but without the header row.
headers.txt: A text file containing the headers for each row of length 1150.
post-cleaning-dataset.csv: A CSV containing all unique collected matches that had length 1150.
pre-cleaning-dataset.csv: A CSV containing all collected matches.
team_dict.txt: A text file contining a python dictionary, maping team combinations to a 2 dimensional array, where the first integer is the number of wins by that team combination and the second integer is the number of times that team combination was encountered.
win_rate.txt: A text file contining 2 numbers: the first beign the number of times blue team won, and the second being the number of matches in the dataset. 