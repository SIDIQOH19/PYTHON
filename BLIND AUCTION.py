print('Welcome to the blind auction!')


def find_winner(bid_dictionary):
    winner = ''
    highest_bid = 0

    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


bids = {}
continue_bid = True

while continue_bid:
    name = input('Enter your name:')
    price = int(input('What is your bid: \n$'))
    bids[name] = price
    continue_bidding = input(
        "Are there any other bidders?. Choose 'Yes' or 'No'. \n").lower()
    if continue_bidding == 'no':
        continue_bid = False
        find_winner(bids)
    elif continue_bidding == 'yes':
        print('\n' * 10)
