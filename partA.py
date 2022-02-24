import csv
import os

files = ['credits.csv', 'keywords.csv', 'links.csv', 'movies_metadata.csv', 'ratings_small.csv']
find_id = [2, 0, 2, 5, 1]
for i in range(len(files)):
    print("Removing duplicates from "+ files[i])
    rem_id = set()
    with open(files[i],'r',encoding='utf8') as in_file, open(files[i][:-4:] +'2' + files[i][-4::],'w',encoding='utf8') as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen or line in rem_id: continue # skip duplicate
            seen.add(line)
            rem_id.add(line[find_id[i]])
            out_file.write(line)
in_file.close()
out_file.close()

print("Correcting movies_metadata...")
with open('movies_metadata2.csv', newline='',encoding='utf8') as csvfile, open('movies_metadata3.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[6] != "imdb_id":
            row[6]=row[6][2::]
         spamwriter.writerow(row)
csvfile.close()
csvout.close()
        
print("Reading movies from movies_metadata...")
with open('movies_metadata3.csv', newline='',encoding='utf8') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     md_id_set = set()
     md_imdbid_set = set()
     for row in spamreader:
        md_id_set.add(row[5])
        md_imdbid_set.add(row[6])
csvfile.close()

id_set = set()
imdbid_set = set()


print("Reading movies from credits...")
with open('credits2.csv', newline='',encoding='utf8') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         if row[2] in id_set: continue
         id_set.add(row[2])
csvfile.close()

print("Reading movies from keywords...")
with open('keywords2.csv', newline='',encoding='utf8') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         if row[0] in id_set: continue
         id_set.add(row[0])
csvfile.close()

print("Reading movies from links...")
with open('links2.csv', newline='',encoding='utf8') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         if row[1] not in imdbid_set:
             imdbid_set.add(row[1])
csvfile.close()

for i in id_set:
   if i in md_id_set:
      md_id_set.remove(i)

for i in imdbid_set:
   if i in md_imdbid_set:
      md_imdbid_set.remove(i)

print("Removing movies from credits...")
with open('credits2.csv', newline='',encoding='utf8') as csvfile, open('credits3.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[2] in md_id_set: continue
         if row[0] == "cast":
             row[0] = "cred_cast"
         spamwriter.writerow(row)
csvfile.close()
csvout.close()

print("Removing movies from keywords...")
with open('keywords2.csv', newline='',encoding='utf8') as csvfile, open('keywords3.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[0] in md_id_set: continue
         spamwriter.writerow(row)
csvfile.close()
csvout.close()

print("Removing movies from links...")
movieid_rem = set()
with open('links2.csv', newline='',encoding='utf8') as csvfile, open('links3.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[1] in md_imdbid_set: continue
         spamwriter.writerow(row)
         movieid_rem.add(row[0])
csvfile.close()
csvout.close()

print("Removing movies from ratings...")
with open('ratings.csv', newline='',encoding='utf8') as csvfile, open('ratings2.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[1] in movieid_rem:
            spamwriter.writerow(row)
csvfile.close()
csvout.close()

print("Removing movies from ratings_small...")
with open('ratings_small2.csv', newline='',encoding='utf8') as csvfile, open('ratings_small3.csv', 'w',newline='',encoding='utf8') as csvout:
     spamreader = csv.reader(csvfile, delimiter=',')
     spamwriter = csv.writer(csvout)
     for row in spamreader:
         if row[1] in movieid_rem:
            spamwriter.writerow(row)
csvfile.close()
csvout.close()

print("Deleting temporary files...")
filelist = {"credits.csv", "credits2.csv", "keywords.csv", "keywords2.csv",\
            "links.csv", "links2.csv", "movies_metadata.csv", "movies_metadata2.csv",\
            "ratings.csv", "ratings_small.csv", "ratings_small2.csv"}
for f in filelist:
   if os.path.exists(f):
      os.remove(f)

print("Renaming files...")
filelist = {"credits3.csv", "keywords3.csv",\
            "links3.csv", "movies_metadata3.csv",\
            "ratings2.csv", "ratings_small3.csv"}
for f in filelist:
   os.rename(f,f[:-5:] + f[-4::])

