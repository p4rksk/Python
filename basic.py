import os

from google import genai
import requests


# 1. 환경변수에서 API 키를 자동으로 가져옵니다.
# (GOOGLE_API_KEY라는 이름으로 등록하셨다면 별도 입력 없이 작동합니다.)
client = genai.Client() 

# 2. USGS API에서 최근 1시간 동안 발생한 규모 4.5 이상의 지진 데이터 가져오기 
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4.5"
response_api = requests.get(url)
data = response_api.json()

# 가장 최근 지진 발생 지역 
if data['features']:
    latest_earthquake = data['features'][0]
    target_place = latest_earthquake['properties']['place']
    target_mag = latest_earthquake['properties']['mag']
    target_time = latest_earthquake['properties']['time']

    print(f" 감지 성공 위치: {target_place}, 규모: {target_mag}")
    print(" AI가 상황을 분석 중입니다...")

    # 3. AI에게 전달할 '미션' (프롬프트)
    prompt = f"""
    당신은 지진 재난 대응 전문 에이전트입니다. 
    다음 지진 데이터를 분석하여 주민들에게 전달할 '긴급 대피 가이드'를 작성하세요.
    
    [지진 데이터]
    - 위치: {target_place}
    - 규모: {target_mag}
    - 시간: {target_time}
    
    [요구사항]
    1. 위험 수준을 (상, 중, 하)로 명시하세요.
    2. 지진 규모에 따른 예상 피해 상황을 짧게 설명하세요.
    3. 주민들이 지금 당장 해야 할 행동 요령을 3가지 번호로 나열하세요.
    4. 말투는 아주 긴박하고 전문적이어야 합니다.
    """
    
    # 4. AI 실행
    ai_response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )

    # 5. 분석 결과 파일화 하기
    with open("earthquake_report.txt", "a", encoding="utf-8") as file:
        file.write(ai_response.text)
        file.write("\n" + "=" * 20 + "\n")

else:
    print("현재 분석할 만한 큰 지진이 없습니다.")    
        

    
 