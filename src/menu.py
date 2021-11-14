from typing import Callable


class Menu:
    MENU_COMMANDS = ["1", "2", "3"]
    ADD_MENU_COMMANDS = ["1", "2"]
    PRACTICE_MENU_COMMANDS = ["y", "n", "u"]
    PRACTICE_UPDATE_MENU_COMMANDS = ["d", "e"]
    LEARNING_MENU_COMMANDS = ["y", "n"]

    @staticmethod
    def print_main_menu() -> None:
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")

    @staticmethod
    def print_add_sub_menu() -> None:
        print("1. Add a new flashcard")
        print("2. Exit")

    @staticmethod
    def print_practice_menu() -> None:
        print('press "y" to see the answer:')
        print('press "n" to skip:')
        print('press "u" to update:')

    @staticmethod
    def print_practice_update_menu() -> None:
        print('press "d" to delete the flashcard:')
        print('press "e" to edit the flashcard:')

    @staticmethod
    def print_learning_menu() -> None:
        print('press "y" if your answer is correct:')
        print('press "n" if your answer is wrong:')

    @staticmethod
    def get_menu_input(choices: list[str], menu: Callable) -> str:
        while True:
            menu()
            if (choice := input()) in choices:
                return choice
            print(f"\n{choice} is not an option\n")

    @staticmethod
    def get_add_input(message: str) -> str:
        while not (user_input := input(message)).strip():
            continue
        return user_input
