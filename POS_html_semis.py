

"""
NAME: SARMIENTO, KYLE CHRISTIAN L.
SECTION:  CPE3-A 
STUDENT NUMBER: 1920213
HTML POS RECEIPT
"""

# POS_System program.
import webbrowser


print ("\t\t\t\t-----------------------------------")
print ("\t\t\t\t|   Welcome to Tagumpay Canteen!  |")
print ("\t\t\t\t| Walk in Hungry, Walk out happy! |")
print ("\t\t\t\t-----------------------------------\n")
#student_213 is a dictionary that contains the student's name, id, and course, this is the student's information
student_213 = {}     # dictionary of student information

print ("\nPlease enter the following details: \n")

menuprice_213= {
   # STORE MENU PRICE IN A DICTIONARY CALLED menuprice_213
    'Soda' : 29.25, 'Bottled Water' : 20.00, 'Coffee': 50.00, 'Tea': 35.50, 'Bread' : 15.00, 'Apple' : 20.50, 'Banana' : 15.00, 'Oranges' : 25.10, 'Tapsilog' : 80.99, 'Porksilog' : 80.99
}
menuqntty_213  = {
    # STORE MENU QUANTITY IN A DICTIONARY CALLED menuqntty_213
    'Soda': 4, 'Bottled Water' : 4, 'Coffee' : 2, 'Tea' : 2, 'Bread' : 1, 'Apple' : 5, 'Banana' : 5, 'Oranges' : 3, 'Tapsilog' : 5, 'Porksilog' : 4
}


addstudent_213 = 'Yes'  # variable that determines if the user wants to add another student
studentList_213= []     # list of students in the canteen stored in the dictionary student_213
studenttmp_213 = {}     # temporary dictionary that stores the student's information
file_name = 'POSReceipt.html'   # file name of the html file

while addstudent_213 == 'Yes':  # loop that runs until the user doesn't want to add another student
    studentname_213 = input("Enter Student Name: ").strip().title()
    studentid_213 = input("Enter Student ID: ").lower()
    yearlevel_213 = input("Enter Year Level: ").strip().title()
    course_213 = input("Enter Course & Section: ").strip().upper()

    
    #print all the details entered by the user
    print("\nStudent Name: ",studentname_213)
    print("Student ID: ", studentid_213)
    print("Year Level: ", yearlevel_213)
    print("Course & Section: ", course_213)
    #wallet amount is set to 150
    student_213['walletamount_213'] = round(150.00, 2) # wallet amount for student to spend on items in the menu (150.00)

     # Adding student information to dictionary as key-value pairs
    student_213["studentname_213"]=studentname_213  # student name is added to the dictionary
    student_213["studentid_213"]=studentid_213      # student id is added to the dictionary
    student_213["course_213"]=course_213   
    
    checkInformation_213 = input('\nAre you certain of your inputs? ("Yes"/"No"): ').strip().upper()
    if checkInformation_213 == 'YES':
        addstudent_213 = input('\nDo you want to add another Student? ("Yes"/"No" ): ').strip().title()
        a_student = student_213.copy()
        studentList_213.append(a_student)
    else:
        print('\nPlease re-enter the following details: ')
        continue

 
import datetime                         #import datetime module to get current date and time
now = datetime.datetime.now()           #variable now is set to current date and time
time_now = now.strftime("%H:%M:%S")      #variable time_now is set to current time

with open(file_name,'w') as f:        #open file name as f and write to it with the following information (w)
    message = '''
    <html>
    <head>
    <h1 style="border:#BDB76B; border-width:5px; border-style:solid;"> <font color="#FFFFE0">  <center> WELCOME TO TAGUMPAY CANTEEN!
    </center> </h1>
        <h2>
        <center>
        <div>
        <pre>
POINT OF SALES RECEIPT 
Lipa City, Batangas 
Date: '''+now.strftime("%Y-%m-%d")+'''   Time: '''+time_now+'''
Contact No.: (756) 1611/(404) 1321 
      
         </pre>
           </div>
        </center>
        </h2>
        
        <hr>
    </head>
  <style>
body {
  background-image: url('canteen.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
</html>'''
    f.write(message)


price_amount = 0    #declare a variable to store the total price of the transaction
store_profit = 0    #declare a variable to store the total profit of the store
total_store_profit = 0  #declare a variable to store the total profit of the store


