from serpapi import GoogleSearch

print("Enter your question: ")
q = input()

search = GoogleSearch({
    "q": "meraki" + q,
    "api_key": #############################################
  })

#store the result as a disctionary
results = search.get_dict()

abox = results["answer_box"]

#print snippet of the answer box
print('\033[1m' + abox["snippet"] + '\033[0m')

#print list of the answer box if it exists
if "list" in abox:
    for num, line in enumerate(abox["list"],1):
        print(str(num) + ".", line)

#print link to the article
print("\nFor more information please visit the following article:\n" + abox["link"])
