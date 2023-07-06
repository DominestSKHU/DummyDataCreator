<<<<<<< HEAD
import random
import csv
# 성별 목록
genders = ["F", "M"]

# 랜덤한 성별 선택
random_genders = [random.choice(genders) for _ in range(300)]

# 주로 사용되는 한국 성씨
last_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임"]

# 주로 사용되는 한국 이름
first_names = ["현우", "지영", "성우", "예슬", "민수", "지수", "예진", "지훈", "은지", "수민"]

# 랜덤한 이름 생성
random_names = [random.choice(last_names) + random.choice(first_names) for _ in range(300)]

# 랜덤한 학번 생성
random_student_numbers = [random.randint(20180000, 20239999) for _ in range(300)]

# 신청기간 목록
application_periods = ["VY", "HY", "LY", "YY"]

# 랜덤한 신청기간 선택
random_application_periods = [random.choice(application_periods) for _ in range(300)]

# 랜덤한 계좌번호 생성
random_account_numbers = [f"{random.randint(100000000000, 999999999999)}" for _ in range(300)]

# 랜덤한 전화번호 생성
random_phone_numbers = [f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}" for _ in range(300)]

# 랜덤한 LINKKEY 생성
random_linkkeys = [random.randint(1000000000, 9999999999) for _ in range(300)]

# 학과 목록
departments = ["IT융합 자율학부", "인뭉융합 자율학부", "사회융합 자율학부", "미디어컨텐츠융합 자율학부", "[유한][UH] 의료뷰티학과", "[유한][UH] 컴퓨터소프트웨어공학과", "[유한][UH] 패션디자인학과"]

# 랜덤한 학과 선택
random_departments = [random.choice(departments) for _ in range(300)]

# CSV 파일 생성
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["기숙사", "상태", "차수", "성별", "이름", "학번", "신청방", "신청기간", "확정방", "HP", "보증금", "기숙사비", "기숙사비(2)", "공공요금", "청구액합계", "입금액", "환블금액", "은행", "가상계좌", "LINKKEY", "대학학과"])
    for i in range(300):
        writer.writerow([ "B","A",random_application_periods[i],random_genders[i],random_names[i],random_student_numbers[i],"02",random_application_periods[i],"",random_phone_numbers[i],"50,000","1,021,410","","",random_application_periods[i],"0","0","대전은행",random_account_numbers[i],random_linkkeys[i], random_departments[i]])
=======
>>>>>>> 22544b2ea057b9b65194dabd86620739cb76d8df
