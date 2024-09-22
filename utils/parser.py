def parse_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                highest_lowercase.append(item)

    highest_lowercase.sort(reverse=True)
    return numbers, alphabets, highest_lowercase[:1]  # Highest lowercase only
