import streamlit as st
import pickle
import pandas as pd
import requests


def  fetch_poster(movie_id):
   response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4c7ea28adfc5c5f10d8fe8ddb4f0761a&language=en-US'.format(movie_id))
   data= response.json()
   poster_path= data['poster_path']
   full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
   return full_path




movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recomended_movies=[]
    recomended_movies_posters=[]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recomended_movies.append((movies.iloc[i[0]].title))
        recomended_movies_posters.append(fetch_poster(movie_id))


    return recomended_movies, recomended_movies_posters



st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'Select Movie',
movies['title'].values)


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


    
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])