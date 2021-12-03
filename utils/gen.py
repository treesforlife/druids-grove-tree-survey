import csv

data_filename = './../data/survey.csv'

def main():
  with open(data_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0][:2] == 'DG':
        tree_id = row[0]
        print(tree_id)

main()
