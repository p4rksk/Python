agent_bag = ["웹 검색", "웹 개발", "자동화"]

def work_agent(work_name):
    if work_name in agent_bag:
        print(f"{work_name} 작업 하겠습니다.")
    else:
        print(f"{work_name}이 리스트에 없어 작업을 할 수 없습니다.")

work_agent("자동화")

