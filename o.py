
text = input()
text_seperated = text.split(" ")
import re
#print(text_seperated)
upper = re.findall('([A-Z][a-z]+)', text)
aval = (re.findall('([.][ ][A-Z][a-z]+)', text))
aval2 = []
for word in aval:
    aval2.append(word.replace(". ", ""))
#print(upper)
#print(aval2)
for i in range(1,len(text_seperated)):
    if text_seperated[i].replace("." , "") in upper and text_seperated[i] not in aval2:
            print(i+1,":",text_seperated[i].replace("." , "").replace(",", "") , sep="")
    else:
        print("None")
        break
