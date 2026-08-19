from __future__ import annotations
from card import Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class GameBoard:
    """
    GameBoard class to store cards in draw pile and discard pile
    """

    def __init__(self, cards: ArrayList[Card]):
        """
        Constructor for the GameBoard class

        Args:
            cards (ArrayList[Card]): The list of cards to be used in the game

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) (Initialising instance variables and setting up the data structures)
            Worst Case Complexity: O(1)
        """
        self.draw_pile = cards
        self.discard_pile = ArrayList()

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) (Appending to the end of the discard_pile)
            Worst Case Complexity: O(1)
        """
        self.discard_pile.append(card)

        

    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(n) (n cards from discard pile are moved to temporary, shuffled, and moved back to draw pile)
            Worst Case Complexity: O(n)
        """
        temporary = ArrayList()

        while not self.discard_pile.is_empty():
            temporary.append(self.discard_pile.delete_at_index(0))
        
        RandomGen.random_shuffle(temporary)
        
        while not temporary.is_empty():
            self.draw_pile.append(temporary.delete_at_index(0))

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            Best Case Complexity: O(1) (If draw pile is not empty)
            Worst Case Complexity: O(n) (draw pile is empty and reshuffle is called)
        """
        if len(self.draw_pile) == 0:
            self.reshuffle()
        return self.draw_pile.delete_at_index(0)