anotherSTDNT_213 = 'Y'
while anotherSTDNT_213.upper() == 'Y':          # while loop that asks the user if they want to add another student
    id = input("\nEnter Student ID to verify: ")  # prompt the user to enter the student id
    flag=True                                   # flag is set to true, then it will be used to check if the student id is found in the list studentList_213
    for x in studentList_213:                   # for loop that iterates through the list studentList_213
        if x["studentid_213"] == id:

            print ("\n\t\t\t\t-------------------")
            print ("\t\t\t\t|   ID VERIFIED!  |")
            print ("\t\t\t\t-------------------\n")
            #print student name
            print("Student Name: ", x["studentname_213"])
            #print student id
            print("Student ID: ",id)
            print("Year Level: ", yearlevel_213)
            print("Course & Section: ", course_213)
            #studenttmp_213 is a temporary dictionary that stores the student information
            studenttmp_213 = x                  # studenttmp_213 is set to the dictionary x 
            flag=False                          # flag is set to false because the student id is found in the list studentList_213
            break
    if(flag):
      
        print ("\n\t\t\t\t--------------------")
        print ("\t\t\t\t|   ID NOT FOUND!  |")
        print ("\t\t\t\t--------------------\n")
    #ask the user if he/she wants to add another student and if yes, ask for the student details again
    anotherSTDNT_213 = input("\nDo you want to continue verifying  another Student?(Y/N): ")
    a_student = student_213.copy()     # copy the dictionary student_213 to a_student
    studentList_213.append(a_student)   # append the dictionary a_student to the list studentList_213
    if anotherSTDNT_213.upper() == 'Y': # if the user wants to add another student, ask for the student details again
        continue     
    def menu ():    # function that prints the menu, def menu () is called in the main function
        print ("\nPress 1: View the menu and the stocks.")
        print ("Press 0: Proceed to a transaction.")
        #   ask the user What would you like to do? plus the student name + :
        return input ("\nWhat would you like to do " + studenttmp_213["studentname_213"] + "? : ") # return the user input
    run = menu () # run is set to the function menu ()
    while True:   # while loop that runs until the user enters 0
        if run == '1':
            print("\n\t\t\t--------------------------------------------------------")
            print("\t\t\t|         TAGUMPAY CANTEEN --- MENU PRICES             |")
            print("\t\t\t--------------------------------------------------------\n")
            print ('\nHere are the menu prices: ')
           #use a for loop to print the menu prices
            for x in menuprice_213.keys():
                #add "php" to the price
                print (x, ":-----", menuprice_213[x], "Php")

            print("\n\t\t\t--------------------------------------------------------")
            print("\t\t\t|         TAGUMPAY CANTEEN --- MENU STOCKS             |")
            print("\t\t\t--------------------------------------------------------\n")
            print ('\nHere is the menu and stocks: ')
          #use a for loop to print the menu and stocks
            for x in menuqntty_213.keys():
                print (x, ':-----', menuqntty_213[x])

            run = menu () # run is set to the function menu (), which is called again
        if run == '0':    # if the user enters 0, break the loop and proceed to the transaction
            print("\t\t\t----------------------------------------------------------------------")
            print("\t\t\t|                        TAGUMPAY CANTEEN  ---  MENU                 |")
            print("\t\t\t----------------------------------------------------------------------\n")
            print("\t\t\t\t\t\tEXERCISES\n")
            print("\t\t\t\t|| Soda --- P29.95  \t\t|| Bottled Water --- P20.00\n")
            print("\t\t\t\t|| Coffee --- P50.00 \t\t|| Tea --- P35.50\n")
            print("\t\t\t\t|| Bread --- P15.00 \t\t|| Apple -- P20.50 \n")
            print("\t\t\t\t|| Banana --- P15.00 \t\t|| Oranges --- 25.10\n")
            print("\t\t\t\t|| Tapsilog --- P80.99 \t\t||  Porksilog --- P80.99\n")
           
        break
    
    orders = ''     #declare a variable to store the orders of the student (the user will enter the orders)
    pricefoeacrorder_213 = ''
    priceamount_213 = 0  #declare a variable to store the total price of the transaction
    addorder_213 = 'Yes'    #declare a variable to store the user input if he/she wants to add another order
    while addorder_213 == 'Yes':
            try:
                print('\nYour balance is Php ' + str(round(studenttmp_213['walletamount_213'],2)) + ':')
                order_213 = input("\nWhat would you like to order? : ").strip().title()
                print('\n'+ order_213 + ': Php ' + str(menuprice_213[order_213]) + ' (' + str(menuqntty_213 [order_213]) + ' remaining...)')
            except KeyError:
                print('\t\nSorry, please try again.')
                continue

            try:
                qty = int(input("\nHow many " + order_213 + ' do you want to order?: '))
                #compute the price of the added order
                priceamount_213 += float(menuprice_213[order_213]) * float(qty)  
                #subtract  the quantity of the added order from the stock
               

            except ValueError:
                print('\t\nSorry, we do not have enough ' + order_213 + ' in stock.')
                priceamount_213 = 0
                continue
            #use tr catch to catch the error if  the order quantity is greater than the stock quantity
            try:
                if int(qty) > menuqntty_213[order_213]:
                    #o not subtract the order quantity from the stock quantity
                    raise ValueError
            except ValueError:
                print('\t\nSorry, we do not have enough ' + order_213 + ' in stock.')
                priceamount_213 = 0
                continue
            #compute the price of the added order
            #if the wallet amount is less than the price of the added order, decline the order
            if studenttmp_213['walletamount_213'] < menuprice_213[order_213] * qty:
                print('\t\nSorry, you do not have enough money in your wallet.')
                priceamount_213 = 0
                continue
            else:
                #subtract the price of the added order from the wallet amount
                studenttmp_213['walletamount_213'] -= menuprice_213[order_213] * qty
                menuqntty_213[order_213] -= qty
                print ('Order processed.\n')
            # PRINT the selected order and the corresponding price amount. including the change.
                print ('\nYour order is: ', end="")
                print (order_213, end=" ")
                print ('\nQuantity: ', end="")
                print (qty, end=" ")
                print('Current price:')
                print('Php ' + str(round(priceamount_213, 2)))
                store_profit += priceamount_213
                pricefororder_213 = 0
                pricefororder_213 += menuprice_213[order_213] * qty
                orders += '----' + str(qty) + '-----' + order_213 + '---- Php '+str(pricefororder_213) +'<br>'
                addorder_213 = input('\nDo you want to add more? ("Yes"/"No"): ').strip().title()
       
            #compute the total store profit   
    anotherstudent_213 = input('Do you want to take other orders from other students? ("Yes"/"No"): ').strip().title() 
    total_store_profit += store_profit
    store_profit = 0  
    #display the price for each order and quantity
    



    if qty != 0:    #if the user entered any orders, print the total price amount
            with open(file_name,'a') as f: #open the file in append mode and store the data in the file
                #append means to add the data to the end of the file
                message = '''
<html>
    <body>
         <center>
						<table >
                         <table style="background-color:#FFFFE0;color:black;">
<tr style="background-color:#BDB76B;color:black;">
<th>Student Information</th><th>Data</th>
        <tr class="service">                     
							<tr class="tabletitle">  						
							</tr>
							<tr class="service">  
                            
								<td class="tableitem"><p class="itemtext">Student Name: </p></td>
								<td class="tableitem"><p class="itemtext">'''+ str(studenttmp_213['studentname_213']) +'''</p></td>
                            </center>
							</tr>
							<tr class="service">
								<td class="tableitem"><p class="itemtext">Student ID: </p></td>
							
								<td class="tableitem"><p class="itemtext">'''+ str(studenttmp_213 ['studentid_213']) +'''</p></td>
							</tr>
							<tr class="service">
								<td class="tableitem"><p class="itemtext">Course and Section: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(studenttmp_213['course_213']) +'''</p></td>
							</tr>                         
							<tr class="service">
								<td class="tableitem"><p class="itemtext">Wallet Balance: </p></td>
						
								<td class="tableitem"><p class="itemtext"> Php '''+ str(round(studenttmp_213['walletamount_213'],2)) +'''</p></td>
                          
							</tr>            
						</table>
        <p> 
        <table>
         <table style="background-color:#FFFFE0;color:black;">
