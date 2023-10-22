input_file_path = 'rockyou.txt'
output_file_path = 'rockyou_mod.dic'

with open(input_file_path, 'r', errors='ignore') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:

        if line[0].isalpha() and 'a' <= line[0].lower() <= 'z':
            line = line.rstrip() + "0\n"
            output_file.write(line.capitalize())
