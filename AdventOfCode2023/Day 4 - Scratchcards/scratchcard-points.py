import math

"""
The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. 
Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. 
You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. 
The first match makes the card worth one point and each match after the first doubles the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). 
Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! 
That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.
So, in this example, the Elf's pile of scratchcards is worth 13 points.

Take a seat in the large pile of colorful cards. How many points are they worth in total?

"""

def get_scratchcard_points():
     # Result sum
    scratchcard_points = 0
    
    # Input file with game data
    doc = open("scratchcards-input.txt", "r")

    for line in doc:
        # Filters out the card number prefix
        two_side_card = line.split(":")[1]

        winning_numbers, card_numbers = two_side_card.split("|")[0].split(), two_side_card.split("|")[1].split()

        # Match counter
        matches_per_round = 0

        for number in card_numbers:
            if number in winning_numbers:
                matches_per_round += 1 
        scratchcard_points += int(math.pow(2, matches_per_round - 1))
    print(f"Total scratchcard points: {scratchcard_points}")
    return scratchcard_points

"""
There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. 
So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. 
So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. 
This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

This time, the above example goes differently:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
Your copy of card 2 also wins one copy each of cards 3 and 4.
Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 
8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. 
In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?"""

def get_total_scratchcards():
     # Input file with game data
    doc = open("scratchcards-input.txt", "r")

    # Initialize dictionary with instances of scratchcards (one of each)
    card_count = len(doc.readlines())

    original_scratchcards = {}

    for i in range(card_count):
        original_scratchcards[str(i+1)] = 1

    # Gard number counter - could be fetched from input, but less splicing
    card_number = 1

    # Initalize dictionary that will remember what cards each card wins copy of 
    memoize_scratchcards = {}

    # Returns file read pointer to beginning of files since readlines() took it to EOF
    doc.seek(0)

    for line in doc:
        # Filters out the card number prefix
        two_side_card = line.split(":")[1]

        # Split input into winning numbers and a set of possible numbers that could match winning numbers
        winning_numbers, card_numbers = two_side_card.split("|")[0].split(), two_side_card.split("|")[1].split()

        # Number of matches - used to add copies
        number_of_matches = 0 
        
        # Identifies how many matches are found to determine which copies you win
        for number in card_numbers:
            if number in winning_numbers:
                number_of_matches += 1 
        
        list_of_copies_won = []

        # Creates a dictionary that stores for each card which card copies it wins. Serves as memoization for reference later. 
        for i in range(number_of_matches):
            list_of_copies_won.append(str(card_number + i + 1))
        
        memoize_scratchcards[str(card_number)] = list_of_copies_won
        card_number += 1

    # The true processing starts now
    # Have to loop through memoize dict to calculate true amount of copies
    for card_number in memoize_scratchcards.keys():
        magic_filter_function(card_number, memoize_scratchcards, original_scratchcards)
        
    number_of_scratchcards = 0
    
    for cards in original_scratchcards.values():
        number_of_scratchcards += cards
    
    print(f"Total number of scratchcards: {number_of_scratchcards}")
    return number_of_scratchcards
    
# Auxiliary function - recursively goes through each card
# Each card has a list of card copies it won 
# Iterates per card in list, identifies it as a copy to add to the original
# However, every copy in itself wins the same cards as the original
# We utilize memoized dictionary to loop through it all 
def magic_filter_function(card_number, memoize_scratchcards, original_scratchcard):
    for card_copy in memoize_scratchcards[card_number]:
        original_scratchcard[card_copy] += 1
        magic_filter_function(card_copy, memoize_scratchcards, original_scratchcard)

get_scratchcard_points()
get_total_scratchcards()