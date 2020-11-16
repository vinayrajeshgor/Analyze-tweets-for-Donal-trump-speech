#import the file
import pandas as pd
import numpy as np

#read the file
df = pd.read_csv('tweets.csv')
print(df)

#create column named as Sender, Time and Tweet
column_names=['Sender', 'Time', 'Tweet']
df = pd.read_csv('tweets.csv', names=column_names)
print(df)

#create Sender column to list
list_sender = df.Sender.to_list()
print(list_sender)

print("\n")

from collections import Counter

#top 5 most active senders are
counts = Counter(list_sender)
print("The 5 most active senders with counts are", counts.most_common(5))

print("\n")

#create tweets column to list
list_tweets = df.Tweet.to_list()
print(list_tweets)

print("\n")

#top 5 most retweeted are
for i in list_tweets:
    if i.startswith('RT'):
        counts = Counter(list_tweets)
print("The 10 most re-tweeted tweets are\n", counts.most_common(10))

#2 for loop for screen_name
screenname=list()
for i in list_tweets:
    for j in i.split():
        if j.startswith('@'):
            screenname.append(j)
            print(screenname)
            
#5 most cited screen-names          
print('\n')
counts =Counter(screenname)
print("The 5 most cited screeen-names are\n", counts.most_common(5))

#2 for loop for hashtags
hashtags=list()
for h in list_tweets:
    for k in h.split():
        if k.startswith('#'):
            hashtags.append(k)
            print(hashtags)
            
#5 most popular hashtags           
print('\n')
counts =Counter(hashtags)
print("The 5 most cited hashtags are\n", counts.most_common(5))

#create tweets column to list
list_time = df.Time.to_list()
print(list_time)

#sorting the data set by timestamp
list_time, list_tweets = zip((*sorted(zip(list_time,list_tweets))))
print(list_tweets)

sorting_by_tweets = list_tweets
print(sorting_by_tweets)

#splitting the tweets into 5 and converting in to strings
list_split = np.array_split(sorting_by_tweets,5)
for array in list_split:
    print(list(array))

#creating subset of strings    
x=list_split[0]
print(x)

#printing 1st strings acting as a words of bags
str0 = ' '.join(map(str, x))
print(str0)

y=list_split[1]
print(y)

#printing 2nd strings acting as a words of bags
str1 = ' '.join(map(str, y))
print(str1)

z=list_split[2]
print(z)

#printing 2nd strings acting as a words of bags
str2 = ' '.join(map(str, z))
print(str2)

a=list_split[3]
print(a)

#printing 4th strings acting as a words of bags
str3 = ' '.join(map(str, a))
print(str3)

b=list_split[4]
print(b)

#printing 5th strings acting as a words of bags
str4 = ' '.join(map(str, b))
print(str4)

#import stopwords from text file
column_names_stopwords = ['stop_words']
sw = pd.read_csv('stopwords.txt', names=column_names_stopwords)
print(sw)

#create Stopwords column to list
list_stop_words = sw.stop_words.to_list()
print(list_stop_words)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

#wordcloud for string0
cloud1=WordCloud(width=800, height=800,background_color='black',colormap='rainbow', stopwords=list_stop_words).generate(str0)
plt.imshow(cloud1)
plt.axis("off")
plt.show()

#wordcloud for string1
cloud2=WordCloud(width=800, height=800,background_color='black',colormap='rainbow', stopwords=list_stop_words).generate(str1)
plt.imshow(cloud2)
plt.axis("off")
plt.show()

#wordcloud for string2
cloud3=WordCloud(width=800, height=800,background_color='black',colormap='rainbow', stopwords=list_stop_words).generate(str2)
plt.imshow(cloud3)
plt.axis("off")
plt.show()

#wordcloud for string3
cloud4=WordCloud(width=800, height=800,background_color='black',colormap='rainbow', stopwords=list_stop_words).generate(str3)
plt.imshow(cloud4)
plt.axis("off")
plt.show()

#wordcloud for string4
cloud5=WordCloud(width=800, height=800,background_color='black',colormap='rainbow', stopwords=list_stop_words).generate(str4)
plt.imshow(cloud5)
plt.axis("off")
plt.show()

