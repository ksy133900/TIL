import json
from pprint import pprint


def movie_info(movies, genres):
    pass 

    movie_result = []

    for a in movies:
        for num in a.get('genre_ids'):
            for i in genres:
                if num == i.get('id'):
                    genre_names = []
                    genre_names.append(i.get('name'))

            result = {
            'genre_names' : genre_names,
            'id' : a.get('id'),
            'overview' : a.get('overview'),
            'title' : a.get('title'),
            'vote_average' : a.get('vote_average')

            }
            movie_result.append(result)
            
    return movie_result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))