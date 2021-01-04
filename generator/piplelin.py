file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
lines_list = (line.rstrip().split(",") for line in lines)
cols = next(lines_list)

company_dict = (dict(zip(cols,data)) for data in lines_list)

#for data in company_dict:
#    print('\n')
#    for key,value in data.items():
#        print(f"key -> {key}, value -> {value}")


funding =(int(company["raisedAmt"]) for company in company_dict if company["round"] == "a")
total_series_a = sum(funding)

print(f'total -> {total_series_a}')


