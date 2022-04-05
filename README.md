# naxap

1. Download this and extract zip
2. Give complete path of `my_text_file.txt`
 ``` 
path = "path_to_file/my_text_file.txt"
search_string = "https://bytescare.com"
```
3. `python3  12.py`

<b>Problem Statement 12</b>
Given a text file, find if any URL is present in the text file or not, if present extract first occurrence

Example: Given input my_text_file.txt contains the text "Visit my site https://bytescare.com" then the output must be "Occurrence Found: 1 First 

Occurrence: https://bytescare.com"

Input: Location of the text file

Output: Number of URL occurrences and First Occurrence

Partial Acceptable Solution: If can only output Occurrence found

Complete solution: If output occurrence found and the First Occurrence


<b>Run this</b>
```
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

path = "path_to_file/my_text_file.txt"
search_string = "https://bytescare.com"
result_statement1, result_statement2 = operation(path, search_string)
print(result_statement2)
print(result_statement1)
```
## Output.
```
Number of occurrnce are 5
first occurence in line 386 at word 2

```
##


<b>Problem Statement 5</b>

Given a single domain and a list of random domain names, find which are the closest match in the list,

Example: Given input domain:google.com and domain list: [thegoogle.com, good.go, google.co.in, bing.com] will closely matches with thegoogle.com, good.go, google.co.in but not bing.com. Example google .com matches 100% with google.com

Input: domain and list of the domain with which you will match the  domain

Output: Floating Point/Decimal or Percentage value of Single Domain Matches with the other domains within the domain list.

Partial Acceptable Solution: None (If its a match or not is not acceptable)

Complete solution: Giving output in floating-point/decimals as a prediction from  0-1 or 0%-100% with each domain in the domain list.

## Run this
Step 1 : `python3  5.py`
```
from difflib import SequenceMatcher

def matcher(domain_list, search_domain):
    for domain in domain_list:
        ratio = SequenceMatcher(None, domain, search_domain).ratio()
        print(str(domain) + ' = ' + str(ratio))



lst = ['thegoogle.com', 'good.go', 'google.co.in', 'bing.com']
domain = 'google.com'
matcher(lst, domain)
```
<b>Output</b>
```
thegoogle.com = 0.8695652173913043
good.go = 0.5882352941176471
google.co.in = 0.8181818181818182
bing.com = 0.5555555555555556
```

Feel Free to email me one of given in my resume


Thanks & Regard

Team Naxap

Team Bytes Care
