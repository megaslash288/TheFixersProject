import csv

def retrieve_wage(name):
    #opens the csv for use as list of dictionaries
    with open('TradeIncome.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        list_of_dict_data = []
        for row in csv_reader:
            list_of_dict_data.append(row)
    #remove everything that isnt an annual earnings value
    list_of_dict_data = [element for element in list_of_dict_data if element["Trade"].startswith("Annual")]
    try: 
        dict_entry = [entry for entry in list_of_dict_data if name in entry["Trade"]]
        wageamount = dict_entry[0]["wage"]
        wageamount = float(wageamount)
        return wageamount
    except:
        print("I frew up")

