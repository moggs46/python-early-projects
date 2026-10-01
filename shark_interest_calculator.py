#Constants for design
X= 10*"*"
SHARK = "\U0001F988"*3
#Description
print(f"{X:<15s}{SHARK:<3s}Welcome to Shark Interest \
      Calculator{SHARK:>2s}{X:>14s}\n")
print(80*"-")
print("***    %-14s***"%("Description"),) 
print("\U0001F534This program calculates three things:\
      \n\U0001F538the compound interest")
print("\U0001F538outstanding balance \n\U0001F538current balance.")
print("\u2005")
print("\U0001F534These values calculated based on the user input for:")
print("\U0001F538principal \n\U0001F538interest rate")
print("\u2005")
print("\U0001F534After every 5 weeks,program asks to user about their \
payments.")
print("\u2005")
print("\U0001F534When current balance equal or less than zero,\
program ends.\n")
print(80*"-")
#Program takes required inputs from user
print("Please, enter the asked values!")
name_loanee = str(input("\U0001F464Enter the loanee's name: "))
principal = int(input("\U0001F4B0Please enter the principal's amount: "))
principal_amount = principal
INTEREST = float(input("\U0001F4C8\
Please enter the interest rate as a percantage: "))
interest_rate = INTEREST / 100
print("\n")
#variables for calculations
week_number = 0
outstanding_interest = 0
paid_interest = 0


#Program runs until both of principal and interest paid
while(principal_amount > 0 or outstanding_interest > 0):
      W ="Week"
      I = "Interest"
      OI = "Out. Interest"
      OP = "Out. Principal"
      B ="Balance"
      PD = "Paid Total"
      DS ="$"
      print("-" * 100)
      print(f"{W:<6s}{I:>15s}{OI:>18s}{OP:>20s}{B:>15s}{PD:>15s}")
      print("-" * 100)
      while(week_number < 5):#Calculations continues until week 5

            #Calculations for compund interest, outsatnding principal and outstanding interest
            current_interest = (principal_amount + outstanding_interest)*\
                               interest_rate
            outstanding_interest = outstanding_interest + current_interest
            paid_interest = paid_interest + current_interest
            
            #Appropriate messages for each information
            print(f"{week_number + 1:<6}"
                  f"{round(current_interest, 2):>14}"
                  f"{round(outstanding_interest, 2):>17}"
                  f"{round(principal_amount, 2):>19}"
                  f"{round(principal_amount + outstanding_interest, 2):>14}"
                  f"{round(paid_interest, 2):>14}")
            
            week_number = week_number + 1

      #After 5 week is completed, program gives a 5 week summary
      print("\n----- 5 Week Summary -----")
      print("\U0001F538 Outstanding principal:", round(principal_amount, 2))
      print("\U0001F538 Outstanding interest:", round(outstanding_interest, 2))
      print("\U0001F538 Current balance:", round(principal_amount + \
                                                 outstanding_interest, 2))
      print("\U0001F538 Interest paid to date:", round(paid_interest, 2))
      print("--------------------------\n")
      #Program takes required inputs from user
      choose = str(input("\U0001F4B3Do you made a payment?(Y or N)"))

      #if choose is Y, program takes input for paymnet and made calculations again based on payment
      #if choose is different from Y, program only resets the week number
      if(choose == "Y"):
          print("\U0001F648\U0001F649\U0001F64AI hope you,",name_loanee,"\
,don't leave me \U0001F648\U0001F649\U0001F64A")
          payment = float(input("Enter the amount you pay: "))
          week_number = 0
          op_payment = payment/2
          oi_payment = payment/2

          if(principal_amount >= op_payment):
              principal_amount = principal_amount - op_payment
          else:
              leftover = op_payment - principal_amount
              principal_amount = 0
              oi_payment = oi_payment + leftover

          if(outstanding_interest >= oi_payment):
              outstanding_interest = outstanding_interest - oi_payment
          else:
              leftover2 = oi_payment - outstanding_interest
              outstanding_interest = 0
              principal_amount = principal_amount - leftover2
              if(principal_amount < 0):
                 principal_amount = 0
          
      else:
          print("I glad to continue working with you,",name_loanee)
          week_number = 0


     
#If principal and interest paid is equal to zero,programs gives a congrulation message
print("-"*80)
print("Well done")
print("-"*80)
print("\n\U0001F389 Loan fully paid! Congratulations,", name_loanee + "!")
print("I will miss you,",name_loanee)
          


import tkinter #Library for tkinter

window = tkinter.Tk()
window.geometry ("700x700")
window.title ("Loan Interest Calcuation")#Title of the window

window.attributes ("-topmost", True)
window.update_idletasks ()
window.attributes ("-topmost", False)
window.focus_force ()

canvas = tkinter.Canvas(window, height = 700, width = 700, bg="white") #features of window
canvas.pack()


#Variables for calculations 
total = principal + paid_interest
max_height = 400 
width = 100

#calculations based on initial principal and paid interest  
principal_height = int((principal / total) * max_height)
interest_height = int((paid_interest / total) * max_height)
principal_text = round(principal,2)
interest_text = round(paid_interest,2)

#The columns features such as coordinates, colour and texts.
canvas.create_rectangle(150, 600 - principal_height, 150 + width, 600,\
                        fill="blue")
canvas.create_text(150 + width // 2,600-principal_height - 20,\
                   text ="Principal $"+str(principal_text), fill = "blue")
canvas.create_rectangle(300, 600 - interest_height, 300 + width, 600, fill="red")
canvas.create_text(300 + width // 2,600-interest_height - 20, text ="Interest $"\
                   +str(interest_text), fill = "red")
canvas.create_text(400, 50, text ="Principal vs Interest Paid",\
                   font=("Helvetica", 14, "bold"))
canvas.create_text(350, 660, text="\U0001F4AC I will miss you... \U0001F988",\
                   font=("Courier", 10, "italic"), fill="gray")


canvas.update()

window.mainloop()


