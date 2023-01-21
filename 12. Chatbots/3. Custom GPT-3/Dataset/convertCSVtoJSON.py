import csv 
import json 



def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    print(jsonArray)

    with open('testdata.jsonl', 'w') as outfile:
        for i in jsonArray:
            json.dump(i, outfile)
            outfile.write('\n')
    
    # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
    #     jsonString = json.dumps(jsonArray, indent=4)
    #     jsonf.write(jsonString)
          
csvFilePath = r'Mental_Health_FAQ_Without_First_Column.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)