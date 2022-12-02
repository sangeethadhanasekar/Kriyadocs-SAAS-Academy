import feedparser
import csv
print("Select the subject category:")

li=['Animal_Behavior_and_Cognition','Biochemistry','Bioengineering','Bioinformatics','Biophysics','Cancer Biology','Cell Biology','Clinical Trials*','Developmental Biology','Ecology','Epidemiology*','Evolutionary Biology','Genetics','Genomics','Immunology','Microbiology','Molecular Biology','Neuroscience','Paleontology','Pathology','Pharmacology_and_Toxicology','Physiology','Plant_Biology','Scientific_Communication_and_Education','Synthetic_Biology','Systems_Biology','Zoology']
for i in range(1,len(li)+1):
    print("%d:"%i,li[i-1])
ch=int(input("enter the category no."))

feed = feedparser.parse("http://connect.biorxiv.org/biorxiv_xml.php?subject=%s"%li[ch-1].replace(" ",'_'))

print('Number of posts in RSS feeds :', len(feed.entries))
# open the file in the write mode
f = open('%s_file'%li[ch-1], 'w',encoding='UTF-8')

writer = csv.writer(f)

#

# close the file

writer.writerow(['Number of posts in RSS feeds :%d'%len(feed.entries)])
for i in range(1,len(feed.entries)+1):
    ans = []
    entry = feed.entries[i - 1]
    ans.extend([" title: %s"%str(entry.title)," abstract: %s"%str(entry.description)])
    writer.writerow(ans)

f.close()