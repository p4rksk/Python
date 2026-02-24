import requests
from urllib3 import request


# 구글 서버 접속 시도
response = requests.get("https://www.google.com")

# 결과
if response.status_code == 200:
    print("구글 서버 접속 성공!")
    print(f"가져온 데이터: {response.text[:100]}") # 일부 데이터 가져오기
else:
    print("연결에 실패했습니다.")