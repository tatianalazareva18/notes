import csv
import os
from datetime import datetime

# Имя файла для хранения заметок
NOTES_FILE = 'notes.csv'

# Класс для заметки
class Note:
    def __init__(self, note_id, title, body, date_created=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.date_created = date_created or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def update(self, title, body):
        self.title = title
        self.body = body
        self.date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def __repr__(self):
        return f"[{self.note_id}] {self.title} (Last modified: {self.date_created})"

# Чтение заметок из файла
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    
    notes = []
    with open(NOTES_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            note_id, title, body, date_created = row
            notes.append(Note(note_id, title, body, date_created))
    
    return notes

# Сохранение заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for note in notes:
            writer.writerow([note.note_id, note.title, note.body, note.date_created])

# Создание новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введиите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = Note(note_id, title, body)
    return note

# Выборка заметок по дате
def find_notes_by_date(notes, date):
    return [note for note in notes if note.date_created.startswith(date)]

# Вывод всех заметок
def list_notes(notes):
    if notes:
        for note in notes:
            print(note)
    else:
        print("Заметки не найдены.")

# Редактирование заметки
def edit_note_by_id(notes, note_id):
    for note in notes:
        if note.note_id == note_id:
            title = input(f"Введите новый заголовок (current: {note.title}): ")
            body = input(f"Введите новый текст (current: {note.body}): ")
            note.update(title, body)
            print("Заметка успешно обновлена.")
            return
    print("Заметка не найдена.")

# Удаление заметки
def delete_note_by_id(notes, note_id):
    for note in notes:
        if note.note_id == note_id:
            notes.remove(note)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")

# Основное меню приложения
def main():
    notes = load_notes()

    while True:
        print("\n--- Приложение Заметки ---")
        print("1. Все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Поиск заметки по дате")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            list_notes(notes)
        elif choice == '2':
            note = create_note()
            notes.append(note)
            save_notes(notes)
            print("Заметка успешно добавлена.")
        elif choice == '3':
            note_id = input("Введите идентификатор заметки для редактирования: ")
            edit_note_by_id(notes, note_id)
            save_notes(notes)
        elif choice == '4':
            note_id = input("Введите идентификатор для удаления: ")
            delete_note_by_id(notes, note_id)
            save_notes(notes)
        elif choice == '5':
            date = input("Введите дату (ГГГГ-MM-ДД) для поиска заметок: ")
            found_notes = find_notes_by_date(notes, date)
            list_notes(found_notes)
        elif choice == '6':
            save_notes(notes)
            print("EВыходg...")
            break
        else:
            print("Неверный параметр. Пожалуйста, попробуйте еще раз.")

if __name__ == '__main__':
    main()
