import requests

# 1. 실시간 지진 데이터를 제공하는 서버 주소 (JSON 형식)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

print("에이전트가 전 세계 실시간 지진 정보를 탐색 중입니다.")

# 2. 서버에 요청 보내고 응답 받기
response = requests.get(url)

data = response.json() # JSON 데이터를 파이썬 딕셔너리로 변환

# 3. 데이터 분석 (가장 최근 지진 1개 정보만 가져오기)
latest_quake = data['features'][0]['properties']

place = latest_quake['place']
mag = latest_quake['mag']

print("-" * 20)
print(f" 발생위치: {place}")
print(f" 규모: {mag}")

if mag >= 5.0:
    print("[경보] 5.0 이상의 지진이 발생했습니다 즉시 대피 경로를 확인하십시오")

if 3.0 < mag < 5.0:
    print("[주의] 중간 규모 지진입니다. 주의가 필요합니다.")
    
if mag <= 3.0:
    print("[안전] 미세한 진동입니다. 일상 생활이 가능합니다.")
    