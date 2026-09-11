from search import search_web


def print_line():
    print("─" * 70)


def main():
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                                OSINT                                 ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()

    query = input("   Suchbegriff: ").strip()

    if not query:
        print("\n   Kein Suchbegriff eingegeben.")
        return

    print()
    print(f"   Suche nach: {query}")
    print("   Bitte warten...")
    print()

    results = search_web(query)

    if not results:
        print("  ❌ Keine Ergebnisse gefunden.")
        return

    print(f"   {len(results)} Ergebnisse gefunden")
    print()
    print_line()

    for i, result in enumerate(results, 1):
        print(f"  [{i}] {result['title']}")
        print(f"      🔗 {result['url']}")

        if result["snippet"]:
            print(f"       {result['snippet']}")

        print_line()

    while True:
        print()
        print("  Optionen:")
        print("  [Zahl]  Ergebnis auswählen")
        print("  [N]     Neue Suche")
        print("  [Q]     Beenden")

        choice = input("\n  ➜ ").strip().lower()

        if choice == "q":
            print("\n   Beendet.")
            break

        if choice == "n":
            main()
            break

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(results):
                selected = results[number - 1]

                print()
                print_line()
                print("   AUSGEWÄHLTES ERGEBNIS")
                print_line()
                print(f"  Titel:")
                print(f"  {selected['title']}")
                print()
                print(f"  Quelle:")
                print(f"  {selected['url']}")
                print()
                print(f"  Beschreibung:")
                print(f"  {selected['snippet']}")
                print_line()

                print()
                print("  [S]  Verschlüsselt speichern")
                print("  [B] ↩ Zurück")

                action = input("\n  ➜ ").strip().lower()

                if action == "s":
                    print("\n   Speichern kommt als nächster Schritt.")

                elif action == "b":
                    continue

            else:
                print("\n   Ungültige Nummer.")

        else:
            print("\n   Ungültige Auswahl.")


if __name__ == "__main__":
    main()
