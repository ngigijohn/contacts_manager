import csv
contactsFile = open('contacts.csv', encoding='utf8')
contactsReader = csv.reader(contactsFile)
outputFile = open('output.csv', 'w', newline='', encoding='utf8')
outputWriter = csv.writer(outputFile)
outputReader = csv.reader(outputFile)


def removeSpecialCharacters(name):
    clean_name = ''
    for char in name:
        if char.isalpha() or char.isspace() or char == '_':
            clean_name += char
    return(clean_name)

# def fillEmptyName():
#     for row in outputReader:
#         try:
#             new_line = row[:]
#             if outputReader.line_num > 3:
#                 new_line = []

#                 new_line.append(
#                     '9__' + removeSpecialCharacters(row[0]).title())
#                 new_line.append(
#                     '9__' + removeSpecialCharacters(row[0]).title())
#                 new_line += row[2:]
#             outputReader.writerow(new_line)

#         except Exception as e:
#             raise e


def prefix(prefix_string='9_'):
    for row in contactsReader:
        try:
            new_line = row[:]
            if contactsReader.line_num > 3:
                new_line = []
                new_line.append(
                    '9__' + removeSpecialCharacters(row[0]).title())
                new_line.append(
                    '9__' + removeSpecialCharacters(row[0]).title())
                new_line += row[2:]
            outputWriter.writerow(new_line)

        except Exception as e:
            raise e

    print(f'Done: Prefixed with {prefix_string}')


prefix()


def filterNumbers(*countryCodes):
    pass
