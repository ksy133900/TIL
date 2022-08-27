import requests
from pprint import pprint


def credits(title):
    pass 
    result_dict = {'cast':[], 'crew':[]}  # {cast:actors, crew:directors} 형태로 반환할 딕셔너리
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243/credits'
    params = {
        'api_key': '',
        'language': 'ko-KR'    
}
    response = requests.get(BASE_URL+path, params=params).json()
    
    if 'success' in response.keys():
        return None
     #  people_dict['cast']를 반복하며, 배우 상세정보 조회
    for actor in response['cast']:
        # cast_id 값이 10보다 작은 배우의 이름을 result_dict['cast']의 value값으로 추가한다.
        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])
     #  people_dict['crew']를 반복하며, 스텝 상세정보 조회
    for crew in response['crew']:
        # 7-2. department값이 Directing인 감독의 이름을 result_dict['crew']의 value값으로 추가한다.
        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name'])
    return result_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
