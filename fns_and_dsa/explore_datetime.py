from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)


def calculate_future_date():
    # Ask user for number of days
    days = int(input("Enter number of days to add: "))
    
    current_date = datetime.now()
    
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    
    # Format: YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
