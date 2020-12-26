# importing nse from nse tools 
from nsetools import Nse 

# creating a Nse object 
nse = Nse() 

# # getting quote of the sbin 
# quote = nse.get_quote('sbin') 

# # printing comapny name 
# print(quote['companyName']) 

# # printing average price 
# print("Average Price : " + str(quote['averagePrice'])) 


# all_stock_codes = nse.get_stock_codes()
# print(all_stock_codes.keys())

for key, value in all_stock_codes.items() :


    print (key, value)

    