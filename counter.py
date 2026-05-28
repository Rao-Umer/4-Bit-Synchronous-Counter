import time


def synchronous_counter(start: int = 1, end: int = 10, delay: float = 0.5) -> None:
    if start > end:
        raise ValueError(f"Start value ({start}) must be less than or equal to end value ({end}).")
    if delay < 0:
        raise ValueError("Delay must be a non-negative number.")

    print(f"\n{'=' * 35}")
    print(f"   Synchronous Counter: {start} → {end}")
    print(f"{'=' * 35}\n")

    for number in range(start, end + 1):
        print(f"  Count: {number:>2}  {'✓' if number == end else '...'}")
        time.sleep(delay)

    print(f"\n{'=' * 35}")
    print("   Counter finished successfully!")
    print(f"{'=' * 35}\n")


def get_user_input() -> tuple:
    print("\n--- Custom Counter Setup ---")
    try:
        start = int(input("Enter start number  (default 1) : ") or 1)
        end   = int(input("Enter end number    (default 10): ") or 10)
        delay = float(input("Enter delay seconds (default 0.5): ") or 0.5)
        return start, end, delay
    except ValueError:
        print("\n[!] Invalid input detected. Running with default settings.\n")
        return 1, 10, 0.5


def main() -> None:
    print("\nWelcome to the Synchronous Counter!")
    print("------------------------------------")
    print("1. Run default counter (1 to 10)")
    print("2. Run custom counter")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        synchronous_counter()
    elif choice == "2":
        start, end, delay = get_user_input()
        try:
            synchronous_counter(start=start, end=end, delay=delay)
        except ValueError as e:
            print(f"\n[Error] {e}")
    elif choice == "3":
        print("\nGoodbye!\n")
    else:
        print("\n[!] Invalid choice. Running default counter.\n")
        synchronous_counter()


if __name__ == "__main__":
    main()
