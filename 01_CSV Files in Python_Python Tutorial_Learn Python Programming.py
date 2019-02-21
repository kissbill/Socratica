import csv
from datetime import datetime
#print(dir(csv)) #miket tartalmaz a modul

path = "C:/Users/Hanokri/Downloads/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) #the first line is the header
#data = [row for row in reader] # maradek adatok kiolvasasa

#print(header)
#print(data[0])

#Adat tisztitas , time , float es int -re
data = []
for row in reader:
	#row = [ Date , Open, High,Low, Close, Adj. Close]
	date = datetime.strptime(row[0], '%m/%d/%Y')
	open_price = float(row[1]) # 'open' egy beepitett fugybeny lenne
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])
	adj_close = float(row[6])

	data.append([data, open_price, high, low, close, volume, adj_close ])


#print(data[0])

#Kiiratas
#Megterules napi szinten

returns_path = "C:/Users/Hanokri/Downloads/Google Stock Market Data_return.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date","Return"])

for i in range(len(data) - 1): #utolso napnak nincs mivel hasonlitani
	todays_row = data[i]
	todays_date = todays_row[0]
	todays_price = todays_row[-1]
	yestarday_row = data[i + 1]
	yestarday_price = yestarday_row[-1]

	daily_return = (todays_price - yestarday_price) /yestarday_price
	#writer.writerow([todays_date,daily_return])
	formatted_date = todays_date.strptime('%m/%d/%Y')
	writer.writerow([formatted_date,daily_return])