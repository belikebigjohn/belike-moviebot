import requests as rq
from bs4 import BeautifulSoup


def get_movie_url(title):
    title = title.replace(" ","+")
    url = f"https://www.imdb.com/find?q={title}&s=tt&exact=true&ref_=fn_tt_ex"
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = rq.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # проверяем, зашли ли мы на сайт
    if response.status_code == 200:
        print("получаем ссылку")
    else:
        print('error')


    # ищем названия фильмов по запросы
    try:
        elements = soup.find_all('h3', attrs={"class": "ipc-title__text"})
        #print(elements)
        if elements:
            movie_titles = []
            for element in elements:
                # вычленяем названия из того говна которое мы получили
                title_text = element.get_text(strip=True)
                # исключаем "Titles", "More results", "Advanced search", "Recently viewed"
                if title_text not in ["Titles","title", "More results", "Advanced search", "Recently viewed"]:
                    movie_titles.append(title_text)
            #print(movie_titles)
        else:
            print('error')
    except Exception as e:
        print("Titles Error:",e)
#   ipc-lockup-overlay ipc-focusable ipc-focusable--constrained        класс первой ссылки!!!
    # начинаем искать ссылку на первый результат поиска
    try:
        first_url_element = soup.find('a', attrs={"class": "ipc-lockup-overlay ipc-focusable ipc-focusable--constrained"})
        imdb_url = "https://www.imdb.com/"
        #print(first_url_element)
        # убираем лишнее
        if first_url_element and first_url_element.get('href'):
            href_value = first_url_element['href']
            # по сколько ссылка в хрефе состоит лишь из половинки ссылки,
            # то собираем ссылку из заготовки (imdb_url) и готовой части хрефа (href_value)
            #print(imdb_url + href_value)
            return imdb_url + href_value
        else:
            return 'Cсылка не найдена'
    except Exception as e:
        return "get_movie_url/url_element ERROR:",e


#get_movie_url("заводной апельсин")


def get_movie_info(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = rq.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # проверяем, зашли ли мы на сайт
    if response.status_code == 200:
        print("получаем информацию")
    else:
        print('error')

    try:
        movie_title = soup.find('span', attrs={"data-testid": "hero__primary-text"})
        title = movie_title.text if movie_title else "Нет названия/Ничего не найдено"
        #print(title)

        movie_description = soup.find('span', attrs={"class":"sc-bf30a0e-1 gWyXyP"})
        description = movie_description.text if movie_description else "Нет описания/Ничего не найдено"
        #print(description)
        return f"{title}\n {description}"
    except Exception as e:
        return "get_movie_info/ ERROR", e


#get_movie_info("https://www.imdb.com/title/tt0361748/?ref_=nv_sr_srsg_1_tt_7_nm_0_in_0_q_%25D0%25B1%25D0%25B5%25D1%2581%25D1%2581%25D0%25BB%25D0%25B0")

def enter_point(title_message):
    ...
    # print("Привет фильм!")
    #
    # url = get_movie_url(title_message)
    # if url != "Cсылка не найдена":
    #     info = get_movie_info(url)
    #     return info
    # elif url == "Cсылка не найдена":
    #     print("Ссылка не найдена. Проверьте правильность введенного названия")
    # else:
    #     print("Error")

if __name__ == "__main__":
    ...
    # title_message = input("Enter movie title:")
    # enter_point(title_message)