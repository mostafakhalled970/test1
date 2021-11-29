import csv
import pandas as pd
import matplotlib.pyplot as plt

# path of csv file

file_data = pd.read_csv('D:\\tasks\\results_40.csv')


# Graph Count of Status

x = []
y = []
with open('D:\\tasks\\results_40.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[1])
                                                                #y.append((row[3]))
x =[ 'OK', 'NOK', 'FAUILT' ]
y = [1354, 38, 1274]
plt.bar(x, y, color='g', width=0.70, label="Status")
plt.xlabel('ID')
plt.ylabel('Status')
plt.title('IDs')


# count rows of file
file = open('D:\\tasks\\results_40.csv')
read_file = csv.reader(file)
no_of_lines = len(list(read_file))


# count data in col Status
Col_data = pd.DataFrame(file_data, columns=['Status'])
Status_Count = file_data.pivot_table(columns=['Status'], aggfunc='size')


# loop to search ID in CSV
while True:

    f_new = file_data[file_data['ID'] == input("please enter id:  ")]
    for i in file_data:
        if i=='ID':
            print('id is found',f_new)
            break
        else:
            print('not found')
            break
    break
print("total rows in file: ", no_of_lines)
print("count of: ", Status_Count)
plt.legend()
plt.show()