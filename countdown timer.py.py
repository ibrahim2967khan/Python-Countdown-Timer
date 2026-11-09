import time

def countdown():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    total_seconds = hours * 3600 + minutes * 60 + seconds

    print("\nCountdown Started!")

    while total_seconds > 0:
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60

        print(f"Time Left: {hrs:02d}:{mins:02d}:{secs:02d}")

        time.sleep(1)
        total_seconds -= 1

    print("\n Time's Up! Countdown Completed.")

def main():
    print("==========================")
    print("     COUNTDOWN TIMER")
    print("==========================")

    while True:
        print("\n1. Start Timer")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            countdown()

        elif choice == "2":
            print("Thank you for using Countdown Timer!")
            break

        else:
            print("Invalid choice! Try again.")

main()
    


