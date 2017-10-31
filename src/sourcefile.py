# Input data
import csv
import numpy as np
file = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/input/itcont.txt", 'r')
#print(file.read().split('|'))
yourResult = [line.split('|') for line in file.readlines()]

print("\n")
print("Original Input \n")
print(yourResult)

# SINGLE RECORD
print("\n")
print("Example of single record:\n")
print(yourResult[0])
print("\n")
# cleaned data
print("Cleaned file output:\n")
file2 = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/input/cleanedfile/cleaned.txt", "w")
array1 = []
for i in range(len(yourResult)):
    sr = yourResult[i]
    cmte_id = sr[0]
    zip1 = sr[10]
    date1 = sr[13]
    tr_amt = sr[14]
    other_id = sr[15]
# For Input File Consideration number 1
    if other_id == "":
     #   array1.append(float(tr_amt)) # Float data type is required here
        imtstr = [cmte_id, zip1, date1, tr_amt, other_id]
        myString1 = "|".join(str(elm) for elm in imtstr)

        print(myString1)

        #file2 = open("C:/Users/Rounak Kulkarni/Documents/Insight project/input/cleanedfile/cleaned.txt", "a")
        file2.write(myString1+"\n")
file2.close()
#print(array1)
#print(np.median(array1))

# code for zip
print("\n")
print("Zip output:\n")
file3 = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/input/cleanedfile/cleaned.txt", "r")
yourResult_f3 = [line.split('|') for line in file3.readlines()]

#print(yourResult_f3)
d = []
#array2 = []
file4 = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/output/medianvals_by_zip.txt", "w")
globalamt_for_zip = []
global_ziplist = []
count_for_tran = 0
for j in range(len(yourResult_f3)):
    sr1 = yourResult_f3[j]
    d = sr1[0]
    zip11 = sr1[1]
    zipq = zip11[:5]
    global_ziplist.append(int(zipq))
    for g in range(len(yourResult_f3)):
        rec = yourResult_f3[g]
        zipq1 = []
        zip111 = sr1[1]
        zipq1.append(str(zip11))
        zipq1 = zipq1[:5]
        for zipq1 in global_ziplist:
            globalamt_for_zip.append(float(sr1[3]))

        count_for_tran = count_for_tran + 1

    median1 = np.median(globalamt_for_zip)
 #   no_of_trans = len(globalamt_for_zip)
    total_amt = sum(globalamt_for_zip)
#deleteContent1(file4)
    imtstr1 = [d, zipq, median1, count_for_tran, total_amt]
    myString12 = "|".join(str(elm) for elm in imtstr1)

    print(myString12)

            # file2 = open("C:/Users/Rounak Kulkarni/Documents/Insight project/input/cleanedfile/cleaned.txt", "a")
    file4.write(myString12 + "\n")
file3.close()
file4.close()


# code for date
print("\n")
print("Date file output:\n")
file5 = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/input/cleanedfile/cleaned.txt", "r")
yourResult_f3da = [line.split('|') for line in file5.readlines()]

#print(yourResult_f3da)
dda = []
#array2 = []
file6 = open("C:/Users/Rounak Kulkarni/Documents/GitHub/find-political-donors-for-insight/output/medianvals_by_date.txt", "w")
globalamt_for_date = []
global_datelist = []
count_for_tranda = 0
for k in range(len(yourResult_f3da)):
    sr1da = yourResult_f3da[k]
    dda = sr1da[0]
    date = sr1da[2]
    global_datelist.append(int(date))
    for zipq1 in global_ziplist:
        globalamt_for_date.append(float(sr1da[3]))

        count_for_tranda = count_for_tranda + 1

    median1da = np.median(globalamt_for_date)
 #   no_of_trans = len(globalamt_for_zip)
    total_amtda = sum(globalamt_for_date)
#deleteContent1(file4)
    imtstr1da = [dda, date, median1da, count_for_tranda, total_amtda]
    myString12da = "|".join(str(elm) for elm in imtstr1da)

    print(myString12da)

            # file2 = open("C:/Users/Rounak Kulkarni/Documents/Insight project/input/cleanedfile/cleaned.txt", "a")
    file6.write(myString12da + "\n")
file5.close()
file6.close()

file.close()
