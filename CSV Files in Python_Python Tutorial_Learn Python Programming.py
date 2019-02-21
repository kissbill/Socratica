path = "C:/Users/Hanokri/Downloads/Google Stock Market Data - google_stock_data.csv.csv"

#lines = [line for line in open(path)]

#print(lines[0])

#print(lines[1].strip())

#print(lines[1].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]

print(dataset[1])