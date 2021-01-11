""" Calculates total volume of all companies for previous 3 days and 
then filter out the companies whose volume exceeds the volume provided by
user i.e reference volume""" 
import os, sys, csv
path='F:\\KSE project data\\200 files'

files_list = os.listdir(path)

reference_volume = 50000
fields = []
company_volume = []
filtered_companies = []
filtered_companies_name = []

for num in range(3):
    with open(path+'\\'+files_list[num]) as csvfile:
        print('opened:', files_list[num])
        csvreader = csv.reader(csvfile)
        fields = next(csvreader) #Here used to eliminate header in csv files  
        """ 'next()' reads the first line of the file, when used again reads the
         next line and so on """

        print(fields)
        print(100*'*','\n')
        #print(len(list(csvreader))) #gives the 'number of rows minus now of rows already read'

        if num == 0:
            for each_row in csvreader:
                company_volume.extend([each_row[0], int(each_row[6]), 1])
                #[company_name, volume, #of volumes added(1 means none added yet)]
            
        else:
            for each_row in csvreader:
                if each_row[0] in company_volume:
                    current_volume = int(each_row[6])
                    volume_index = (company_volume.index(each_row[0]))+1 #selects the volume location of company
                    prev_volume =  int(company_volume[volume_index])
                    updated_volume = current_volume + prev_volume
                    company_volume[volume_index] = updated_volume
                    company_volume[volume_index+1] += 1
                    
                else:
                    company_volume.extend([each_row[0], int(each_row[6]), 1])
                

# with open(path+'\\'+'test file2.txt', 'w') as file:
#     file.write(str(company_volume))

counter = int(len(company_volume)/3) 
sequencer = 1

for count in range(counter): #filters out the companies according to given volume
    if company_volume[sequencer] > reference_volume:
        filtered_companies.extend([company_volume[sequencer-1], company_volume[sequencer]])
        filtered_companies_name.append(company_volume[sequencer-1])
    sequencer += 3

print(company_volume)
print(len(company_volume))
print(100*'*', '\n')
print(filtered_companies_name)
print(len(filtered_companies))

# with open(path+'\\'+'filtered companies.txt', 'w') as file:
#     file.write(str(filtered_companies))
#     file.write(str(filtered_companies_name))
