name = 'ruwe_990nan❤💞💜'
clean_name = ''

for char in name:
    if char.isalpha() or char.isspace() or char == '_':
        clean_name += char

print(clean_name)
