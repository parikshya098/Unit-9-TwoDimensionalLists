data = []
file1 = open("CarSales.txt","r")     
for line in file1: 
        line = line.replace("\n","")      
        line = line.split(",")    
        data.append(line)       
file1.close()

count = 0     
price = 0   
for car in data:       
        count += 1    
        price += float(car[1])      
averageprice = price / count         
print("{:>5} Total Cars - Average Price: ${}".format(count,round(averageprice)))    

car_make = input("Enter Car Make: ")  
while(car_make != ""): 
        currentcount = 0        
        currentprice = 0       
        for car in data:       
                if car[0] == car_make:
                        currentcount += 1 
                        currentprice += float(car[1])
        if(currentcount != 0): 
                current_average = currentprice/currentcount     
                print("{:>6}  Cars Sold".format(currentcount))
                print("${:>5}  Average Price".format(round(current_average)))
                difference = current_average - averageprice    
                percent_diff = (difference * 100) / averageprice
                print("{:>5}% Above/Below Average".format(round(percent_diff,2)))
        else:   
                print("Car Make Not Found")
        car_make = input("Enter Car Make: ")   