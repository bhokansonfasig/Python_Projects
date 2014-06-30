from random import *

#About computer levels:
##Level 0 - Plays completely randomly
##Level 1 - Learns to play lowest card in hand
##Level 2 - Learns that two players can't be holding the exact same card
##Level 3 - Learns to pay attention to discarded cards
##Level 4 - Learns how to remember what other players are holding
##Level 5 - Learns to discard if someone knows their hand

fulldeck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
topcard = []
discarded = []
hands = []
c1p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c1p2card = [0]
c1p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c1p3card = [0]
c1p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c1p4card = [0]
c2p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c2p1card = [0]
c2p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c2p3card = [0]
c2p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c2p4card = [0]
c3p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c3p1card = [0]
c3p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c3p2card = [0]
c3p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c3p4card = [0]
c4p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c4p1card = [0]
c4p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c4p2card = [0]
c4p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
c4p3card = [0]
revealed = [0, 0, 0, 0]
playersleft = []
protected = []

playnum = 0
compnum = 0

comp1diff = 0
comp2diff = 0
comp3diff = 0
comp4diff = 0

while (playnum<=1 or playnum>=5) or (compnum<=-1 or compnum>=5):
    playnum = eval(input("Total number of players: "))
    compnum = eval(input("Number of computer players: "))
    if playnum==compnum:
        comp1diff = eval(input("Computer 1 level: "))
    if playnum<=compnum+1:
        comp2diff = eval(input("Computer 2 level: "))
    if playnum<=compnum+2 and playnum>=3:
        comp3diff = eval(input("Computer 3 level: "))
    if playnum<=compnum+3 and playnum==4:
        comp4diff = eval(input("Computer 4 level: "))


############################################################

def checkhandend(deck,playersleft):
    if deck==[]:
        return True
    count = playersleft.count(0)
    if count==len(playersleft)-1:
        return True
    return False

