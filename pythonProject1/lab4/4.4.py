def is_lucky(ticket_number):
    half_length = len(ticket_number) // 2
    first_half = ticket_number[:half_length]
    second_half = ticket_number[half_length:]

    return sum(map(int, first_half)) == sum(map(int, second_half))


# Пример использования функции:
ticket1 = "385916"
ticket2 = "231002"

if is_lucky(ticket1):
    print("Билет", ticket1, "- счастливый")
else:
    print("Билет", ticket1, "- несчастливый")

if is_lucky(ticket2):
    print("Билет", ticket2, "- счастливый")
else:
    print("Билет", ticket2, "- несчастливый")