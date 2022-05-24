import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('/home/quangmt/Documents/Recommendation_system/archive/tmdb_5000_movies.csv')
credits = pd.read_csv('/home/quangmt/Documents/Recommendation_system/archive/tmdb_5000_credits.csv')

movies = movies.merge(credits, on= 'title')
# print(movies.info())
movies_in = movies[['id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies_in.dropna(inplace=True)


def convert_genres(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies_in['genres'] = movies_in['genres'].apply(convert_genres)
movies_in['keywords'] = movies_in['keywords'].apply(convert_genres)

def convert_cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter <3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

movies_in['cast'] = movies_in['cast'].apply(convert_cast)
movies_in['cast'] = movies_in['cast'].apply(lambda x:x[0:3])

def convert_crew(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies_in['crew'] = movies_in['crew'].apply(convert_crew)
movies_in['overview'] = movies_in['overview'].apply(lambda x:x.split())
movies_in['genres'] = movies_in['genres'].apply(collapse)
movies_in['keywords'] = movies_in['keywords'].apply(collapse)
movies_in['cast'] = movies_in['cast'].apply(collapse)
movies_in['crew'] = movies_in['crew'].apply(collapse)

movies_in['tags'] = movies_in['overview'] + movies_in['genres'] + movies_in['keywords'] + movies_in['crew']

new_data = movies_in.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])

new_data['tags'] = new_data['tags'].apply(lambda x:" ".join(x))
new_data['tags'] = new_data['tags'].apply(lambda x:x.lower())

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_data['tags']).toarray()

simi = cosine_similarity(vectors)

def recommended(movie):
    movie_index = new_data[new_data['title'] == movie].index[0]
    movie_dis = simi[movie_index]
    movie_list = sorted(list(enumerate(movie_dis)), reverse=True, key=lambda x:x[1])[1:10]

    for i in movie_list:
        print(new_data.iloc[i[0]].title)


data = {
        'id': [9999999,9999998],
        'title': ['Fifty', 'Sixty'],
        'tags': ['abc', 'xyz']
    }
df_add = pd.DataFrame(data)
print(new_data.append(df_add, ignore_index=True))


