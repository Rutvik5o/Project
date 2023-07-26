Menu={
         "Latte":{

                   "Ingredients":{

                        "Water":200,
                        "Milk":150,
                        "Coffee":24,


                   },
                   "Cost":150,
                },


         "Espresso":{

                   "Ingredients":{

                        "Water":50,
                        "Coffee":18,

                        },
                        "Cost":100,

                   },

         "Cappuccino":{

                   "Ingredients":{

                        "Water":250,
                        "Milk":100,
                        "Coffee":24,

                        },
                        "Cost":200,
                   }

         }

Profit=0

Resources={
             "Water":500,
             "Milk":200,
             "Coffee":100,
}


def Check_Resources(Order_Ingredients):

      for item in Order_Ingredients:    #water #milk #coffee

        if Order_Ingredients[item]>Resources[item]:

            print(f"Sorry there is not enough {item}.")

            return False

        return True

def Process_Coins():

    print("Please Insert coins.")

    Total=0

    Coins_Five=int(input("How Many 5rs. Coins?"))

    Coins_Ten=int(input("How Many 10rs. Coins?"))

    Coins_Twenty=int(input("How Many 20rs Coins?"))

    Total=Coins_Five*5 + Coins_Ten*10 + Coins_Twenty*20

    return Total

def Is_Payment_Successful(Money_Received,Coffee_Cost):

    if Money_Received >= Coffee_Cost:

        global Profit

        Profit += Coffee_Cost

        Change=Money_Received - Coffee_Cost

        print(f"Here is your Rs: {Change} in change.")

        return True

    else:

        print("Sorry that's no enough money. Money Refunded.")

        return False

def Make_Coffee(Coffee_Name,Coffee_Ingredients):

    for item in Coffee_Ingredients:

         Resources[item]-= Coffee_Ingredients[item]

    print(f"Here is your {Coffee_Name}....☕ Enjoy:)!!!")


Is_on=True

while Is_on:

    Choice=input("What would you like to have?-> (Latte/Espresso/Cappuccino)")

    if Choice == "Off":

        Is_on=False

    elif Choice == "Report":

        print(f"Water = {Resources['Water']}ml")

        print(f"Milk = {Resources['Milk']}ml")

        print(f"Coffee = {Resources['Coffee']}g")

        print(f"Money= Rs{Profit}")

    else:

        Coffee_Type=Menu[Choice]

        print(Coffee_Type)

        if Check_Resources(Coffee_Typ
    e['Ingredients']):

            Payment=Process_Coins()

            if Is_Payment_Successful(Payment,Coffee_Type['Cost']):

                Make_Coffee(Choice,Coffee_Type['Ingredients'])



