import requests
from pprint import pprint

# 2. 특정 조건에 맞는 영화 출력
def vote_average_movies():
    # 0. 평점 8 이상인 영화 목록을 담는 리스트 초기화
    vote_average_movies_over_8 = []

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'ea7605a7a7e59759ce6acfc9527a9e1a',
        'language': 'ko-KR'
}
 
    response = requests.get(BASE_URL+path, params=params).json()
    # 3. response의 'results'항목을 `movie_details`에 할당)
    movie_details = response.get('results',None)

    # 5. movie_details 반복
    for movie_detail in movie_details:
        # 6. 개별 영화들의 평점 확인
        vote_average = movie_detail.get('vote_average', None)
        # 7. 8점 이상인 경우 vote_average_movies_over_8에 해당 영화 정보를 담는다.
        if vote_average >= 8:
            vote_average_movies_over_8.append(movie_detail)

    # 8. 평점 8 이상인 영화들의 목록을 담은 리스트를 반환한다.
    return vote_average_movies_over_8



if __name__ == '__main__':
    pprint(vote_average_movies())    