import json
import csv
import pandas as pd
from bs4 import BeautifulSoup as soup
from textblob import TextBlob as tb
from textblob import Word
from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import Nominatim

key = '9bab2ce2c68947ddba5167644aaa0272'
geocoder = OpenCageGeocode(key)
geolocator = Nominatim(user_agent="Texas State University")

geo = []
sensitive = []
coordinates = []
created_at = []
id = []
source = []
replystatus = []
replyuser = []
replyname = []
citynameAPIfull = []
citynameAPI = []
countryAPI = []
hashcount = []
hashtext = []
userid = []
name = []
screenname = []
samename = []
hashtagspelling = []
userurl = []
urlbinary = []
descrtext = []
descrlen = []
descrpol = []
descrsub = []
descrspell = []
ver = []
follower = []
friends = []
listed = []
favorites = []
status = []
accountcreate = []
translated = []
qouted = []
retweet = []
favoritecount = []
mentionscount = []
urlcount = []
witheld = []
withheldscope = []
text = []
textpol = []
textsub = []
textlen = []
textspell = []
lat = []
lng = []
location = []
q = 0
z = 0

fileInput = r"C:\Users\mxr29\OneDrive\Desktop\Twitter Geo\coronavirus-tweet-id-2020-03-21-15-dos.jsonl"