def playerturn(turn,held):
    if protected.count(turn)!=0:
        protected.remove(turn)
    print("Your held card is:", held)
    draw_i = randrange(len(deck))
    draw = deck.pop(draw_i)
    print("You drew the card:", draw)
    if (held==7 and (draw==6 or draw==5)) or ((held==6 or held==5) and draw==7):
        discard = 7
        print("Forced to discard 7")
    else:
        discard = 0
    while discard!=held and discard!=draw:
        discard = eval(input("Choose a card to discard: "))
    discarded.append(discard)
    c1p2.remove(discard)
    c1p3.remove(discard)
    c1p4.remove(discard)
    c2p1.remove(discard)
    c2p3.remove(discard)
    c2p4.remove(discard)
    c3p1.remove(discard)
    c3p2.remove(discard)
    c3p4.remove(discard)
    c4p1.remove(discard)
    c4p2.remove(discard)
    c4p3.remove(discard)
    if turn==1 and discard==c2p1card[0]:
        c2p1card[0] = 0
    if turn==1 and discard==c3p1card[0]:
        c3p1card[0] = 0
    if turn==1 and discard==c4p1card[0]:
        c4p1card[0] = 0
    if turn==2 and discard==c1p2card[0]:
        c1p2card[0] = 0
    if turn==2 and discard==c3p2card[0]:
        c3p2card[0] = 0
    if turn==2 and discard==c4p2card[0]:
        c4p2card[0] = 0
    if turn==3 and discard==c1p3card[0]:
        c1p3card[0] = 0
    if turn==3 and discard==c2p3card[0]:
        c2p3card[0] = 0
    if turn==3 and discard==c4p3card[0]:
        c4p3card[0] = 0
    if turn==4 and discard==c1p4card[0]:
        c1p4card[0] = 0
    if turn==4 and discard==c2p4card[0]:
        c2p4card[0] = 0
    if turn==4 and discard==c3p4card[0]:
        c3p4card[0] = 0

    if discard==held:
        hands[turn-1] = draw
    else:
        hands[turn-1] = held
        
    if discard==8 and held==8:
        discarded.append(draw)
        index = playersleft.index(turn)
        playersleft[index] = 0
        hands[turn-1] = 0
        print("Player",turn,"knocked out of round")
    if discard==8 and draw==8:
        discarded.append(held)
        index = playersleft.index(turn)
        playersleft[index] = 0
        hands[turn-1] = 0
        print("Player",turn,"knocked out of round")
    if discard==6:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<5:
            tries += 1
            chose = eval(input("Choose a player to trade hands with: "))
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        if tries<5:
            hands[turn-1], hands[chose-1] = hands[chose-1], hands[turn-1]
            revealed[turn-1] = 1
            revealed[chose-1] = 1
            if turn==1 and chose==2:
                c2p1card[0] = hands[turn-1]
            if turn==1 and chose==3:
                c3p1card[0] = hands[turn-1]
            if turn==1 and chose==4:
                c4p1card[0] = hands[turn-1]
            if turn==2 and chose==1:
                c1p2card[0] = hands[turn-1]
            if turn==2 and chose==3:
                c3p2card[0] = hands[turn-1]
            if turn==2 and chose==4:
                c4p2card[0] = hands[turn-1]
            if turn==3 and chose==1:
                c1p3card[0] = hands[turn-1]
            if turn==3 and chose==2:
                c2p3card[0] = hands[turn-1]
            if turn==3 and chose==4:
                c4p3card[0] = hands[turn-1]
            if turn==4 and chose==1:
                c1p4card[0] = hands[turn-1]
            if turn==4 and chose==2:
                c2p4card[0] = hands[turn-1]
            if turn==4 and chose==3:
                c3p4card[0] = hands[turn-1]
    if discard==5:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5) and tries<5:
            tries += 1
            chose = eval(input("Choose a player to discard their hand: "))
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        if len(deck)>0:
            draw_i = randrange(len(deck))
            hands[chose-1] = deck.pop(draw_i)
        else:
            hands[chose-1] = topcard[0]
    if discard==4:
        protected.append(turn)
    if discard==3:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<5:
            tries += 1
            chose = eval(input("Choose a player to compare hands with: "))
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        print("Player",chose,"has a",hands[chose-1])
        if hands[chose-1]<hands[turn-1] and chose!=0:
            discarded.append(hands[chose-1])
            index = playersleft.index(chose)
            playersleft[index] = 0
            hands[chose-1] = 0
            print("Player",chose,"knocked out of round")
        if hands[turn-1]<hands[chose-1] and chose!=0:
            discarded.append(hands[turn-1])
            index = playersleft.index(turn)
            playersleft[index] = 0
            hands[turn-1] = 0
            print("Player",turn,"knocked out of round")
    if discard==2:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<5:
            tries += 1
            chose = eval(input("Choose a player's hand to view: "))
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        print("Player",chose,"has a",hands[chose-1])
        revealed[chose-1] = 1
    if discard==1:
        chose = 0
        cardchose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<5:
            tries += 1
            chose = eval(input("Choose a player's hand to guess: "))
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        while (cardchose<=1 or cardchose>=9) and tries<5:
            cardchose = eval(input("What card do you think they are holding? "))
        if cardchose==hands[chose-1] and tries<5:
            discarded.append(hands[chose-1])
            index = playersleft.index(chose)
            playersleft[index] = 0
            hands[chose-1] = 0
            print("Player",chose,"knocked out of round")
        elif tries<5:
            print("Player",chose,"does not have",cardchose)

