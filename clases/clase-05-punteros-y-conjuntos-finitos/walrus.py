def ask_ok(prompt, retries = 4, complaint = "Yes or no, please!"):
    while True:
        if retries == 0:
            break
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        print(complaint)
        retries = retries - 1;
    return -1


walrus = False;
print(walrus)

print(walrus := True)

inputs = list()
while True:
    current = input("Ingrese algo: ")
    if current == "quit":
        break;
    inputs.append(current)
print(inputs)

inputs = list()
while (current := input("Escriba algo: ")) != "quit":
    inputs.append(current)
print(inputs)

def pot(a, b):
    if b == 0:
        return 1
    p = pot(a, b // 2)
    result = p * p
    if b % 2 == 1:
        result = result * a
    return result

for i in range(0, 11):
    print(pot(2, i))
