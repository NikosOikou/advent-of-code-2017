registers = {}
max_ever = 0

for instruction in open('input.txt'):
    parsed = instruction.split()
    register = parsed[0]
    inc_dec = parsed[1]
    amount = int(parsed[2])
    variable = parsed[4]
    condition = instruction.split('if')[1].strip()
    condition = condition.replace(variable, "registers['%s']" % variable)

    if register not in registers:
        registers[register] = 0

    if variable not in registers:
        registers[variable] = 0

    if eval(condition):
        if inc_dec == 'inc':
            registers[register] += amount
        else:
            registers[register] -= amount
    current_max = max(registers.values())
    max_ever = max(current_max, max_ever)

print max_ever
