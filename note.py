import note_manager


def main():
    while True:
        print()
        print("Введите команду: 1 - новая заметка, 2 - прочитать заметку, 3 - изменить заметку, 4 - удалить заметку, 5 - список заметок, 6 - выход: ")
        command = input().lower()
        if command == "1":
            print("Введите заголовок заметки:")
            title = input()
            print("Введите заметку:")
            body = input()
            note_manager.add_note(title, body)
            print("Заметка успешно сохранена.")

        elif command == "2":
            print("Введите номер заметки:")
            note_id = int(input())
            note_manager.read_note(note_id)

        elif command == "3":
            print("Введите номер заметки:")
            note_id = int(input())
            print("Введите новый заголовок заметки:")
            new_title = input()
            print("Введите новое тело заметки:")
            new_body = input()
            note_manager.edit_note(note_id, new_title, new_body)

        elif command == "4":
            print("Введите номер заметки:")
            note_id = int(input())
            note_manager.delete_note(note_id)

        elif command == "5":
            note_manager.list_notes()

        elif command == "6":
            break

        else:
            print("Неверный номер. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()