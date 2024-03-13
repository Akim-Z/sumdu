letters = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")


def print_alphabet():
    alphabet = sorted(letters)
    alphabet = [f"{upper}{lower}" for upper, lower in zip(alphabet[:26], alphabet[26:])]
    print(", ".join(alphabet))


print_alphabet()
