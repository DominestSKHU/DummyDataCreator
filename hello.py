import random
import csv

# 랜덤한 LINKKEY 생성
random_linkkeys = [random.randint(1000000000, 9999999999) for _ in range(300)]

# 학과 목록
departments = ["IT융합 자율학부", "인뭉융합 자율학부", "사회융합 자율학부", "미디어컨텐츠융합 자율학부", "[유한][UH] 의료뷰티학과", "[유한][UH] 컴퓨터소프트웨어공학과", "[유한][UH] 패션디자인학과"]

# 랜덤한 학과 선택
random_departments = [random.choice(departments) for _ in range(300)]

# CSV 파일 생성
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["LINKKEY", "대학학과"])
    for i in range(300):
        writer.writerow([ random_linkkeys[i], random_departments[i]])