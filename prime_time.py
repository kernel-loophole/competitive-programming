def doc_str():

    return '''
    You are playing a new solitaire game called Prime Time. You are given a deck of cards, 
    and each card has a prime number written on it. Multiple cards may have the same number.

Your goal is to divide the cards into two groups in such a way that 
the sum of the numbers in the first group 
is equal to the product of the numbers in the second group. Each card must 
belong to exactly one of the two groups, and each group must contain at least one card.
 The sum or product of a group that consists of a single card is simply the number on that card.'''
if __name__=="__main__":
    print(doc_str())