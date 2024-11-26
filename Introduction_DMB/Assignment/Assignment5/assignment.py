from pymongo import MongoClient
import json

# MongoDB 클라이언트 연결
client = MongoClient("mongodb://localhost:27017/")

# 데이터베이스 목록 가져오기
databases = client.list_database_names()

# 데이터베이스 목록 출력
print(databases)

# 데이터베이스 및 컬렉션 선택
db = client["myDatabase"]         # 원하는 데이터베이스 이름으로 변경
collection = db["restaurants"]     # 원하는 컬렉션 이름으로 변경

# JSON 파일 열기 및 읽기
with open("/Users/hunjunsin/Desktop/box/Introduction_DMB/Assignment/Assignment5/restaurants.json") as file:
    for line in file:
        data = json.loads(line)
        collection.insert_one(data)
# 데이터 삽입
if isinstance(data, list):  # 데이터가 배열 형식인지 확인
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("JSON data inserted successfully.")