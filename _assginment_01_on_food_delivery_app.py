# class resturant


def_int_(self, name):
ID, Food name, Quantity, Discount, Price, Stock

    self.name=Name
    self.food={1:{'Name':'Chicken Briyani','Quantity',:1, 'price':350.0.', 'Discount':80.0, 'stock'.7.0},
                2:{'Name':'Kadiachicken','Quantity':5.0,'price':200.0, 'Discount':70.0, 'stock':60.0},
                3:{'Name':'Mutton kurma','Quantity':4.0,'price':340.0,'Discount':30.0, 'Stock':70.0}
                4:{'Name':'Dahi kabab','Qunatity':4.6,'price':359.0,'Discount':73.0, 'Stock':80.0}
                5:{'Name':'italian champ','Quantity':1.0,'price':250.0, 'Discount':50.0,'Stock':40.0}
                6:{'Name':'Chicken noodles', 'Quantiy':1.0,'price':120.0, 'Discount':25.0, 'Stock':12.0}
                7:{'Name':'Chicken curry', 'Quantity':1.0, 'price':140.0, 'Discuont':14.0, 'Stock':14.0}
                8:{'Name':'Veg Noodles', 'Quantity':1.0, 'price':120.0,'Discount':12.0, 'Stock':1.0}
                9:{'Nmae':'Pizza', 'Quantity':1.0,'price':140.0,'Discount':14.0, 'Stock':12.0}
                10:{'Name':'Veg Pizza','Quantity': 'price':150.0,'Discount'15.0, 'Stock':10.0}
    self.food_ID=len(self.food)+1
    self.user_details={1:{"User Name":"Ballu", "phone no.": 12012013,"Email_ID":'rajkumargopu201@email.com','password':'FREEWORD','Address':'Hyderabad'}}
                      {2:{"User Name":"Viany", "Phone no": 123145151,"Email_ID":'vinai123@email.com''Password':'KRETHI SHETTY','Address': 'karimnager'}}
                      {3:{"User Name":"Raj", "phone no": 141141521, "Email_ID":'rajkumarks124@email.com','Password':'VAAGDEV8','aDRESS':'vijayanagaram'}} 
    self.ordered_item=[]
    self.iterator=1






#adimin functionalities


def admin_login(self):
    email=input("Enter your Email ID :")
    pas=input("Enter your password:")
    while self.iterator<=(len(self.admind_details):
        if len(self.admin_details)!=0
        if email==self.admin_details[self.iterator]["Email_ID"]andpas==self.admin_details[self.iterator]["Password"]:
            print("\n"4,"!! LOGIN SUCESSFULL!!","/n"2)
            while true:
                print(''*''31+"ADMIM PAGE"+''*''*31+"\n"
                                "\t(1)ADD FOOD\DRINKS\n"
                                "\t(2)EDIT SERVICES\n"
                                "\t(3)VIEW FOOD\n"
                                "\t(4)UPDATE FOOD STOCKS\n"
                                "\t(5) GO BACK\n"+''_''*72)
y= input("Enter the number only :")
if y=="1":
    self.food[x]["Name"]=input("Updated Food name: ")
    print(''\n!! Food Name Sucessfully Updated!!/n")
    elif y=="2":
        self.food[x]["quantity"]=float(input("Updated Quantity in values only :"))
    print("\n!! Food Quantity Sucessfully Updated!!\n")
    elif y="3":
        self.food[x]["price"]=float(input("Updated Discount price in Rs only :"))
        print("/n!! Food Price Sucessfully Updated!!/n")
        elif y=="4":self.food[x]["Discount]=float(input("Updated Discount in Rs only :")
        print(/n!! Food Discount Sucessfully Updated!!\n")
        elif y=="5":
        self.food[x]["Stock"]=float(input("Updated Discount price in Rs only"))
        print(\n!! Food Stock Sucessfully Updated!!\n")
        elif y==="6":
            print(Back")
            else: 
                print("!! Sorry Invalid Number !!\n")

            else:
                print(\n!! INcorrect Food ID!!\n")
            except Exception as e:
                print("\n!! Something went wong please try again !!/n")\

def view_foodfood(self):
    print("\n\n""*"*25,"AVALIABLE FOOD ITEMS ","*"20)
    PRINT("\n\nFOOD ID|  FOOD ITEM    |QUANTITY|PRICE(RS)|DISCOUN(RS)|STOCK(RS)")
if len(self.food)!=0:
    menu=[]
    for items in self .food:
        menu.append([item,self.fooditems["Name"],self.food[item]["Quantity"],self.food[items]["price"],self.food[item]["Discount"],self.food[items]["Stock"]])
        for i in menu:
            print("\n\n" . i[1],""*(20-len(i[1])), i[2], "\t", i[3],"\t\t", i[4])
        else:
            print("!! Sorry No Food items is Added !!\n")
        def delete_food_item(self):
            self.veiw_food()
            try:
                print("*"25," !!WRNING!!""*"*20)
                print('\n','*"17, "Food item will Delete Permenently",''*10,"\n")
                print("Enter the Food ID")
                x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("/n !! Food deleted sucesfully!!/n")
                print)"*"25,"UPDATED FOOD LIST","*"20)
                self.view_food()
                else:
                print('\n',''*17,"Incorrect food ID entered !",''*10,"\n")
                ecept exception ase:
                print("\n!! Something went wrong please try again!!n")



#USER FUNCTIONALITY

def user_register(self):
    tye:
    i= len(self.user_details)
    while i>0:
        user_name= input("Enter you full name :")
        phone_no=int(input("Enter your 10 digit phone number :")
        email= input("Enter you email id:"))
        password=input("Enter ou password")
        adress=inpu("Enter your city")
        for i in self . use-details.keys():
            if email==self .user_details[selfiterator]["Email_ID"]:
                print("\n"*4,"YOU ALREADY HAVE AN ACCOUNT ! ")
                print("\n"*4, "LOGIN FROM YOUR ACCOUNT or CREATE WITH NEW MAIL_ID !\n/n")
                break

            else:
                self.user_details[len(sel. use_details)]={"User Name" :user_name, "phone no":phoneno , "Email,"Password":passwprd"Address":adress}
            print("\n!! your account  is created sucessfully 11\n")
            prin(f"Welcome To {self. name}Restaurant\n")
            print(""*""30."USER _DETAILS","*"25)
            for i in self.user_details[len(self.user_details)]:
                print(I. ":", self.user_details[len(self.user_etails)][i])
                break
            break
        except Exception as e:
            print("\n!! Soomethng went wrong please try again !!\n")

       def user_LOgin(self):
        try:
            print("*"*25, "WELCOME TO".self.name."*"*20)
            email=input("Enter yourEmail ID :")
            pas=input(Enter your password:")
            if len(self/user_details)!=0:
                for i in self. user_details. keys():
                if email= self.user-details[self.iterator]["Email_ID"]and pas===self .user_details[self .iterator]["password"]
                print("\n"*4,"!! login sucess full!!")
                while true:
                    print("*"*31+ "USER ACCOUNT PAGE"+"*" *31+ "\n"
                                        "\t(1) NEW ORDER \n"
                                        "\t(2) MY HISTORY \n"
                                        "\t(3) PDATE PROFILE \n"
                                        "\t(4) GO BACK\n"+" -"*72)
                    z= input("Enter Key:")
                    if z== "T":
                        sef.place_order()
                        elifz=="2":
                        self.ordered_history()
                        elif z=="3":
                            self.update_details()
                            elif z=="4":
                                print("back"0
                                breakelif email==self.user_details[self.iterator]["Email_ID"]
                                ["emai_ID"]and pas!=self.user-details[self.iterator]["passwod"]):
                                print("YOU DONT HAVE AN ACCOUNT PLEASE CREATE ONE !\n|n|n")
                                break
                            else:
                                self.iterator+=1
                                except:
                                    pint("\n!! something went wrong please try again!!")
                                
                                deaf place_order(elf0;
                                payment=[]
                                try:
                                    print("\n\nFOODID | FOODITEM |QUANTITY |PRICE (rs)| DISCOUNT(rs)")
                                    
                                    if len(self.foood)!=0:
                                    menu=[]
                                    for items in self.food:
                                        menu.append([items.self.food[items]["Name"].self.food[items]
                                        ["Quantity"].selffood[items]["price"].self.food[items]["Discount"]])
                                        for i in menu:
                                            print("\n\n" .i[1]. ""*(20- len(i[1])).i[2]. "\t".i[3]."\t\t".i[4])
                                            while True :
                                                print("*"*31 +"*"*31 +"\n"
                                                                        "\t(1)PLACE ORDER \n")
                                                                        "\t(2)PAYMENT\n"
                                                                        "\t(3) GO BACK\n"+"_"*72)
                                                x=input("ypur Key:")
                                                if x=="1":
                                                    print("Enter the Food umber you want to order separtaed by comma")
                                                    y=input("you choice:").spilt(".")
                                                    for i in y:
                                                        z=int(i)
                                                        if z<=len(menu):
                                                            self.ordered_item.append(menu[z-1])
                                                            else:
                                                                print("We Don't have this Food item :".z)
                                                                print("Also make sureyou include 'COMMAS'! \for example:! 1,5,9,4'")
                                                                break
                                                            print("\n\n","*"*25<"YOUR ORDER ","8"*20, "\n")
                                                            print("\n\nFOOD ID|  FOODITEM  |QUANTITY| PRICE (RS) |DISCOUNT(RS)")
                                                            payment=[]
                                                            for i in self.ordeed_item:
                                                                payment=[]
                                                                print("\n\n",i[0],""*(20-len(i[1])), i[2], "\t", i[3], "\t", i[4])
                                                                x=i[3]-i[4]
                                                                payment.append(x)
                                                                print("\n\n'\t\tyour total payment is :" ,sum(payment),"RS")
                                                                elif x=="2':
                                                                    if len(self.ordered_item)==0:
                                                                        print(please make AN ORDER TO PAY")
                                                                        else:
                                                                            print("SUCESSFULLY PAID", sum(ayment)."RS")
                                                                            exit()
                                                                            elif x=="3":
                                                                                break
                                                                             else:
                                                                                print("!! invaild Number!!\n")
                                                                                except :
                                                                                    print("\N!! Something went wrong try again !!")

                                                                                def ordered_history(self):
                                                                                    print("\nList of previous ordered :")
                                                                                    if len(self.ordered_item)=0:
                                                                                        print("\n\n",i[0],"\t", ""*(20-len(i[1])),i[2], "\t" ,i[3])
                                                                                        
                                                                                    def update_details(self0:
                                                                                        try:
                                                                                            while True:
                                                                                                print("select Below Options to Update Your Profile Details\n")
                                                                                                print("*"*31+ "EDIT PROFILE PAGE"+"*"*31 +"\n"

                                                                                                                               "t(1) UPDATE NAME\n"
                                                                                                                               "\T(2) UPDATE PHONE NUMBER\n"
                                                                                                                               "\t(3) UPDATE EMAIL ID\n"
                                                                                                                               "\t(4) UPDATE PASWORD\n"
                                                                                                                               "\t(5) UPDATE ADDRESS\n"
                                                                                                                               "t(6) GO BACK\NN"+"_"*72)
                                                                                                print("1. Nmae\n2.Phone number\n3. EmailID\n4. Pssword\n5 Address\n6.Exit\n")
                                                                                                x=input()
                                                                                                if x=="T":
                                                                                                    self.user_details["User Name"]=input("Enter your updated full name :")
                                                                                                    print("\n!! Details Updated suceeessfully!!\n")
                                                                                                    elif x==2:
                                                                                                        self.iser_details["phone No."]=int(input("Enter your updated 10 digit phone number :")
                                                                                                        print("\n!! Details Updated suceessfully !!\n')
                                                                                                        elif x=="3":
                                                                                                            self.user_details["Email_ID"]=input("Enter your updated emil id:")
                                                                                                            print("\n!! Deatails Updated suceessfully !!")

                                                                                                        elif x=="4":
                                                                                                            self.user_details["Password"]=input9"Enter your updated password :")
                                                                                                            print("\n!! Detail Updated sucessfully !!")
                                                                                                        eilf x=="5":
                                                                                                            self.user_details["Address"]=input("Enter your Updated address with area PN code")
                                                                                                            print("\n!! Details Updated sucesfully !!\n")
                                                                                                        eilfx=="6":
                                                                                                        break
                                                                                                    else:
                                                                                                        print("\n!! Invalid Number Entered !!\n")

                                                                                                    if x in ["1","2","3","4","5"]
                                                                                                    for i in sef.user_details:
                                                                                                        print("Deatails Updated",i, ":",self>user_details[i])
                                                                                                    else;
                                                                                                    print("\\nplease Enter correct input\n")
                                                                                                    except exception as e:
                                                                                                        print("\n!! Something went wrong please try again!!\n")




                                                                                                    # CLASS EXECUTION BY CREATING INSTANCE


                                                                                                try:
                                                                                                    def main():
                                                                                                        instance=Restaurant("Ed_yoda-D_Dhoba")
                                                                                                        print("*"*28,  "WELCOME TO"instanc, name, "*"*24. "\n")
                                                                                                        while True :
                                                                                                            print("\n\n\n,""8'*31= "MAIN MENU""*"*32+"\n\n\n"
                                                                                                                                    "\t(1) ADMIN\n"
                                                                                                                                    "\t(2) USER\n"
                                                                                                                                    "\t(3) EXIT\n+"_"*72)
                                                                                                        x=input("please select your operation :")
                                                                                                        if x=="T":
                                                                                                            print("\nDEARADMIN PLEASE LOGIN !\n")
                                                                                                            instance.admin_login()
                                                                                                            elif x=="2':
                                                                                                                while True
                                                                                                                print("\n\n"*2,"*"*31+"USERPAGE'+ "*"*31="\n\n"
                                                                                                                                       "\t(1)CREATE ACCOUNT\n"
                                                                                                                                       "\t(2)LOGIN/n"
                                                                                                                                       "t(3) EXIT\n"+"_"*72)
                                                                                                                y=input9"\nyour choice:")
                                                                                                                if y=="T":
                                                                                                                    instance user_register()
                                                                                                                    elif y=="2":
                                                                                                                        instance.user_login()
                                                                                                                        elif y=="3":
                                                                                                                            breakelse:
                                                                                                                            print("/nInvalid Number")
                                                                                                                            elif x=="3":
                                                                                                                                breal
                                                                                                                                else:
                                                                                                                                    print("Invalid Number")
                                                                                                                                except Exceotiion as e :
                                                                                                                                    print("\n\nsomething went wromg please give input carefully ")


                                                                                                                            #calling the main function 
                                                                                                                             
                                                                                                                             
                                                                                                                             if_name_=='__main__':
                                                                                                                             main()
                                                                                                                             print("\n\n THANK YOU EVERYONE !! \n\n")                                                                            



                                                                                
                                                           

                                                                



                                                                                               