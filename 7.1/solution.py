programs_with_base = set()
all_programs = set()

for line in open('input.txt'):
    all_programs.add(line.split()[0])

    if '->' in line:
        programs = line.split('->')[1].split(',')

        for program in programs:
            programs_with_base.add(program.strip())

for program in all_programs:
    if program not in programs_with_base:
        print program
