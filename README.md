<h1>무작위 학생 정보 생성 스크립트</h1>

<p>이 스크립트는 Python을 사용하여 무작위 학생 정보를 생성하고 CSV 파일에 저장하는 기능을 제공합니다. 학생들의 성별, 이름, 학번, 차수, 현재 상태 등의 정보를 무작위로 생성하여 파일로 출력합니다.</p>

<h2>사용법</h2>
<p>Python 3.x 환경이 필요합니다.</p>
<ol>
  <li>의존성 패키지 설치:</li>
  <code>python-dateutil</code> 의존성 패키지를 설치합니다. 아래 명령어를 실행하세요:
  <pre><code>pip install python-dateutil</code></pre>

  <li>스크립트 실행:</li>
  <p>프로젝트 디렉토리에서 아래의 코드를 실행하여 무작위 학생 정보를 생성하고 CSV 파일에 저장할 수 있습니다:</p>
  <pre><code>import random
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 코드 내용 생략...

# CSV 파일 생성
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "성별", "학번", "차수", "현재상태", "생년월일", "기숙사", "전공", "학년", "기간",
                     "호실", "배정방", "입사일자", "퇴사일자", "차수시작일", "차수종료일", "HP", "사회코드", "사회명", "ZIP", "LINKKEY", "주소"])
    for i in range(300):
        writer.writerow([random_names[i], random_genders[i], random_student_numbers[i], random_rounds[i], random_current_statuses[i], random_birthdays[i], "B", random_departments[i], str(random_grades[i]) + "학년", random_application_periods[i],
                         "02", random_rooms[i], random_entry_dates[i], "", random_entry_dates[i], random_end_dates[i], random_phone_numbers[i], random_social_codes[i], random_social_names[i], random_zip_codes[i], random_addresses[i]])
  </code></pre>
  <p>위의 코드를 실행하면 <code>output.csv</code>라는 이름의 CSV 파일이 생성되고, 그 안에 무작위로 생성된 학생 정보가 저장됩니다.</p>
</ol>
<br/>
<h1>데이터 구성</h1>
   
  <ul>
        <li>이름: random_names</li>
        <li>성별: random_genders</li>
        <li>학번: random_student_numbers</li>
        <li>차수: random_rounds</li>
        <li>현재상태: random_current_statuses</li>
        <li>생년월일: random_birthdays</li>
        <li>기숙사: "B"</li>
        <li>전공: random_departments</li>
        <li>학년: [random_grade + "학년" for random_grade in random_grades]</li>
        <li>기간: random_application_periods</li>
        <li>호실: "02"</li>
        <li>배정방: random_rooms</li>
        <li>입사일자: random_entry_dates</li>
        <li>퇴사일자: ""</li>
        <li>차수시작일: random_entry_dates</li>
        <li>차수종료일: random_end_dates</li>
        <li>HP: random_phone_numbers</li>
        <li>사회코드: random_social_codes</li>
        <li>사회명: random_social_names</li>
        <li>ZIP: random_zip_codes</li>
        <li>LINKKEY: random_linkkeys</li>
        <li>주소: random_addresses</li>
    </ul>
  
</br>

<h2>라이선스</h2>

<p>이 프로젝트는 MIT 라이선스 하에 제공됩니다. 자세한 내용은 <a href="./https://ko.wikipedia.org/wiki/MIT_%ED%97%88%EA%B0%80%EC%84%9C">LICENSE</a>을 참조하세요.</p>
