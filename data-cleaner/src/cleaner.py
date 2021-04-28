# this program checks for uniqueness of match IDs and removes the duplicates
import csv


def clean(original_file, new_file, header_file):
    removeDuplicates(original_file, new_file, header_file)

# load the headers
def get_headers(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content


# remove the duplicate match IDs, and remove the match IDs with incorrect length
def removeDuplicates(filename, new_filename, header_file):
    matchIDs = {}
    count = 0
    duplicates = 0
    #open the appopriate files and set up reader and writer
    new_file = open(new_filename, "w",newline='')
    original_file = open(filename, "r")
    writer = csv.writer(new_file, delimiter=',')
    reader = csv.reader(original_file, delimiter=',')

    writer.writerow(get_headers(header_file).split(','))
    
    for row in reader:
        matchID = row[0]
        if matchID not in matchIDs and len(row) == 1150:
            writer.writerow(row)
        elif matchID in matchIDs:
            duplicates += 1
        matchIDs[matchID] = matchID
        count += 1

    print(f'Found {duplicates} "repeated match IDs out of {count} matches')
    new_file.close()
    original_file.close()
