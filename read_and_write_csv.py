import csv

def csv_read(file = "user_details.csv"):

    try:
        with open(file, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            csv_list = list(csvreader)
            return csv_list

    except:
        return "No file found."

print(csv_read())

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
            csv_transform = csv.writer(target)
            for i in range(len(old_file)):
                row = []
                for k in range(len(old_file[i])):
                    if k in target_indices:
                        #print(target_indices)
                        row.append(old_file[i][k])

                csv_transform.writerow(row)
        #csv_transformed = list(csv_transformed)
            # csvreader = csv.reader(new_file, delimiter=",")
            # csv_transformed = list(csvreader)
            # #return csv_list
            # return csv_transformed
        with open(new_file, newline="") as csvnew:
            csvreread = csv.reader(csvnew, delimiter=",")
            csv_transformed = list(csvreread)
            for i in range(len(csv_transformed)):
                if csv_transformed[i] == []:
                    return "Invalid csv!"

            return csv_transformed



    except:
        return "Invalid"

tester1 = write_to_new("new_user_details.csv", [1, 2, 4])


print(tester1)