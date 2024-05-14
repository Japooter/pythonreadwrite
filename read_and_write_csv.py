import csv

def csv_read(file = "user_details.csv"):

    try:
        with open(file, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            csv_list = list(csvreader)
            return csv_list

    except:
        return "No file found."

#print(csv_read()[0][2])

def write_to_new(new_file, columns, file = "user_details.csv"):

    try:
        with open(new_file, "w") as target:
            target_columns = []
            target_indices = []
            old_file = csv_read(file)
            for value in columns:
                #print(value)
                for header in range(len(old_file[0])):
                    #print(old_file[0][value])
                    #print(old_file[0])
                    #print(header)
                    if value == header:
                        target_columns.append(old_file[0][header])
                        target_indices.append(value)
        #return target_indices
            for i in range(len(old_file)):
                for k in range(len(old_file[0])):
                    if k in target_indices:
                        #print(target_indices)
                        csv_transformed = csv.writer(target)
                        csv_transformed.writerow(old_file[i][k])


    except:
        return "Invalid"

tester1 = write_to_new("attempt_4.csv", [1, 2, 4])

print(tester1)