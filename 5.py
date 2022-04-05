# Problem Statement 5
# Given a single domain and a list of random domain names, find which are the closest match in the list,
# Example: Given input domain:google.com and domain list: [thegoogle.com, good.go, google.co.in, bing.com] will closely matches with thegoogle.com, good.go, google.co.in but not bing.com. Example google .com matches 100% with google.com
#
# Input: domain and list of the domain with which you will match the  domain
# Output: Floating Point/Decimal or Percentage value of Single Domain Matches with the other domains within the domain list.
# Partial Acceptable Solution: None (If its a match or not is not acceptable)
# Complete solution: Giving output in floating-point/decimals as a prediction from  0-1 or 0%-100% with each domain in the domain list.
from difflib import SequenceMatcher

def matcher(domain_list, search_domain):
    for domain in domain_list:
        ratio = SequenceMatcher(None, domain, search_domain).ratio()
        print(str(domain) + ' = ' + str(ratio))



lst = ['thegoogle.com', 'good.go', 'google.co.in', 'bing.com']
domain = 'google.com'
matcher(lst, domain)
