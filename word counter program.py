text=input("enter the text:")
words=0
for i in text:
    if i==" " or i=="\t" or i=="\n":
        words+=1
if len(text)>0:
    print("number of words:",words+1)
else:
    print("number of words:0")

