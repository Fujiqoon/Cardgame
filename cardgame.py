from random import shuffle

class Cards:
    values=[None,None,'2','3','4','5',
        '6','7','8','9','10','Jack',
        'Queen','King','Ace']
    suits=['spade','diamond','heart','club']
    
    #Cardはsuitとvalueの2つのパラメーターを持つinstanseを作る
    def __init__(self,v,s):
        self.value=v
        self.suit=s
    
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        else:
        	False

    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        else:
            return False
    def __repr__(self):
        v=self.values[self.value]+"of"+self.suits[self.suit]
        return v

class Deck():
	#Deckのinstanseには全てのcardが入る
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Cards(i,j))
        shuffle(self.cards)
    #rm_cardはcardリストが0になるまでpopする
    def rm_cards(self):
        if len(self.cards)==0:
            return
        else:
            return self.cards.pop()

class Player():
	#Playerのinstanseの初期値設定
    def __init__(self,name):
        self.wins=0
        self.cards=None
        self.name=name

class Game():
	#Game instanseにDeck,Playerのinstanseも呼び出し
    def __init__(self):
        name1=input('Enter player1 name')
        name2=input('Enter player2 name')
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)
        
    def wins(self,winner):
        w='{} wins this round'.format(winner)
        print(w)
    
    def draw(self,p1n,p1c,p2n,p2c):
        d='{} of {},{} of {}.'
        d=d.format(p1n,p1c,p2n,p2c)
        print(d)
        
    def play_game(self):
        cards=self.deck.cards
        print('Begining the war!')
        while len(cards)>=2:#2人が引くことができる間
            m='q to quit.Any key to play'
            response=input(m)
            if response=='q':
                break
            p1c=self.deck.rm_cards()
            p2c=self.deck.rm_cards()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            
            if p1c>p2c:
                self.p1.wins=+1
                self.wins(self.p1.name)
                
            else:
                self.p2.wins=+1
                self.wins(self.p2.name)
                
        win=self.winner(self.p1,self.p2)
        print('War is over.Winner is {}.'.format(win))
            
    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return 'It was tie.'
            
game=Game()
game.play_game()
