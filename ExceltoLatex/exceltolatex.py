def exceltolatex (filename1, filename2):

	import pandas as pd

	table=pd.read_excel(filename1, header=None)

	m, n=table.shape

	cols='|'

	for p in range(0,n): 
		cols=cols+'c|'	


	f= open(filename2,"w+")

	f.write('\\begin{tabular}{'+cols+'}\hline \r\n')
	
	f.close()

	f= open(filename2,"a+")

	for p in range(0,m):
		for q in range(0,n-1):
			pqs=str(table.loc[p][q])
			f.write(pqs+'&')
		pqsn=str(table.loc[p][n-1])
		f.write(pqsn +'\\\\ \hline \r\n')
	f.write('\end{tabular}')

	f.close()



