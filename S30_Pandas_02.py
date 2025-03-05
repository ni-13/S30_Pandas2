# Pandas_02

# 1148. Article Views I_Solution_Q1

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df= views[views['author_id']==views['viewer_id']]
    df.drop_duplicates(subset = ['author_id'], inplace= True)
    df.sort_values(by = ['author_id'], inplace= True)
    return df[['author_id']].rename(columns = {'author_id':'id'})

#Alternative1

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df= views[views['author_id']==views['viewer_id']]
    df= df['author_id'].unique()
    df= pd.DataFrame(df, columns= ['id'])
    return df.sort_values(by= ['id'])

______________________________________________________________________________________________________________________________________

# 1683. Invalid Tweets_Solution_Q2

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
   isValid = tweets['content'].str.len()> 15
   df= tweets[isValid]
   return df[['tweet_id']]

#Alternative1

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
   df= tweets[tweets['content'].str.len() >15]
   return df[['tweet_id']]

_________________________________________________________________________________________________________________________________________