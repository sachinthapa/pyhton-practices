import gzip
import csv 


def main():
    print("Writting names to names.txt from csv file....")
    
    with open('names.txt', "w", encoding = "utf-8") as destination:
        destination.writelines(readNames())
    
    print("Copying names from names.txt to sorted_names.txt ....")

    with open('names.txt', "r", encoding = "utf-8") as source, open(
            'sorted_names.txt', "w", encoding = 'utf-8') as destination:
        destination.writelines(sorted(source.readlines()))

    print("Finished writing from names to sorted_names.... ")    

def readNames():
    with open('name_basics.tsv', encoding="utf-8") as tsv_file:
        tsv = csv.reader(tsv_file, delimiter = '\t')
        next(tsv)
        for record in tsv:
            yield f"{record[1]}\n"

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")



readNames()
