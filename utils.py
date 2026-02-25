"""
Utility functions for student statistics.
Contains functions to calculate average, minimum, and maximum scores.
"""


def calcul_moyenne(liste_notes):
    """
    Calculate the average of a list of scores.

    Args:
        liste_notes (list of float): List containing student scores.

    Returns:
        float: The average score.
    """
    if len(liste_notes) == 0:
        return 0

    somme = sum(liste_notes)
    moyenne = somme / len(liste_notes)

    return moyenne


def trouver_min(liste_notes):
    """
    Find the minimum value in a list of scores.

    Args:
        liste_notes (list of float): List containing student scores.

    Returns:
        float: The minimum score.
    """
    if len(liste_notes) == 0:
        return None

    return min(liste_notes)


def trouver_max(liste_notes):
    """
    Find the maximum value in a list of scores.

    Args:
        liste_notes (list of float): List containing student scores.

    Returns:
        float: The maximum score.
    """
    if len(liste_notes) == 0:
        return None

    return max(liste_notes)