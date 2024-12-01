from controller import Controller

def main():
    days = get_days()
    show_days(days)
    select_days(days)

def show_days(days: list) -> None:
    calendar_columns = 6
    calendar_rows = 24//calendar_columns
    for row in range(calendar_rows):
        row_one, row_two, row_three = "", "", ""
        for column in range(calendar_columns):
            day = days[(row)*calendar_columns + column]
            row_one += f"{day.board[0][0]}{day.board[0][1]}{day.board[0][2]}{day.board[0][3]}" + " "
            row_two += f"{day.board[1][0]}{day.board[1][1]}{day.board[1][2]}{day.board[1][3]}" + " "
            row_three += f"{day.board[2][0]}{day.board[2][1]}{day.board[2][2]}{day.board[2][3]}" + " "
        print(row_one+"\n"+row_two+"\n"+row_three+"\n")

def get_days() -> list:
    return Controller.set_days()

def select_days(days: list) -> int:
    print("Please select a day between 1 and 25 (all other numbers end the loop):")
    day = select_day()
    while day >= 1 and day <= 25:
        try:
            days = Controller.change_day_to_selected(days, day)
            gift = Controller.get_a_gift(days, day)
            show_gift(day, gift)
            show_days(days)
            day = select_day()
        except ValueError as e:
            print(e)
            print("Please select another day")
            day = select_day()

def select_day():
    print("Select a day")
    day = int(input())
    return day

def show_gift(day: int, gift: str) -> None:
    print(f"\nDay {day} has the following gift: {gift}\n")

if __name__ == "__main__":
    main()