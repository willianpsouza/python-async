from fastapi import FastAPI
from fastapi.responses import JSONResponse


import requests
import concurrent.futures
import json

app = FastAPI()

# One connection to all sessions ! 
s = requests.Session()

def DefaultRespose(content):
    headers = {"Content-Type": "application/json"}
    return JSONResponse(content=content, headers=headers)


def data():
        return {
            "_id": "63cac1995b68566eb1e85fd3",
            "index": 0,
            "guid": "dd182962-cbde-4749-aa34-ab2c9a9383e6",
            "isActive": True,
            "balance": "$1,988.02",
            "picture": "http://placehold.it/32x32",
            "age": 39,
            "eyeColor": "brown",
            "name": "Clay Douglas",
            "gender": "male",
            "company": "ELECTONIC",
            "email": "claydouglas@electonic.com",
            "phone": "+1 (982) 592-3547",
            "address": "577 Stuyvesant Avenue, Bellfountain, Louisiana, 3381",
            "about": "Irure culpa esse eiusmod sint qui dolor qui aliquip nisi mollit velit dolor non dolore. Pariatur ullamco est esse aliqua tempor labore dolore excepteur esse pariatur aliqua commodo. Velit velit elit ut nulla ex sit exercitation aliquip consequat dolore ea. Incididunt amet et non nulla.\r\n",
            "registered": "2017-02-19T11:45:15 +06:00",
            "latitude": 75.369903,
            "longitude": 156.108572,
            "tags": [
                "adipisicing",
                "reprehenderit",
                "veniam",
                "pariatur",
                "cupidatat",
                "ipsum",
                "ad"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Moran Livingston"
                },
                {
                    "id": 1,
                    "name": "Blake Stafford"
                },
                {
                    "id": 2,
                    "name": "Shepherd Middleton"
                }
            ],
            "greeting": "Hello, Clay Douglas! You have 6 unread messages.",
            "favoriteFruit": "banana"
        },
        {
            "_id": "63cac1999ae834a9e0c6689e",
            "index": 1,
            "guid": "25ca65b9-9a99-461b-aaf6-545059be51ab",
            "isActive": True,
            "balance": "$3,067.58",
            "picture": "http://placehold.it/32x32",
            "age": 22,
            "eyeColor": "blue",
            "name": "Hoover Matthews",
            "gender": "male",
            "company": "SPACEWAX",
            "email": "hoovermatthews@spacewax.com",
            "phone": "+1 (846) 583-3844",
            "address": "647 Sutton Street, Devon, Maryland, 5764",
            "about": "Aute in officia adipisicing non mollit aliqua commodo Lorem et occaecat consequat. Do commodo nulla minim est ut. Dolore et reprehenderit consectetur aliqua esse.\r\n",
            "registered": "2017-09-19T01:22:13 +05:00",
            "latitude": 83.911038,
            "longitude": 50.478669,
            "tags": [
                "cillum",
                "magna",
                "labore",
                "aute",
                "voluptate",
                "labore",
                "nostrud"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Maldonado Welch"
                },
                {
                    "id": 1,
                    "name": "Amber Fitzpatrick"
                },
                {
                    "id": 2,
                    "name": "Ramona Dunlap"
                }
            ],
            "greeting": "Hello, Hoover Matthews! You have 8 unread messages.",
            "favoriteFruit": "apple"
        },
        {
            "_id": "63cac199496d18db6a027044",
            "index": 2,
            "guid": "b528fafa-5671-4215-9786-57c9183839c7",
            "isActive": False,
            "balance": "$2,413.45",
            "picture": "http://placehold.it/32x32",
            "age": 20,
            "eyeColor": "blue",
            "name": "Garza Cardenas",
            "gender": "male",
            "company": "KOOGLE",
            "email": "garzacardenas@koogle.com",
            "phone": "+1 (826) 459-2699",
            "address": "341 Aviation Road, Columbus, Vermont, 2438",
            "about": "Id ut qui tempor culpa id consectetur et minim labore amet ad aliquip ea. Do ut veniam laboris id. Ullamco excepteur ipsum non deserunt aliquip minim anim proident laborum sint irure.\r\n",
            "registered": "2018-08-29T03:30:58 +05:00",
            "latitude": -30.270761,
            "longitude": 158.940332,
            "tags": [
                "non",
                "minim",
                "exercitation",
                "ea",
                "fugiat",
                "nostrud",
                "aliquip"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Ana Clemons"
                },
                {
                    "id": 1,
                    "name": "Patterson Hancock"
                },
                {
                    "id": 2,
                    "name": "Barber Best"
                }
            ],
            "greeting": "Hello, Garza Cardenas! You have 9 unread messages.",
            "favoriteFruit": "apple"
        },
        {
            "_id": "63cac199c812db9b2942827e",
            "index": 3,
            "guid": "abec31ee-5374-45b2-8925-1f910d28c32e",
            "isActive": True,
            "balance": "$1,795.75",
            "picture": "http://placehold.it/32x32",
            "age": 31,
            "eyeColor": "brown",
            "name": "Sharlene Zimmerman",
            "gender": "female",
            "company": "UNISURE",
            "email": "sharlenezimmerman@unisure.com",
            "phone": "+1 (885) 452-3885",
            "address": "566 Vandervoort Place, Glasgow, Alabama, 2894",
            "about": "Ipsum reprehenderit dolore voluptate excepteur anim eiusmod tempor enim magna quis nisi elit. Nulla ea velit elit irure sint commodo. Commodo anim nostrud enim exercitation qui aute culpa in duis laborum ipsum voluptate.\r\n",
            "registered": "2022-12-27T09:04:10 +06:00",
            "latitude": 83.214118,
            "longitude": -43.681967,
            "tags": [
                "sunt",
                "mollit",
                "occaecat",
                "sunt",
                "eu",
                "est",
                "velit"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Humphrey Burton"
                },
                {
                    "id": 1,
                    "name": "Wall Callahan"
                },
                {
                    "id": 2,
                    "name": "Madeleine Pitts"
                }
            ],
            "greeting": "Hello, Sharlene Zimmerman! You have 6 unread messages.",
            "favoriteFruit": "apple"
        },
        {
            "_id": "63cac1996cea337a3507ca9b",
            "index": 4,
            "guid": "b5de330b-2a18-4577-8b7a-12069c580fbc",
            "isActive": False,
            "balance": "$3,584.50",
            "picture": "http://placehold.it/32x32",
            "age": 31,
            "eyeColor": "blue",
            "name": "Karen Mcdowell",
            "gender": "female",
            "company": "OZEAN",
            "email": "karenmcdowell@ozean.com",
            "phone": "+1 (865) 525-2374",
            "address": "326 Tompkins Avenue, Chilton, Missouri, 6173",
            "about": "Est dolor aliquip reprehenderit ullamco ipsum est et veniam incididunt. Cillum esse occaecat anim reprehenderit nostrud esse ex eu aliqua ullamco sit sint eu aliqua. Labore ex commodo ea est minim ad ullamco tempor reprehenderit occaecat reprehenderit nulla magna.\r\n",
            "registered": "2020-03-25T11:28:15 +05:00",
            "latitude": 31.351391,
            "longitude": 26.736712,
            "tags": [
                "qui",
                "labore",
                "nostrud",
                "et",
                "aliquip",
                "esse",
                "quis"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Stein Cote"
                },
                {
                    "id": 1,
                    "name": "Roberson Fuentes"
                },
                {
                    "id": 2,
                    "name": "Erma Drake"
                }
            ],
            "greeting": "Hello, Karen Mcdowell! You have 5 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "63cac199c879cdd1537f7282",
            "index": 5,
            "guid": "a1a52678-f368-402f-9739-cd76a31fad44",
            "isActive": True,
            "balance": "$1,243.48",
            "picture": "http://placehold.it/32x32",
            "age": 40,
            "eyeColor": "blue",
            "name": "Christian Nichols",
            "gender": "female",
            "company": "ZIDOX",
            "email": "christiannichols@zidox.com",
            "phone": "+1 (945) 456-2848",
            "address": "233 Elizabeth Place, Conestoga, Arizona, 6837",
            "about": "Nostrud do commodo duis tempor labore cupidatat ad. Irure proident esse aute nisi est minim nisi pariatur minim incididunt. Ea ullamco nisi aliquip anim mollit ut aliquip quis et nulla laboris non. Velit exercitation eiusmod incididunt laboris non.\r\n",
            "registered": "2019-05-15T04:37:26 +05:00",
            "latitude": 49.846664,
            "longitude": 128.728976,
            "tags": [
                "culpa",
                "magna",
                "occaecat",
                "magna",
                "amet",
                "eiusmod",
                "ipsum"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Rebekah Whitney"
                },
                {
                    "id": 1,
                    "name": "West Langley"
                },
                {
                    "id": 2,
                    "name": "Carlson Conley"
                }
            ],
            "greeting": "Hello, Christian Nichols! You have 1 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "63cac1994a27141075129434",
            "index": 6,
            "guid": "ecf000dd-3fa9-4c8b-ab66-42045b36749b",
            "isActive": False,
            "balance": "$3,271.68",
            "picture": "http://placehold.it/32x32",
            "age": 20,
            "eyeColor": "brown",
            "name": "Dyer Moon",
            "gender": "male",
            "company": "XSPORTS",
            "email": "dyermoon@xsports.com",
            "phone": "+1 (893) 441-2361",
            "address": "776 Hazel Court, Williamson, Colorado, 6186",
            "about": "Sunt incididunt pariatur amet consequat labore. Eiusmod excepteur labore cillum anim sunt proident et laboris ea veniam cillum amet adipisicing excepteur. Eiusmod velit labore nostrud proident officia nulla exercitation eu excepteur ad. Nostrud sit commodo deserunt velit adipisicing mollit amet.\r\n",
            "registered": "2022-07-14T06:59:11 +05:00",
            "latitude": -63.735901,
            "longitude": -81.686588,
            "tags": [
                "ipsum",
                "adipisicing",
                "sit",
                "ipsum",
                "mollit",
                "commodo",
                "consequat"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Blanchard Leon"
                },
                {
                    "id": 1,
                    "name": "Jan Schroeder"
                },
                {
                    "id": 2,
                    "name": "Brooke Harrington"
                }
            ],
            "greeting": "Hello, Dyer Moon! You have 9 unread messages.",
            "favoriteFruit": "strawberry"
        }


def get_page_content(w_page_url, timeout=10):
    response = s.get(url=w_page_url, timeout=timeout)
    if response.status_code == 200:
        print(response.text.replace("\n",""))
        
        return response.text.replace("\n","")

    return {}


@app.get("/")
async  def read_results():
    return DefaultRespose(data())


@app.get("/with_thread")
def read_results():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        futures.append(executor.submit(data, ))
        for future in concurrent.futures.as_completed(futures):
            return DefaultRespose(future.result())


@app.get("/remote")
async def read_remote():
    pages = ["http://172.17.0.2/static_teste/"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in pages:
            futures.append(executor.submit(get_page_content, w_page_url=url))
        for future in concurrent.futures.as_completed(futures):
            return DefaultRespose(future.result())
