from __future__ import annotations
from player import Player
from game_board import GameBoard
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) (Initialising instance variables)
            Worst Case Complexity: O(1)
        """
        self.players = CircularQueue(15) # Circular queue to store players with maximum capacity of 15 players
        self.current_player = None # represents which player's turn to play
        self.current_color = None # represents the current color of the top card on the discard pile
        self.current_label = None # represents the current value of the top card on the discard pile
        self.game_board = None # represents the game board with draw pile and discard pile
        # All attributes are initialized to None and to be modified later in gaame

    def generate_cards(self) -> ArrayList[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayList[Card]: The list of Card objects generated
        """
        list_of_cards: ArrayList[Card] = ArrayList(Config.DECK_SIZE)
        idx: int = 0

        # Generate 4 sets of cards from 0 to 9 for each color
        for color in CardColor:
            if color != CardColor.BLACK:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards.insert(idx, Card(color, CardLabel.SKIP))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.REVERSE))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.DRAW_TWO))
                    idx += 1
            else:
                # Generate black crazy and draw 4 cards
                for i in range(4):
                    list_of_cards.insert(idx, Card(CardColor.BLACK, CardLabel.CRAZY))
                    idx += 1
                    list_of_cards.insert(
                        idx, Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
                    )
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, players: ArrayList[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayList[Player]): The list of players

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n) (loop through players to add cards to their hand, first drawn card is valid)
            Worst Case Complexity: O(n+m) (loop through players to add cards to their hand, draw card until a valid number card is drawn)
        """
        self.players = players
        deck = self.generate_cards()
        self.game_board = GameBoard(deck)

        # Each player get 7 cards at initialisation
        for _ in range(Config.NUM_CARDS_AT_INIT): 
            for player in self.players: # loop through each player
                card = self.game_board.draw_card() # draw a card from the draw pile
                player.add_card(card) # add the card to the player's hand

        # loop until a number card is drawn
        while True: 
            first_card = self.game_board.draw_card() # a top card from draw pile is drawn
            if first_card.label.value <= 9: # check if the card is a number card
                self.game_board.discard_pile.append(first_card) # Place it on the discard pile
                break # break the loop when a number card is drawn
            # loop again if not a number card
        
        self.current_color = first_card.color # update the current color
        self.current_label = first_card.label # update the current label
        self.current_player = None # remain None since the game has not yet started


    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity: O(1) (current player is None, return the first player // or current player index is 0 (first player))
            Worst Case Complexity: O(n)  (iterate through player list to get current player index)
        """
        if self.current_player is None: # after initialisation and before game starts
            self.current_player = self.players[0]
            return self.current_player # return the first player
        
        current_player_index = self.players.index(self.current_player) # get the index of the current player

        # get the index of the next player, loop back to 0 if current player is the last player
        next_player_index = (current_player_index + 1) % len(self.players) 

        return self.players[next_player_index] # return the next player
    
    def reverse_players(self) -> None:
        """
        Method to reverse the order of the players

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n) (iterate through player list to reverse the order)
            Worst Case Complexity: O(n)
        """
        reversed_lst = ArrayList(len(self.players)) # create a new empty ArrayList to store the reversed players

        # loop through self.players from the last player to the first player
        for i in range(len(self.players) - 1, -1, -1):  
            # add the players in reversed order to reversed_lst
            reversed_lst.append(self.players[i])
        
        self.players = reversed_lst # update self.players to the reversed_lst

    def skip_next_player(self) -> None:
        """
        Method to skip the next player in the game

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n) (calls next_player() method to get the next player)
            Worst Case Complexity: O(n)
        """
        self.next_player() # skip current player and move on to next player

    def play_draw_two(self) -> None:
        """
        Method to play a draw two card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n) (Draw 2 cards to the next player)
            Worst Case Complexity: O(n)
        """
        next_player = self.next_player()
        # draw 2 cards for next player
        for _ in range(2): 
            self.draw_card(next_player, False)

        # skip their turn and move to the next player
        self.current_player = self.next_player()

    def play_black(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) (Black Crazy Card is played, only set current_color)
            Worst Case Complexity: O(n) (Black Draw Four Card is played, draw 4 cards for next player)
        """
        # set current_color to a randomly chosen color excluding Black when a Black card is played
        self.current_color = CardColor(RandomGen.randint(0,3))

        # If the card played is Black Draw Four
        # make the next player draw 4 cards and skip their turn
        if card.label == CardLabel.DRAW_FOUR:
            # draw 4 cards for next player
            next_player = self.next_player()
            for _ in range(4):
                self.draw_card(next_player, False)
            
    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity: O(1) (draw a card from the draw pile and add it to the end of the player's hand without needing to shift cards)
            Worst Case Complexity: O(n) (draw a card from the draw pile, sort and add it to the player's hand, shifting cards to the right of the added card // or plays the card directly)
        """
        card = self.game_board.draw_card() # draw a card from the draw pile

        player.add_card(card) # add the card to the player's hand 

        # check if the card can be played
        if playing and (card.color == self.current_color or card.label == self.current_label or card.color == CardColor.BLACK):
            player.play_card(self.current_color, self.current_label) # play the card if it can be played
            return card # play the card if it can be played
        
        return None

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """
        
        self.current_player = self.next_player() # get the first player to play
        round_num = 1 # round number starts from 1
        
        while True: # loop until a player wins

            played_card = self.current_player.play_card(self.current_color, self.current_label)

            if played_card:
                self.game_board.discard_pile.append(played_card)
                self.current_color = played_card.color
                self.current_label = played_card.label

                # Check if player has no cards left, return as winner
                if self.current_player.is_empty():
                    return self.current_player
                
                # If played card is a special card, perform the corresponding action
                if played_card.label == CardLabel.SKIP:
                    self.skip_next_player()
                elif played_card.label == CardLabel.REVERSE:
                    self.reverse_players()
                elif played_card.label == CardLabel.DRAW_TWO:
                    self.play_draw_two()
                elif played_card.color == CardColor.BLACK:
                    self.play_black(played_card)

            else:
                # Check if draw pile is empty
                if self.game_board.draw_pile.is_empty():
                    self.game_board.reshuffle()

                # Draw a card if no card is played
                drawn_card = self.draw_card(self.current_player, True)

                # If the drawn card can be played, play it
                if drawn_card and (drawn_card.color == self.current_color or drawn_card.label == self.current_label or drawn_card.color == CardColor.BLACK):
                    self.game_board.discard_pile.append(drawn_card)
                    self.current_color = drawn_card.color
                    self.current_label = drawn_card.label
                    
                    # If played card is a special card, perform the corresponding action
                    if drawn_card.label == CardLabel.SKIP:
                        self.skip_next_player()
                        self.current_player = self.next_player()
                    elif drawn_card.label == CardLabel.REVERSE:
                        self.reverse_players()
                    elif drawn_card.label == CardLabel.DRAW_TWO:
                        self.play_draw_two()
                    elif drawn_card.color == CardColor.BLACK:
                        self.play_black(drawn_card)


            self.current_player = self.next_player()
            round_num += 1 # increment round number