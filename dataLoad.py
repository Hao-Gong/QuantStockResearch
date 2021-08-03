import csv


def load_from_file(path):
    rows = []
    with open(path,'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
            break;
    
    return rows