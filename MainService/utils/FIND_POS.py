
import pandas as pd
import re
import json
patternPO = r'(?<=PO\: )(.*?)(?=\n)'
pattern = r'(?<=Positions\: \[)(.*?)(?=\])'

path = r'C:\Users\Ale\Downloads\GPT-3-Hackaton-Dataset-handout.xlsx'
df = pd.read_excel(path)
string = df.iloc[0].loc["combined_email"]



def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def conv(to_be_conv): #I pass a list containing strings
    conv = ""
    for x in to_be_conv: #each x is a string
        conv = x + '-'
    if len(to_be_conv)==0:
        conv =r'alle'
    else:
        conv = conv[:-1]
    return conv



def get_pos(string_email):

    try:

        pre_json = []      #ora è per ogni riga, i.e. mail
        keys = []

        temp = string_email  #has to process this one
        all = re.findall('[0-9]+', temp)  #all the numbers
        ass_po = 0


        for i in range(len(all)):
            pos = all[i]

            if len(pos) == 1 :   #potrebbero essere a due cifre
                if ass_po==0:
                    continue
                pre_json.append((all[ass_po],pos))    #here couple key-pos es; [(10921,1),(10921,2)]

            elif len(pos)==10: #POS SONO ALMENO 10, MA COSI SONO SICURO
                ass_po = i
                keys.append(pos)  #here only keys

        #ora devo fare dictionary locale

        dict = {}
        for key in keys:
            list = []
            for x in pre_json:
                if x[0] == key:
                    list.append(x[1])
            dict[key] = list


        return (dict,keys)


    finally:
        pass

print(get_pos(string))
print("fuck the police")