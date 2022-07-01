from art import logo
print(logo)

def find_highest_bidder(bid_dic_para):
  highest_bid = 0
  # winner = ""?
  for bidder in bid_dic_para:
    bid_amount = bid_dic_para[bidder]
    if highest_bid < bid_amount:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} is the winner giving the highest bid of ${highest_bid}!")

bid_dic = {}
end_game = False
while not end_game:  
  name = input("What is your name?\n")
  price = int(input("What is your bid price?\n$"))  
  bid_dic[name] = price
  others = input("are there other users who want to bid? Type 'yes' or 'no'.\n").lower()
  if others == "no":
    end_game = True
    find_highest_bidder(bid_dic)   

    
 




      
    



   
    
  