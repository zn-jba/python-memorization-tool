from db import Flashcard
from menu import Menu


class Flashcards:
    def __init__(self) -> None:
        self.is_running = True

    def run(self) -> None:
        while self.is_running:
            selection = Menu.get_menu_input(Menu.MENU_COMMANDS,
                                            Menu.print_main_menu)
            match selection:
                case "1":
                    self.add()
                case "2":
                    self.practice()
                case "3":
                    self.quit()

    def quit(self) -> None:
        self.is_running = False
        print("\nBye!")

    @staticmethod
    def add() -> None:
        while True:
            selection = Menu.get_menu_input(Menu.ADD_MENU_COMMANDS,
                                            Menu.print_add_sub_menu)

            if selection != "1":
                break

            question = Menu.get_add_input("Question:\n")
            answer = Menu.get_add_input("Answer:\n")
            Flashcard.add_flashcard(question, answer)

    @staticmethod
    def practice() -> None:
        if not (cards := Flashcard.find_all()):
            print("There is no flashcard to practice!\n")
            return

        for card in cards:
            print(f"\nQuestion: {card.question}")
            selection = Menu.get_menu_input(Menu.PRACTICE_MENU_COMMANDS,
                                            Menu.print_practice_menu)

            match selection:
                case "y":
                    print(f"Answer: {card.answer}")
                    selection = Menu.get_menu_input(Menu.LEARNING_MENU_COMMANDS,
                                                    Menu.print_learning_menu)
                    Flashcards.move_card(card, selection == "y")
                case "n":
                    continue
                case "u":
                    Flashcards.update_card(card)

    @staticmethod
    def update_card(card: Flashcard) -> None:
        sub_selection = Menu.get_menu_input(Menu.PRACTICE_UPDATE_MENU_COMMANDS,
                                            Menu.print_practice_update_menu)
        Flashcards.delete_card(card) if sub_selection == "d" else Flashcards.edit_card(card)

    @staticmethod
    def move_card(card: Flashcard, was_correct: bool) -> None:
        Flashcard.update_card(card, box=card.box + 1 if was_correct else 1)

        if card.box > 3:
            Flashcards.delete_card(card)

    @staticmethod
    def delete_card(card: Flashcard) -> None:
        Flashcard.delete_card(card)

    @staticmethod
    def edit_card(card: Flashcard) -> None:
        print(f"current question: {card.question}")
        new_question = input("please write a new question:\n")
        print(f"current answer: {card.answer}")
        new_answer = input("please write a new answer:\n")
        Flashcard.update_card(card=card,
                              question=new_question if new_question else None,
                              answer=new_answer if new_answer else None)
