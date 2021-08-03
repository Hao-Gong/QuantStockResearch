from dataLoad import load_from_file

path = './output/history_k_data.csv'

rows = load_from_file(path)
print(rows)