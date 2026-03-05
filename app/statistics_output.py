def print_statistics(stats):
    print("\nStatistics:\n------------")
    for key, value in stats.items():
        try:
            print(f"{key.capitalize()}: {round(value, 2)}")

        except Exception as e:
            print(f"{key.capitalize()}: {value}")