<tr style="background-color:#BDB76B;color:black">
<th><pre>Qty    Order      Price</pre></th>
        <tr class="service">
        <tr class="service">
								<td class="tableitem"><p class="itemtext">'''+str(orders)+'''</p></td>
							</tr>							
                       </center>
						</table>               
    </body>
</html>'''
                f.write(message)

'''studenttmp_213['walletamount_213'] = studenttmp_213['walletamount_213'] - price_amount'''
#use of for loop to print the student information
for x in studenttmp_213.keys():
        print (x, ':-----', studenttmp_213[x])   
#compute the total amount of store has earned in the transaction
print('\nAmount earned by the Canteen: Php ' + str(round(priceamount_213, 2)))
#use for loop to print the menu quantities
for x in menuqntty_213.keys():
        print (x, ':-----', menuqntty_213[x])
        
print("\n\t\t\t------------------------------------------------------")
print("\t\t\t|                   TAGUMPAY CANTEEN                 |")
print("\t\t\t------------------------------------------------------\n")


print ('\nThank you for choosing Tagumpay Canteen!')
with open(file_name,'a') as f:
    message = '''
<html>
    <body>
      <center>
        <p> 
        <table>
         <table style="background-color:#FFFFE0;color:black;">
<tr style="background-color:#BDB76B;color:black;">

        <tr class="service">
        <tr class="service">
								

								<td class="tableitem"><p class="itemtext"> Total Bill : Php '''+ str(priceamount_213) +'''</p></td>
                            </center>
							</tr>
                      </center>
						</table>
        <h3>
         <center>
         <h3 style="background-color:#BDB76B;color:black;">
             TAGUMPAY CANTEEN --- MENU STOCKS :
                </center>
        </h3>
        <p>
            <center>
        <p> 
        <table>
         <table style="background-color:#FFFFE0;color:black;">