with open(fileInput, 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    #print(q)
    if q < 1000000000000:
        print(q)
        q=q+1
        result = json.loads(json_str)

        if result['lang'] == 'en' and result["truncated"] == False:
            locstring = result['user']['location']

            if result["place"] == None :
                poop = 0
            else:
                if result["place"]["country_code"] == "US":
                    print(result['place']['url'])
                    print(result["place"]["country_code"])
                    z= z+1
                    location.append(locstring)
                    text.append(result['full_text'])
                    textblob = tb(result['full_text'])
                    textpol.append(textblob.sentiment.polarity)
                    textsub.append(textblob.sentiment.subjectivity)
                    tbwords = textblob.words
                    tblen = len(tbwords)
                    textlen.append(tblen)

                    # spellingc = 0
                    # for p in range (tblen):
                    #     spellingc = spellingc + (words[p].spellcheck()[0][1])
                    #
                    # if spellingc != 0:
                    #     score = spellingc/wordlen
                    #     textspell.append(score)
                    # else:
                    #     textspell.append(-1)

                    retweet.append(result['retweet_count'])
                    favoritecount.append(result["favorite_count"])

                    mentionscount.append(len(result['entities']["user_mentions"]))
                    urlcount.append(len(result['entities']["urls"]))
                    if 'withheld_in_countries' in result:
                        witheld.append(result['withheld_in_countries'])
                    else:
                        witheld.append(0)
                    if "withheld_scope" in result:
                        withheldscope.append(result["withheld_scope"])
                    else:
                        withheldscope.append(0)

                    "withheld_scope"

                    if result["is_quote_status"] == True:
                        qouted.append(1)
                    else:
                        qouted.append(0)


                    created_at.append(result['created_at'])
                    id.append(result['id'])
                    userid.append(result['user']['id'])
                    name.append(result['user']['name'])
                    screenname.append(result['user']['screen_name'])
                    if result['user']["verified"] == True:
                        ver.append(1)
                    else:
                        ver.append(0)

                    follower.append(result['user']["followers_count"])
                    friends.append(result['user']["friends_count"])
                    listed.append(result['user']["listed_count"])
                    favorites.append(result['user']["favourites_count"])
                    status.append(result['user']["statuses_count"])
                    accountcreate.append(result['user'][ "created_at"])


                    if result['user']["is_translator"] == True:
                        translated.append(1)
                    else:
                        translated.append(0)

                    descrtext.append(result['user']['description'])

                    desctextblob = tb(result['user']['description'])
                    descrpol.append(desctextblob.sentiment.polarity)
                    descrsub.append(desctextblob.sentiment.subjectivity)
                    words = desctextblob.words
                    wordlen = len(words)
                    descrlen.append(wordlen)

                    # spellingc = 0
                    # for s in range (wordlen):
                    #     spellingc = spellingc + (words[s].spellcheck()[0][1])
                    #
                    # if spellingc != 0:
                    #     score = spellingc/wordlen
                    #     descrspell.append(score)
                    # else:
                    #     descrspell.append(-1)






                    if result['user']['url'] == None:

                        urlbinary.append(0)
                        userurl.append(0)
                    else:
                        userurl.append(result['user']['url'])
                        urlbinary.append(1)

                    namehold = (result['user']['name'])
                    screennamehold =(result['user']['screen_name'])
                    if namehold.strip() == screennamehold.strip():
                        samename.append(1)
                    else:
                        samename.append(0)



                    hashtaglen = len(result['entities']['hashtags'])
                    hashcount.append(hashtaglen)
                    test = result['entities']['hashtags']
                    hold = []

                    if test != []:
                        for i in range(hashtaglen):
                            hold.append(test[i]['text'])


                    hashtags = str(hold).strip('[]')

                    if hashtags != '':
                        hashtext.append(hashtags)

                    else:
                        hashtext.append(0)



                    if result['place'] == None:
                        citynameAPI.append(0)
                        countryAPI.append(0)
                        citynameAPIfull.append(0)
                    else:
                        citynameAPI.append(result['place']['name'])
                        citynameAPIfull.append(result['place']['full_name'])
                        countryAPI.append(result['place']['country'])



                    if result['in_reply_to_status_id'] == None:
                        replystatus.append(0)

                    else:
                        replystatus.append(result['in_reply_to_status_id'])



                    if result['in_reply_to_user_id'] == None:
                        replyuser.append(0)

                    else:
                        replyuser.append(result['in_reply_to_user_id'])



                    if result['in_reply_to_screen_name'] == None:
                        replyname.append(0)

                    else:
                        replyname.append(result['in_reply_to_screen_name'])




                    sourceobj = soup(result['source'],'html.parser')
                    sourcetext = sourceobj.get_text()
                    if "Twitter" in sourcetext:
                        source.append(0)
                    else:
                        source.append(1)




                    if result['coordinates'] == None:
                        coordinates.append(0)


                    else:
                        coordinates.append(result['coordinates']['coordinates'])




                    if 'possibly_sensitive' in result:
                        var = result['possibly_sensitive']

                        if var == True:
                            sensitive.append(1)
                        else:
                            sensitive.append(-1)

                    else:
                        sensitive.append(0)



                    # if 'retweeted_status' in result:
                    #     print(result['retweeted_status'])



                    # if result['is_quote_status']== True and 'quoted_status_id' in result:
                    #     print("{}".format(result))
                    #     print(result['quoted_status_id'])




                    geohold = result['geo']
                    if geohold == None :
                        geo.append(0)
                    else:
                        geo.append(geohold['coordinates'])
                    q=q+1


print(z)
df = pd.DataFrame({'ID':id,
                           "Location": location,
                           'Coordinates':coordinates,
                           'GEO': geo,
                           'City Name API': citynameAPI,
                           'City Name Full':citynameAPIfull,
                           'Country API' : countryAPI,
                           "Date/Time": created_at,
                           'Sensitive': sensitive,
                           "Source": source,
                           "Reply Status": replystatus,
                           "Reply User" : replyuser,
                           "Reply Name" : replyname,
                           "Hashtag Text": hashtext,
                           "Hashtag count": hashcount,
                            'User Id': userid,
                           'Name': name,
                           'Screen Name': screenname,
                           'Screen/Name Same': samename,
                           'User Url':userurl,
                           'User Url Bin': urlbinary,
                           'Description': descrtext,
                           'Desc Subjectivity': descrsub,
                           'Desc Polarity': descrpol,
                           'Desc Word Count': descrlen,
                           'Verified': ver,
                           'Followers': follower,
                           'Friends': friends,
                           'Listed' : listed,
                           'Favorites': favorites,
                           'Status' : status,
                           'Account Create': accountcreate,
                           'Translated': translated,
                           'Qouted': qouted,
                           'Retweeted': retweet,
                           'Favorite Count': favoritecount,
                           'Mentions Count': mentionscount,
                           'Url Count' : urlcount,
                           'Withheld' : witheld,
                           'Withheld Scope' : withheldscope,
                           'Text Subjectivity' : textsub,
                           'Text Polarity' : textpol,
                           'Text Length' : textlen,
                           'Text' : text
                           })
df.to_csv(r"C:\Users\mxr29\OneDrive\Desktop\Twitter Geo\Excel\jsonconvertboiiiii.csv")




