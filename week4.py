'''import csv
#Read in a CSV file
with open("addresses.csv",'r')as cv:
    with open("addresses_copy.csv",'w',newline='') as cv_cpy:
        cv_cpy_writer=csv.writer(cv_cpy,delimiter=',')
        #Parse the data in the CSV file
        csvreader = csv.reader(cv, delimiter=',')
        for row in csvreader:
            print(row)
            #Write the data back to a CSV file
            cv_cpy_writer.writerow(row)'''

#Split a CSV file based on a filtering criteria 
# (for example all the rows containing a certain word in a certain column)



'''#Read a CSV file with name, number, street, city, 
#state, pin and create a new file containing state, 
#city,number of houses in the state/city into another CSV file?

import csv
city={}
state={}
def func_1():
        with open("file1.csv")as file:
            
            csvreader=csv.reader(file,delimiter=',')

            next(csvreader,None)
            for row in csvreader:
                try:
                    city[row[3].lower()]+=1
                except:
                    city[row[3].lower()]=1
                    
                try:
                    state[row[4].lower()]+=1
                except:
                    state[row[4].lower()]=1
func_1()   
with open("file1.csv")as file:
    with open("file1_copy.csv",'w',newline='') as cv_cpy:
            file1_writer=csv.writer(cv_cpy,delimiter=',')
            header=['state','city','number of houses in the state','number of houses in the city']
            file1_writer.writerow(header)
            csvreader=csv.reader(file,delimiter=',')
            next(csvreader,None)
            for r in csvreader:
                rows=[r[4],r[3],state[r[4].lower()],city[r[3].lower()]]
                print(rows)
                file1_writer.writerow(rows)

'''

