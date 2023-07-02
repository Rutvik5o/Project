import os

print("******** Welcome to our Program of Slient Auction *********")

def find_winner(bidder_details):
    highest_bid=0
    winner=""

    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid=bidding_price
            winner=bidder


    print(f"Here is the list of all the bidder:{bidder_details}")
    print(f"The Winner is {winner} with a bid Price of {highest_bid}")


bidder_data={}
end_of_bidding=False
while not end_of_bidding:

    name=input("What is your name?")
    price=int(input("what is your Bid?"))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'Yes' or 'No':").lower()
    if more_bidders == 'no':
        end_of_bidding=True
        find_winner(bidder_data)

    elif more_bidders == "yes":
        os.system('cls')