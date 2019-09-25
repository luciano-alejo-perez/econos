import requests
import json
url='https://api.estadisticasbcra.com/merval_usd'
token=input('ingrese el token que obtuvo en https://estadisticasbcra.com/api/documentacion (insert your token): ')
headers={'Authorization': 'BEARER ' + token}
r = requests.get(url, headers=headers)
j=json.loads(r.text)

saveq1=input('quiere guardar el archivo json como .txt? (do you want to save json data as .txt?) Y or N: ')

if saveq1 =='Y':
	filename1=input('ingrese un nombre de archivo con extension .txt (insert .txt filename): ') 
	with open(filename1, 'w') as outfile:
	    json.dump(j, outfile)

saveq2=input('quiere guardar los datos como .csv? (do you want to save data as .csv?) Y or N: ')

if saveq2 == 'Y':
	import csv
	filename2=input('ingrese un nombre de archivo con extension .csv (insert .csv filename): ') 
	data = open(filename2, 'w')
	# create the csv writer object
	csvwriter = csv.writer(data)
	count = 0
	for cell in j:

	      if count == 0:

	             header = cell.keys()

	             csvwriter.writerow(header)
	
        	     count += 1

	      csvwriter.writerow(cell.values())

	data.close()


#print(j)