import weather_data   #import user-defined module weather_data
import datetime


#asking user to enter value 1 for temperatue,2 for windspeed and 3 for pressure and 0 to exit
val = int(input("enter the value"'\n' "1 for temperature "'\n'" 2 for windspeed"'\n' " 3 for pressure"'\n' "and 0 to exit: "'\n'))

date_format = '%Y-%m-%d %H:%M:%S'  #setting date format 

while val != 0:     #the loop exits when user enters 0
    
    if val == 1:

        # asking user to input date in above given format
        userdata_date=input("enter the date and time in yyyy-mm-dd hh:mm:ss format only :"'\n')
        
        
        
        try:

            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(userdata_date, date_format)
            
            temp_val=weather_data.temperature(userdata_date) # calling temperatue function from weather_data module

            print(f"temperature at the given {userdata_date} is :",temp_val)  #printing the temperature value at the given date and time
            val = int(input("enter the value"'\n' "1 for temperature "'\n'" 2 for windspeed"'\n' " 3 for pressure"'\n' "and 0 to exit: "))

        except ValueError:

            # printing the appropriate text if ValueError occurs
            print("Incorrect data format, should be %Y-%m-%d %H:%M:%S")

    elif val == 2:


        userdata_date=input("enter the date and time in yyyy-mm-dd hh:mm:ss format only :"'\n')
        
        try:

            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(userdata_date, date_format)
            
            windspeed_val=weather_data.windspeed(userdata_date) #calling windspeed function from weather_data module

            print(f"windspeed at the given {userdata_date} is :",windspeed_val)  #printing windspeed value at given date and time

            val = int(input("enter the value"'\n' "1 for temperature "'\n'" 2 for windspeed"'\n' " 3 for pressure"'\n' "and 0 to exit: "))

        except ValueError:

            # printing the appropriate text if ValueError occurs
            print("Incorrect data format, should be %Y-%m-%d %H:%M:%S")

    elif val == 3:
        
        
        userdata_date=input("enter the date and time in yyyy-mm-dd hh:mm:ss format only :"'\n')
        
        try:

            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(userdata_date, date_format)
            
            pressure_value=weather_data.pressure(userdata_date)

            print(f"pressure at the given {userdata_date} is :",pressure_value)
            
            val = int(input("enter the value"'\n' "1 for temperature "'\n'" 2 for windspeed"'\n' " 3 for pressure"'\n' "and 0 to exit: "))

        except ValueError:

            # printing the appropriate text if ValueError occurs
            print("Incorrect data format, should be %Y-%m-%d %H:%M:%S")

    else:
        print("enter valid number")
        val = int(input("enter the value"'\n' "1 for temperature "'\n'" 2 for windspeed"'\n' " 3 for pressure"'\n' "and 0 to exit: "))