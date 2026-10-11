# 20th github project -> Countdown Timer
print('----------Countdown Timer----------')
import time


def get_time_input():
    while True:
        try:
            hours = int(input("Hours (0-23): ") or 0)
            minutes = int(input("Minutes (0-59): ") or 0)
            seconds = int(input("Seconds (0-59): ") or 0)

            if hours < 0 or minutes < 0 or seconds < 0:
                print("Values cannot be negative.")
                continue
            if minutes > 59 or seconds > 59:
                print("Minutes and seconds must be 0-59.")
                continue

            total = hours * 3600 + minutes * 60 + seconds
            if total == 0:
                print("Total time must be greater than zero.")
                continue

            return total

        except ValueError:
            print("Please enter valid whole numbers.")


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def countdown(total_seconds):
    print(f"\nCountdown started: {format_time(total_seconds)}")
    print("Press Ctrl+C to stop early.\n")

    try:
        while total_seconds > 0:
            print(f"\rTime remaining: {format_time(total_seconds)}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1

        print(f"\rTime remaining: {format_time(0)}")
        print("\nTime's up!")

    except KeyboardInterrupt:
        print(f"\n\nTimer stopped at {format_time(total_seconds)}.")


def main():
    print("=" * 40)
    print("        COUNTDOWN TIMER")
    print("=" * 40)

    while True:
        total = get_time_input()
        countdown(total)

        again = input("\nStart another timer? (yes/no): ").lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
        print()



main()