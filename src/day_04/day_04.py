import re

def has_equal_adjacent_digits(password: str) -> bool:
    return True if re.search(r'(.)(\1+)', password) else False


def has_equal_adjacent_two_digits(password: str) -> bool:
    matches = list(re.finditer(r'(.)(\1+)', password))
    matches = [match for match in matches if len(match.group(2)) == 1]
    return True if matches else False


def has_increasing_digits(password: str) -> bool:
    for i, digit in enumerate(password):
        if i < (len(password) - 1) and digit > password[i + 1]:
            return False
    return True


def right_passwords_count(passwords: list, adjacent_digits_function) -> int:
    right_passwords = []
    for i in passwords:
        password = str(i)
        if adjacent_digits_function(password) and has_increasing_digits(password):
            right_passwords.append(password)
    return len(right_passwords)


if __name__ == '__main__':
    passwords = range(240298, 784957)
    part_one = right_passwords_count(passwords, has_equal_adjacent_digits)
    part_two = right_passwords_count(passwords, has_equal_adjacent_two_digits)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
