
def hide_card(card_numder):
    if ' ' in card_numder:
        card_numder = card_numder.split()
        card_numder = ''.join(card_numder)
        res = ('*'*12) + card_numder[12::]
        return res
    else:
        res = ('*'*12) + card_numder[12::]
        return res



hide_card(input())