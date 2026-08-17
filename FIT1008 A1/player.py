from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *


class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) 
            Worst Case Complexity: O(1) 
        """
        self.name = name
        self.hand = ArraySortedList(Config.NUM_CARDS_AT_INIT) # Initialize with a capacity of 20 cards
        

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) (If card is added to the end without shifting)
            Worst Case Complexity: O(n) (If inserted in the middle, elements are shifted)
        """
        self.hand.add(card)

    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return len(self.hand) == 0

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity: O(1) 
            Worst Case Complexity: O(1) 
        """
        return len(self.hand)

    def play_card(
        self, current_color: CardColor, current_label: CardLabel
    ) -> Card | None:
        """
        Method to play a card from the player's hand

        Args:
            current_color (CardColor): The current color of the game
            current_label (CardLabel): The current label of the game

        Returns:
            Card: The first card that is playable from the player's hand

        Complexity:
            Best Case Complexity: O(1) (If first card is playable)
            Worst Case Complexity: O(n) (Iterate through all cards if no card is playable)
        """
        for i in range(len(self.hand)):
            card = self.hand[i]
            if current_color == card.color or current_label == card.label:
                self.hand.remove(card)
                return card
        return None

    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Optional method for debugging.

        """
        return self.name

    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None

        Returns:
            str: The string representation of the player
        """
        return str(self)

