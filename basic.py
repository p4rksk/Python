import os
from google import genai

# 1. 환경변수에서 API 키를 자동으로 가져옵니다.
# (GOOGLE_API_KEY라는 이름으로 등록하셨다면 별도 입력 없이 작동합니다.)
client = genai.Client() 

# 2. 분석할 데이터 (임의의 데이터)
target_place = "일본 도쿄 근해"
target_mag = 6.2

print(f" 에이전트 가동: {target_place}에서 규모 {target_mag} 지진 감지.")
print(" AI가 상황을 분석 중입니다...")

# 3. AI에게 전달할 '미션' (프롬프트)
prompt = f"""
당신은 지진 재난 대응 전문 에이전트입니다. 
다음 지진 데이터를 분석하여 주민들에게 전달할 '긴급 대피 가이드'를 작성하세요.

[지진 데이터]
- 위치: {target_place}
- 규모: {target_mag}

[요구사항]
1. 위험 수준을 (상, 중, 하)로 명시하세요.
2. 지진 규모에 따른 예상 피해 상황을 짧게 설명하세요.
3. 주민들이 지금 당장 해야 할 행동 요령을 3가지 번호로 나열하세요.
4. 말투는 아주 긴박하고 전문적이어야 합니다.
"""

# 4. AI 실행
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=prompt
)

# 5. 결과 출력
print("=" * 40)
print(response.text)
print("=" * 40)

# 6. 결과 파일로 기록하기
filename = "earthquake_report.txt"

with open(filename, "w", encoding="utf-8") as file: # 파일이름, 모드, 인코딩 방식 순서로 작성한다.
    file.write("--- AI 지진 분석 보고서 ---\n")
    file.write(response.text)
    file.write("\n\n")