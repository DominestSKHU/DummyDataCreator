import random
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime

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

# 차수 목록
rounds = ["202301HD01", "2023SMSK02", "2023SMUH02", "202301SC10"]

# 랜덤한 차수 선택
random_rounds = [random.choice(rounds) for _ in range(300)]

# 신청기간 목록
application_periods = ["VY", "HY", "LY", "YY"]

# 랜덤한 신청기간 선택
random_application_periods = [random.choice(application_periods) for _ in range(300)]

# 현재 상태 목록
current_statuses = ["A", "I"]

# 랜덤한 현재 상태 선택
random_current_statuses = [random.choice(current_statuses) for _ in range(300)]

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


# 랜덤한 생년월일 생성 (20대)
random_birthdays = [f"{str(random.randint(1996, 1999))[2:]}{random.randint(1, 12):02d}{random.randint(1, 28):02d}" for _ in range(300)]

# 랜덤한 학년 생성
random_grades = [random.randint(1, 4) for _ in range(300)]

# 랜덤한 배정방 생성
random_rooms = [f"B{random.randint(1, 10):02d}{random.randint(1, 9):02d}{random.choice(['A', 'B'])}" for _ in range(300)]

# 랜덤한 입사일자 생성 (2019년부터 2023년까지)
random_entry_dates = [f"{random.randint(2019, 2023)}{random.randint(1, 12):02d}{random.randint(1, 28):02d}" for _ in range(300)]

# 입사일자에 6개월 추가하여 차수종료일 생성
random_end_dates = []
for date in random_entry_dates:
    if date:
        end_date = (datetime.strptime(date, "%Y%m%d") + relativedelta(months=+6)).strftime("%Y%m%d")
        random_end_dates.append(end_date)
    else:
        random_end_dates.append("")


# 사회코드와 사회명 매핑
social_code_name_mapping = {
    "S0": "장애인",
    "S1": "저소득계층",
    "S2": "장기입사 희망자",
    "S3": "통학거리",
    "S4": "일반전형"
}

# 랜덤한 사회코드 생성
random_social_codes = [f"S{random.randint(0, 4)}" for _ in range(300)]

# 사회코드에 해당하는 사회명 생성
random_social_names = [social_code_name_mapping[code] for code in random_social_codes]

# 랜덤한 우편번호 생성
random_zip_codes = [f"{random.randint(10000, 99999)}" for _ in range(300)]

# 랜덤한 주소 생성
random_addresses = [f"서울시 가나구 다라동 {random.randint(1, 150)}-{random.randint(1, 150)}" for _ in range(300)]

# CSV 파일 생성
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "이름","성별", "학번", "차수","현재상태","생년월일", "기숙사","전공", "학년","기간",
                      "호실", "배정방", "입사일자", "퇴사일자", "차수시작일", "차수종료일", "HP", "사회코드", "사회명", "ZIP", "LINKKEY","주소" ])
    for i in range(300):
        writer.writerow([ random_names[i],random_genders[i],random_student_numbers[i],random_rounds[i],random_current_statuses[i],random_birthdays[i],"B",random_departments[i], str(random_grades[i])+"학년",random_application_periods[i],
                        "02",random_rooms[i],random_entry_dates[i],"",random_entry_dates[i],random_end_dates[i],random_phone_numbers[i],random_social_codes[i],random_social_names[i],random_zip_codes[i],random_addresses[i]])
