def greet(name):
    """Return a friendly greeting."""
    clean_name = name.strip()
    if clean_name:
        return f"Привет, {clean_name}! Добро пожаловать на первый урок Python."
    return "Привет! Добро пожаловать на первый урок Python."


def main():
    name = input("Как тебя зовут? ")
    print(greet(name))


if __name__ == "__main__":
    main()
