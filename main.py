"""
Main program to test student statistics functions.
"""

import utils


def demander_notes():
    """
    Ask the user to input scores separated by spaces.

    Returns:
        list of float: List of scores.
    """
    while True:
        saisie = input("Enter student scores separated by spaces: ")

        if saisie.strip() == "":
            print("Invalid input. Please enter at least one score.")
            continue

        try:
            liste_notes = [float(note) for note in saisie.split()]
            return liste_notes
        except ValueError:
            print("Please enter valid numbers.")


def main():
    notes = demander_notes()

    print("Average :", utils.calcul_moyenne(notes))
    print("Minimum :", utils.trouver_min(notes))
    print("Maximum :", utils.trouver_max(notes))


if __name__ == "__main__":
    main()