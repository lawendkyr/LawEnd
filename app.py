from crypto import encrypt, decrypt
import os

FILE = "encrypted_notes.txt"


def load_notes():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_note(note):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")


def main():
    while True:
        print("\n OSINT Encryptor")
        print("------------------")
        print("1. Notiz entschlüsseln")
        print("2. Neue Notiz verschlüsseln")
        print("3. Exit")

        choice = input("\nAuswahl: ")

        # ENTScHLÜSSELN
        if choice == "1":
            notes = load_notes()

            if not notes:
                print("\n Keine verschlüsselten Notizen vorhanden.")
                continue

            print("\n Verschlüsselte Notizen:\n")

            for i in range(len(notes)):
                print(f"{i + 1}. {notes[i]}")

            try:
                number = int(input("\nWelche Notiz möchtest du entschlüsseln? "))

                if number < 1 or number > len(notes):
                    print("\n Ungültige Auswahl.")
                    continue

                password = input("Passwort: ")

                try:
                    decrypted = decrypt(notes[number - 1], password)

                    print("\n Entschlüsselte Notiz:")
                    print("------------------------")
                    print(decrypted)
                    print("------------------------")

                except Exception:
                    print("\n Falsches Passwort!")

            except ValueError:
                print("\n Bitte eine Zahl eingeben.")

        # VERSCHLÜSSELN
        elif choice == "2":
            password = input("Passwort: ")
            text = input("Notiz: ")

            encrypted = encrypt(text, password)
            save_note(encrypted)

            print("\n Notiz verschlüsselt gespeichert.")

        # EXIT
        elif choice == "3":
            print("\n Programm beendet.")
            break

        else:
            print("\n Ungültige Auswahl.")


if __name__ == "__main__":
    main()