def AIturn(turn,held,playnum,level):
    if protected.count(turn)!=0:
        protected.remove(turn)
    #print("Computer held card is:", held)
    draw_i = randrange(len(deck))
    draw = deck.pop(draw_i)
    #print("Computer drew the card:", draw)
    if (held==7 and (draw==6 or draw==5)) or ((held==6 or held==5) and draw==7):
        discard = 7
    else:
        discard = 0
    while discard!=held and discard!=draw:
        if level==0:
            discard_i = randint(0,1)
            if discard_i==0:
                discard = draw
            else:
                discard = held
        if level>=1:
            if draw<=held:
                discard = draw
            else:
                discard = held
        if level>=5 and level<10:
            if revealed[turn-1]==1 and discarded.count(1)!=5 and held!=8:
                discard = held
    print("Computer discarded",discard)
    discarded.append(discard)
    c1p2.remove(discard)
    c1p3.remove(discard)
    c1p4.remove(discard)
    c2p1.remove(discard)
    c2p3.remove(discard)
    c2p4.remove(discard)
    c3p1.remove(discard)
    c3p2.remove(discard)
    c3p4.remove(discard)
    c4p1.remove(discard)
    c4p2.remove(discard)
    c4p3.remove(discard)
    if turn==1 and discard==c2p1card[0]:
        c2p1card[0] = 0
    if turn==1 and discard==c3p1card[0]:
        c3p1card[0] = 0
    if turn==1 and discard==c4p1card[0]:
        c4p1card[0] = 0
    if turn==2 and discard==c1p2card[0]:
        c1p2card[0] = 0
    if turn==2 and discard==c3p2card[0]:
        c3p2card[0] = 0
    if turn==2 and discard==c4p2card[0]:
        c4p2card[0] = 0
    if turn==3 and discard==c1p3card[0]:
        c1p3card[0] = 0
    if turn==3 and discard==c2p3card[0]:
        c2p3card[0] = 0
    if turn==3 and discard==c4p3card[0]:
        c4p3card[0] = 0
    if turn==4 and discard==c1p4card[0]:
        c1p4card[0] = 0
    if turn==4 and discard==c2p4card[0]:
        c2p4card[0] = 0
    if turn==4 and discard==c3p4card[0]:
        c3p4card[0] = 0
        
    if discard==held:
        hands[turn-1] = draw
    else:
        hands[turn-1] = held
        
    if discard==8 and held==8:
        discarded.append(draw)
        index = playersleft.index(turn)
        playersleft[index] = 0
        hands[turn-1] = 0
        print("Player",turn,"knocked out of round")
    if discard==8 and draw==8:
        discarded.append(held)
        index = playersleft.index(turn)
        playersleft[index] = 0
        hands[turn-1] = 0
        print("Player",turn,"knocked out of round")
    if discard==6:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<25:
            tries += 1
            chose = randint(1,playnum)
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        if tries<25:
            print("Computer chose to trade hands with Player",chose)
            hands[turn-1], hands[chose-1] = hands[chose-1], hands[turn-1]
            revealed[turn-1] = 1
            revealed[chose-1] = 1
            if level>=4 and turn==1 and chose==2:
                c1p2card[0] = hands[chose-1]
            if level>=4 and turn==1 and chose==3:
                c1p3card[0] = hands[chose-1]
            if level>=4 and turn==1 and chose==4:
                c1p4card[0] = hands[chose-1]
            if level>=4 and turn==2 and chose==1:
                c2p1card[0] = hands[chose-1]
            if level>=4 and turn==2 and chose==3:
                c2p3card[0] = hands[chose-1]
            if level>=4 and turn==2 and chose==4:
                c2p4card[0] = hands[chose-1]
            if level>=4 and turn==3 and chose==1:
                c3p1card[0] = hands[chose-1]
            if level>=4 and turn==3 and chose==2:
                c3p2card[0] = hands[chose-1]
            if level>=4 and turn==3 and chose==4:
                c3p4card[0] = hands[chose-1]
            if level>=4 and turn==4 and chose==1:
                c4p1card[0] = hands[chose-1]
            if level>=4 and turn==4 and chose==2:
                c4p2card[0] = hands[chose-1]
            if level>=4 and turn==4 and chose==3:
                c4p3card[0] = hands[chose-1]
    if discard==5:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5) and tries<25:
            tries += 1
            chose = randint(1,playnum)
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        if chose!=0:
            print("Computer chose to make Player",chose,"discard their hand")
            if len(deck)>0:
                draw_i = randrange(len(deck))
                hands[chose-1] = deck.pop(draw_i)
            else:
                hands[chose-1] = topcard[0]
    if discard==4:
        protected.append(turn)
    if discard==3:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<25:
            tries += 1
            chose = randint(1,playnum)
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
            if level>=4 and turn==1 and c1p2card[0]!=0 and c1p2card[0]<hands[turn-1]:
                chose = 2
            if level>=4 and turn==1 and c1p3card[0]!=0 and c1p3card[0]<hands[turn-1]:
                chose = 3
            if level>=4 and turn==1 and c1p4card[0]!=0 and c1p4card[0]<hands[turn-1]:
                chose = 4
            if level>=4 and turn==2 and c2p1card[0]!=0 and c2p1card[0]<hands[turn-1]:
                chose = 1
            if level>=4 and turn==2 and c2p3card[0]!=0 and c2p3card[0]<hands[turn-1]:
                chose = 3
            if level>=4 and turn==2 and c2p4card[0]!=0 and c2p4card[0]<hands[turn-1]:
                chose = 4
            if level>=4 and turn==3 and c3p1card[0]!=0 and c3p1card[0]<hands[turn-1]:
                chose = 1
            if level>=4 and turn==3 and c3p2card[0]!=0 and c3p2card[0]<hands[turn-1]:
                chose = 2
            if level>=4 and turn==3 and c3p4card[0]!=0 and c3p4card[0]<hands[turn-1]:
                chose = 4
            if level>=4 and turn==4 and c4p1card[0]!=0 and c4p1card[0]<hands[turn-1]:
                chose = 1
            if level>=4 and turn==4 and c4p2card[0]!=0 and c4p2card[0]<hands[turn-1]:
                chose = 2
            if level>=4 and turn==4 and c4p3card[0]!=0 and c4p3card[0]<hands[turn-1]:
                chose = 3

        if tries<25:
            print("Computer compared hands with Player",chose)
        if hands[chose-1]<hands[turn-1] and tries<25:
            discarded.append(hands[chose-1])
            index = playersleft.index(chose)
            playersleft[index] = 0
            hands[chose-1] = 0
            print("Player",chose,"knocked out of round")
        if hands[turn-1]<hands[chose-1] and tries<25:
            discarded.append(hands[turn-1])
            index = playersleft.index(turn)
            playersleft[index] = 0
            hands[turn-1] = 0
            print("Player",turn,"knocked out of round")
    if discard==2:
        chose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<25:
            tries += 1
            chose = randint(1,playnum)
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        if tries<25:
            print("Computer viewed Player ",chose,"'s hand",sep='')
            #print("Player",chose,"has a",hands[chose-1])
            revealed[chose-1] = 1
        if level>=4:
            if turn==1 and chose==2:
                c1p2card[0] = hands[chose-1]
            if turn==1 and chose==3:
                c1p3card[0] = hands[chose-1]
            if turn==1 and chose==4:
                c1p4card[0] = hands[chose-1]
            if turn==2 and chose==1:
                c2p1card[0] = hands[chose-1]
            if turn==2 and chose==3:
                c2p3card[0] = hands[chose-1]
            if turn==2 and chose==4:
                c2p4card[0] = hands[chose-1]
            if turn==3 and chose==1:
                c3p1card[0] = hands[chose-1]
            if turn==3 and chose==2:
                c3p2card[0] = hands[chose-1]
            if turn==3 and chose==4:
                c3p4card[0] = hands[chose-1]
            if turn==4 and chose==1:
                c4p1card[0] = hands[chose-1]
            if turn==4 and chose==2:
                c4p2card[0] = hands[chose-1]
            if turn==4 and chose==3:
                c4p3card[0] = hands[chose-1]
    if discard==1:
        chose = 0
        cardchose = 0
        tries = 0
        while (chose<=0 or chose>=5 or chose==turn) and tries<25:
            tries += 1
            chose = randint(1,playnum)
            if tries<5 and level>=4 and turn==1 and c1p2card[0]!=0:
                chose = 2
            if tries<5 and level>=4 and turn==1 and c1p3card[0]!=0:
                chose = 3
            if tries<5 and level>=4 and turn==1 and c1p4card[0]!=0:
                chose = 4
            if tries<5 and level>=4 and turn==2 and c2p1card[0]!=0:
                chose = 1
            if tries<5 and level>=4 and turn==2 and c2p3card[0]!=0:
                chose = 3
            if tries<5 and level>=4 and turn==2 and c2p4card[0]!=0:
                chose = 4
            if tries<5 and level>=4 and turn==3 and c3p1card[0]!=0:
                chose = 1
            if tries<5 and level>=4 and turn==3 and c3p2card[0]!=0:
                chose = 2
            if tries<5 and level>=4 and turn==3 and c3p4card[0]!=0:
                chose = 4
            if tries<5 and level>=4 and turn==4 and c4p1card[0]!=0:
                chose = 1
            if tries<5 and level>=4 and turn==4 and c4p2card[0]!=0:
                chose = 2
            if tries<5 and level>=4 and turn==4 and c4p3card[0]!=0:
                chose = 3
            if playersleft.count(chose)==0:
                chose = 0
            if protected.count(chose)==1:
                chose = 0
        while (cardchose<=1 or cardchose>=9) and tries<50:
            tries += 1
            if level<2:
                cardchose = randint(2,8)
            if level==2:
                fulldeck.remove(hands[turn-1])
                cardchose = choice(fulldeck)
                fulldeck.append(hands[turn-1])
                fulldeck.sort()
            if level>=3:
                for i in range(len(discarded)):
                    fulldeck.remove(discarded[i])
                fulldeck.remove(hands[turn-1])
                cardchose = choice(fulldeck)
                for i in range(len(discarded)):
                    fulldeck.append(discarded[i])
                fulldeck.append(hands[turn-1])
                fulldeck.sort()
            if level>=4 and tries<30:
                if turn==1 and chose==2 and c1p2card[0]!=0:
                    cardchose = c1p2card[0]
                if turn==1 and chose==3 and c1p3card[0]!=0:
                    cardchose = c1p3card[0]
                if turn==1 and chose==4 and c1p4card[0]!=0:
                    cardchose = c1p4card[0]
                if turn==2 and chose==1 and c2p1card[0]!=0:
                    cardchose = c2p1card[0]
                if turn==2 and chose==3 and c2p3card[0]!=0:
                    cardchose = c2p3card[0]
                if turn==2 and chose==4 and c2p4card[0]!=0:
                    cardchose = c2p4card[0]
                if turn==3 and chose==1 and c3p1card[0]!=0:
                    cardchose = c3p1card[0]
                if turn==3 and chose==2 and c3p2card[0]!=0:
                    cardchose = c3p2card[0]
                if turn==3 and chose==4 and c3p4card[0]!=0:
                    cardchose = c3p4card[0]
                if turn==4 and chose==1 and c4p1card[0]!=0:
                    cardchose = c4p1card[0]
                if turn==4 and chose==2 and c4p2card[0]!=0:
                    cardchose = c4p2card[0]
                if turn==4 and chose==3 and c4p3card[0]!=0:
                    cardchose = c4p3card[0]
                
        if chose>0 and chose!=turn:
            print("Computer guesses that Player",chose,"has a",cardchose)
        if cardchose==hands[chose-1] and chose>0 and chose!=turn:
            discarded.append(hands[chose-1])
            index = playersleft.index(chose)
            playersleft[index] = 0
            hands[chose-1] = 0
            print("Player",chose,"knocked out of round")
        elif tries<25:
            print("Player",chose,"does not have",cardchose)
    

