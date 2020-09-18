from pathlib import Path
import json
import csv
import pandas as pd
trigger_words = ['personal protective equipment', 'PPE', 'hazmat', 'protective equipment', 'protection', 'gear',

                 'mask', 'masks', 'facemask','face mask','face covering', 'N95', 'respirator', 'surgical face mask',

                 'goggles', 'face shield', 'shield', 'helmet', 'hood', 'safety glasses', 'bandana', 'bandanas',

                 'gown', 'coverall', 'don', 'doff', 'lifejacket', 'protective clothing',

                 'gloves', 'hand sanitizer', 'disinfecting wipe', 'scarf', 'scrubs']

numtweet = 0
badfile = 0
dfkeep =pd.read_csv("/gpfs/group/engr/covid19/Cleaned_Place_Object_US_Data/01_2020_ALL/coronavirus-tweet-id-2020-01-21-22.csv")
for dirs in Path(r'/gpfs/group/engr/covid19/Combined_Cleaned_US_Data').iterdir():
    print(dirs.name)

    dirsname = dirs.name +"/"
    dirsnames = "/" + dirsname
    for path in Path(dirs).iterdir():
        print(path)
        if path.name.endswith('.csv'):
            var2 = 0
            try:
                df = pd.read_csv(path)
                length_df = len(df)
                print(length_df)
                drop_count = []
                for i in range(length_df):

                    text = str(df['Text'].values[i])

                    if text in trigger_words:

                        hold = 0
                    else:
                        drop_count.append(i)
                        # print(i)

                length_drop = len(drop_count)
                #print(length_drop)
                var = 0
                try:
                    for i in range(length_drop):

                        df = df.drop(drop_count[i],axis = 0)

                except:
                    print("skip")
                    var = 1
                    badfile = badfile + 1
            except:
                print('skip')
                var2 = 1
                badfile = badfile + 1
        if var != 1 and var2 != 1:
            frame = [dfkeep, df]
            dfkeep = pd.concat(frame)
            numtweet += len(df)
filename = path.name[:-4] +"_keyword_ppe"+ ".csv"
homedir = r"/gpfs/group/engr/covid19/Keyword_Data/Common_Cold"
home = homedir + '/combined/'+ filename

dfkeep.to_csv(home)

print("Number of Bad Files:")
print(badfile)

print("Number of Tweets: ")
print(numtweet)
