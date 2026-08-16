from __future__ import annotations
from enum import auto, IntEnum
from config import Config
from data_structures import *


class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """

    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    BLACK = auto()

    def __str__(self) -> str:
        """
        Method to return the string representation of the CardColor

        Args:
            None

        Returns:
            str: The string representation of the CardColor
        """
        return self.name


class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """

    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()

    def __str__(self) -> str:
        """
        Method to return the string representation of the CardLabel

        Args:
            None

        Returns:
            str: The string representation of the CardLabel
        """
        return self.name


class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Initialize the card with the given color and value.

        Args:
            color (CardColor): The color of the card.
            label (CardLabel): The value of the card.

        Returns:
            None

        Complexity:
            Best Case: O(1) (initialise instance variables)
            Worst Case: O(1)
        """
        self.color = color
        self.label = label

    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Optional method for debugging.
        """
        return f"{self.color.name} {self.label.name}"

    def __repr__(self) -> str:
        """
        Method to return the string representation of the Card

        Args:
            None

        Returns:
            str: The string representation of the Card
        """
        return str(self)

    def __eq__(self, other: Card) -> bool:
        """
        Check if this card is equal to another card.

        Args:
            other (Card): The other card to compare to.

        Returns:
            bool: True if this card is equal to the other card, False otherwise.
        """
        return self.color == other.color and self.label == other.label

    def __lt__(self, other: Card) -> bool:
        """
        Method to compare two cards by color first, then label if colors are the same
        
        Args:
            other (Card): The other card to compare with the current card
            
        Returns:
            bool: True if the current card is less than the other card, False otherwise
        
        Complexity:
            Best Case Complexity: O(1) (If the colors are different, check once will do)
            Worst Case Complexity: 0(1)(If the colors are the same, one extra comparison is needed)
        """
        if self.color != other.color:
            return self.color < other.color
        return self.label < other.label
    
    def __le__(self, other: "Card") -> bool:
        """
        Compare if one card is less than or equal to another.

        Args:
            other (Card): The other card to compare with the current card.

        Returns:
            bool: True if the current card is less than or equal to the other card, False otherwise.

        Complexity:
            Best Case: O(1) (If the colors are different, a single comparison is enough)
            Worst Case: O(1) (If colors are the same, it needs one additional comparison)
        """
        return self < other or self == other