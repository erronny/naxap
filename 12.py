# Given a text file, find if any URL is present in the text file or not, if present extract first occurrence
# Example: Given input my_text_file.txt contains the text "Visit my site https://bytescare.com" then the output must be "Occurrence Found: 1 First Occurrence: https://bytescare.com"
# Input: Location of the text file
# Output: Number of URL occurrences and First Occurrence
# Partial Acceptable Solution: If can only output Occurrence found
# Complete solution: If output occurrence found and the First Occurrence
# Problem Statement 12

def operation(location, substring):
    file = open(location, "r", encoding='UTF-8')
    fileObject = file.read()
    # line_separate = [line for line in fileObject.split("\n") if line.strip() != '']
    line_separate = [line for line in fileObject.split("\n")]
    # print(line_separate)
    dict_collection = {}
    for i in range(len(line_separate)):
        dict_collection[i] = list(line_separate[i].split(" "))
    # print(dict_collection)
    occurence = 0
    occurence_index = None
    line = None
    for key, value in dict_collection.items():
        for item in range(len(value)):
            if value[item].lower() == substring.lower():
                occurence += 1
                if occurence == 1:
                    occurence_index = item+1
                    line = key+1
    display_format = {'key1':line, 'key2':occurence_index}
    result_statement1 = "first occurence in line {key1} at word {key2}".format_map(display_format)
    result_statement2 = "Number of occurrnce are " + str(occurence)
    file.close()
    return result_statement1, result_statement2

path = "/home/erronny/Documents/python/Project/my_text_file.txt"
search_string = "https://bytescare.com"
result_statement1, result_statement2 = operation(path, search_string)
print(result_statement2)
print(result_statement1)
# operation(x, y)