<tr style="background-color:#BDB76B;color:black;">
<th>MENU</th><th>STOCKS</th><th>PRICE</th> 
        <tr class="service">
        <tr class="service">
								<td class="tableitem"><p class="itemtext"> Soda: </p></td>

								<td class="tableitem"><p class="itemtext"> '''+ str(menuqntty_213 ['Soda']) +'''</p></td>  
                                <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213['Soda'])+'''</p></td>                      
							</tr>
                            	<tr class="service">
								<td class="tableitem"><p class="itemtext"> Bottled Water: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Bottled Water']) +'''</p></td>
                                 <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213['Bottled Water'])+'''</p></td>   
                        
							</tr>
                            	<tr class="service">
								<td class="tableitem"><p class="itemtext">  Coffee: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Coffee']) +'''</p></td> 
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Coffee'])+'''</p></td>   
                                          
							</tr>
                            <tr class="service">
								<td class="tableitem"><p class="itemtext">  Tea: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Tea']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Tea'])+'''</p></td>   
                        
							</tr>
                              <tr class="service">
								<td class="tableitem"><p class="itemtext"> Bread: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Bread']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Bread'])+'''</p></td>   
                        
							</tr>
                             <tr class="service">
								<td class="tableitem"><p class="itemtext">  Apple: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Apple']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Apple'])+'''</p></td>  
                        
							</tr>
                            <tr class="service">
								<td class="tableitem"><p class="itemtext"> Banana: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Banana']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Banana'])+'''</p></td>  
                        
							</tr>
                             <tr class="service">
								<td class="tableitem"><p class="itemtext"> Oranges: </p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Oranges']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Oranges'])+'''</p></td>  
                        
							</tr>
                             <tr class="service">
								<td class="tableitem"><p class="itemtext">Tapsilog:</p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Tapsilog']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Tapsilog'])+'''</p></td>  
                        
							</tr>
                             <tr class="service">
								<td class="tableitem"><p class="itemtext">Porksilog:</p></td>
						
								<td class="tableitem"><p class="itemtext">'''+ str(menuqntty_213 ['Porksilog']) +'''</p></td>
                                  <td class="tableitem"><p class="itemtext">Php ''' +str(menuprice_213 ['Porksilog'])+'''</p></td>  
                        
							</tr>		
                    </center>
						</table>          
    </body>

<center>
   <h2 style="border:#BDB76B; border-width:5px; border-style:solid;"> <font color="#FFFFE0";"background-color:#BDB76B  <center> Thank you for choosing Tagumpay Canteen!
    </center> </h2>

    </center> </h1>
    <h3 style="background-color:#BDB76B;color:black;"> <center>
    <br>Tagumpay Canteen || TC  © 2022<br>
    </center> </h3>    
    

</html>'''
    f.write(message)

webbrowser.open_new_tab(file_name)