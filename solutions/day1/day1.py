

with open("input1.txt") as f:
    lines = f.readlines()

numbers = []

def parse_line(line:str, output:list):
    numbers = []
    for character in line:
        try:
            digit = int(character)
            numbers.append(digit)
        except ValueError as e:
            continue
    output.append((numbers[0] * 10) + (numbers[-1]))


for line in lines:
    parse_line(line, numbers)

print(sum(numbers))
print(len(numbers))


