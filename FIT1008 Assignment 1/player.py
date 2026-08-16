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
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

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
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Optional method for debugging.

        """
        pass

    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None

        Returns:
            str: The string representation of the player
        """
        return str(self)
