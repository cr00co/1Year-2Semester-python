from homework.AlchemyGame.combinations import COMBINATIONS

class AlchemyGame:
    def __init__(self):
        self.combinations = COMBINATIONS

        # Элементы, которые уже существуют при запуске игры. Добавляются по ходу игры(если player исследует новый)
        self.discovered = {"water", "fire", "earth", "air"}

    def combine(self, a: str, b: str) -> str | None:
        a, b = a.strip().lower(), b.strip().lower()

        # Оба элемента должны быть уже известны
        if a not in self.discovered or b not in self.discovered:
            missing = [e for e in (a, b) if e not in self.discovered]
            return f"Unknown element(s): {', '.join(missing)}"

        result = self.combinations.get(frozenset({a, b}))

        if result:
            is_new = result not in self.discovered
            self.discovered.add(result)
            tag = " ✨(new!)" if is_new else ""
            return f"{a} + {b} = {result}{tag}"
        return f"No reaction between '{a}' and '{b}'."

    def show_discovered(self):
        print("Discovered:", ", ".join(sorted(self.discovered)))

    def play(self):
        print("=== Alchemy Game ===")
        print("Type two elements separated by '+', or 'quit' to exit, 'list' to see discovered elements.")
        self.show_discovered()

        while True:
            raw = input("\n> ").strip()
            if raw.lower() == "quit":
                break
            if raw.lower() == "list":
                self.show_discovered()
                continue
            if "+" not in raw:
                print("Format: element1 + element2")
                continue

            parts = raw.split("+", 1)
            print(self.combine(parts[0], parts[1]))


if __name__ == "__main__":
    AlchemyGame().play()