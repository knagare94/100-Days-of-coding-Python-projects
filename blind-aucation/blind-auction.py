from art import logo
print(logo)
print("Welcome to the secret aucation program.")

bidder_info = {}

bidder_loop = True
while bidder_loop:
  bidder = input("What is you name?: ")
  bid = int(input("What's your bid?: "))
  bidder_info[bidder] = bid
  add_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if add_bidder == "yes":
  else:
    bidder_loop = False

max_value = 0
max_key = None
for key, value in bidder_info.items():
  if value > max_value:
        max_value = value
        max_key = key

print(f"The winner is {max_key} with a bid of {max_value}")
