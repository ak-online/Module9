# def all_variants(text):
#     for i in range(len(text)):
#         yield text[i]

# def all_variants(text):
#     for i in text:
#         yield i

def all_variants(text):
    for i in range(len(text)):
        #print('i-',i, 'range1 ', range(len(text)))
        for l in range(len(text)-i):
            #print('l-', l, 'range 2', range(len(text)+i))
             yield text[l:l+i+1]

a = all_variants("abc")
for i in a:
    print(i)



