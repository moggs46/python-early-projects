# Program introduction
print ("SuperAltoTravel is a calculation program")
print ("It calculates needed cars and required time to travel for our train.")
print ("It calculates extra needed cars and percentage")
print ("These calculates are based on inputs of user.")
print ("This trip has 2 legs: Ottawa-Toronto and Quebec City-Ottawa")
print ("The user should provide the needed information for program.")

# Get inputs for passenger number and capacity limit
passenger_number = int(input("Enter Passenger Number (Number must be 0 or a positive number):"))   
capacity_limit = float(input("Enter Minimum Capacity Limit:"))

# Program rounds limit percentage to decimal
limit_percentage = round(capacity_limit / 100,3)

#Program calculates full car number
full_cars_number = passenger_number // 300
print("Full car number:",full_cars_number)

# Program calculates extra passengers number and percentage
extra_passengers = passenger_number - full_cars_number * 300
print ("Extra passenger:", extra_passengers)
print ("The percentage of extra passengers:", round((extra_passengers / 300 *100),1), "%")

# Calculation of needed cars
if (extra_passengers >= 300 * limit_percentage):     
    
   full_cars_number = full_cars_number + 1 # add a extra car if condition met.
   print("Sufficient passengers for an extra car")

elif (extra_passengers == 0):
    
    full_cars_number = full_cars_number 
    print("No extra passengers so no extra car")

elif (extra_passengers < 300 * limit_percentage):
    
    full_cars_number = full_cars_number
    print("Insufficient passengers for an extra car")


print ("Total car number:",full_cars_number)

# Define distance and speed identifiers 
distance_ottawa = 412 
distance_quebec_city = 444
normal_speed = 280 

# Starting point is Toronto
choose = "T-O"

if (choose == "T-O"):

    # Get inputs for wind information
    headt_wind = str(input("Is there a head wind? Y or N"))
    
    if (headt_wind == "Y"):
        # if condition met, reduce speed by 10% 
        estimatedt_time = round (distance_ottawa / (normal_speed * 9 / 10),1) 
        print ("Estimated arrival time to Ottawa :",estimatedt_time,"hr")
        estimatedq_time = estimatedt_time + round (distance_quebec_city / (normal_speed * 9 / 10),1)
        
    elif (headt_wind == "N"):
         # Get inputs for wind information
        tailt_wind = str(input("Is there a tail wind? Y or N:"))

         
        if (tailt_wind == "Y"):
            # if condition met, increase speed by 8%
            estimatedt_time = round ( distance_ottawa /(normal_speed + normal_speed * 8 / 100),1)
            print ("Estimated arrival time to Ottawa:",estimatedt_time,"hr")
            estimatedq_time = estimatedt_time + round (distance_quebec_city /(normal_speed + normal_speed * 8 / 100),1)
            
          
        elif(tailt_wind == "N"):
             # if condition met, the speed is normal speed.
             estimatedt_time = round (distance_ottawa / normal_speed,1)
             print ("Estimated arrival time to Ottawa:",estimatedt_time,"hr")
             estimatedq_time = estimatedt_time + round (distance_quebec_city / normal_speed,1)

    # Calculations for arrival time to Quebec city
    total_hour = int((estimatedt_time + estimatedq_time + 0.25)  * 60 // 60 ) # Calculation for hour
    total_minute = int(((estimatedt_time + estimatedq_time + 0.25)  - total_hour) * 60)  # Calculation for minute
    print("Arrival time at Quebec City:", total_hour, ":", total_minute, "PM")


    # Get input for to continue
    choose = str(input("Do you will continue to Quebec City?"
                       "if yes, type yes ; if no, type no:"))


    if (choose == "yes"):

        #if condition met, get input for new passengers number
        new_passenger_number = int(input("Enter New Extra and Additional Passenger Number (Number must be 0 or a positive number):"))
        total_passenger = passenger_number + new_passenger_number
        full_cars_number = total_passenger // 300
        extra_passengers = total_passenger - full_cars_number * 300

        
        # Calculation and conditions for extra car needed and total car needed.
        if (extra_passengers >= 300 * limit_percentage):
            full_cars_number = full_cars_number + 1 
            

        elif (extra_passengers == 0):
            full_cars_number = full_cars_number
            

        elif (extra_passengers < 300 * limit_percentage):
            full_cars_number = full_cars_number
            

        print ("New total needed car number is",full_cars_number) 

        # Get inputs for wind information
        heado_wind = str(input("Is there a head wind? Y or N:"))
       
        if (heado_wind == "Y"):
            # if condition met, reduce speed by 10% 
            estimatedo_time = round (distance_quebec_city / (normal_speed * 9 / 10) ,1)
            print ("Estimated arrival time to Quebec City:",estimatedo_time,"hr")


        elif (heado_wind == "N"):
              # Get inputs for wind information
              tailo_wind = str(input("Is there a tail wind? Y or N"))
             
              if (tailo_wind == "Y"):
                  # if condition met, increase speed by 8%
                  estimatedo_time = round (distance_quebec_city /(normal_speed + normal_speed * 8 / 100) ,1)
                  print ("Estimated arrival time to Quebec City:",estimatedo_time,"hr")
                  
              elif(tailo_wind == "N"):
                   # if condition met, the speed is normal speed.
                   estimatedo_time = round (distance_quebec_city / normal_speed, 1) 
                   print ("Estimated arrival time to Quebec City:",estimatedo_time,"hr")
        print("Estimated total time:", round (estimatedo_time + estimatedt_time + 0.25,1),"hr")
        print("Thank you for traveling with us")
             

    
    if (choose == "no"):
        print("Thank you for traveling with us")


   
input()



   




        
     