############################################################

if comp1diff>5:
    comp1diff = 0
if comp2diff>5:
    comp2diff = 0
if comp3diff>5:
    comp3diff = 0
if comp4diff>5:
    comp4diff = 0

draw_i = randrange(len(deck))
draw = deck.pop(draw_i)
topcard.append(draw)

draw_i = randrange(len(deck))
draw = deck.pop(draw_i)
hands.append(draw)
draw_i = randrange(len(deck))
draw = deck.pop(draw_i)
hands.append(draw)
if playnum>=3:
    draw_i = randrange(len(deck))
    draw = deck.pop(draw_i)
    hands.append(draw)
if playnum>=4:
    draw_i = randrange(len(deck))
    draw = deck.pop(draw_i)
    hands.append(draw)

for i in range(playnum):
    playersleft.append(i+1)

score1 = 0
score2 = 0
score3 = 0
score4 = 0
if playnum==2:
    maxscore = 7
if playnum==3:
    maxscore = 5
if playnum==4:
    maxscore = 4


turn_i = randrange(playnum)

while score1<maxscore and score2<maxscore and score3<maxscore and score4<maxscore:
    if turn_i>=len(playersleft) - 1:
        turn_i = 0
        count = playersleft.count(0)
        for i in range(count):
            playersleft.remove(0)
    else:
        turn_i += 1

    turn = playersleft[turn_i]

    if turn!=0:
        print("-------------------- Player",turn,"--------------------")

        if turn>(playnum-compnum):
            if turn==1:
                AIturn(turn,hands[turn-1],playnum,comp1diff)
            if turn==2:
                AIturn(turn,hands[turn-1],playnum,comp2diff)
            if turn==3:
                AIturn(turn,hands[turn-1],playnum,comp3diff)
            if turn==4:
                AIturn(turn,hands[turn-1],playnum,comp4diff)
        else:
            playerturn(turn,hands[turn-1])

        print("==================================================")
        #print(deck)
        #print(discarded)

    handover = checkhandend(deck,playersleft)

    if handover==True:
        winnerhand = 0
        for i in range(len(hands)):
            if hands[i]>winnerhand:
                winner = i+1
                winnerhand = hands[i]
        if winner==1:
            score1 += 1
            turn_i = playnum - 1
        if winner==2:
            score2 += 1
            turn_i = 0
        if winner==3:
            score3 += 1
            turn_i = 1
        if winner==4:
            score4 += 1
            turn_i = 2

        print("\nPlayer",winner,"wins this round. Scores are:\n")
        print("Player 1:",score1)
        print("Player 2:",score2)
        if playnum>=3:
            print("Player 3:",score3)
        if playnum>=4:
            print("Player 4:",score4)

        if score1==maxscore:
            print("\nPlayer 1 wins!")
        elif score2==maxscore:
            print("\nPlayer 2 wins!")
        elif score3==maxscore:
            print("\nPlayer 3 wins!")
        elif score4==maxscore:
            print("\nPlayer 4 wins!")
        else:
            print("Next round!\n")

        deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        topcard = []
        discarded = []
        hands = []
        c1p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c1p2card = [0]
        c1p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c1p3card = [0]
        c1p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c1p4card = [0]
        c2p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c2p1card = [0]
        c2p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c2p3card = [0]
        c2p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c2p4card = [0]
        c3p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c3p1card = [0]
        c3p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c3p2card = [0]
        c3p4 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c3p4card = [0]
        c4p1 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c4p1card = [0]
        c4p2 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c4p2card = [0]
        c4p3 = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        c4p3card = [0]
        playersleft = []
        protected = []
        
        draw_i = randrange(len(deck))
        draw = deck.pop(draw_i)
        topcard.append(draw)

        draw_i = randrange(len(deck))
        draw = deck.pop(draw_i)
        hands.append(draw)
        draw_i = randrange(len(deck))
        draw = deck.pop(draw_i)
        hands.append(draw)
        if playnum>=3:
            draw_i = randrange(len(deck))
            draw = deck.pop(draw_i)
            hands.append(draw)
        if playnum>=4:
            draw_i = randrange(len(deck))
            draw = deck.pop(draw_i)
            hands.append(draw)

        for i in range(playnum):
            playersleft.append(i+1)

        turn_i = winner - 2
        

