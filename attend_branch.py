import os

def calculate_rate():
    if not os.path.exists("attendance.txt"):
        print("기록이 없습니다.")
        return

    with open("attendance.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 데이터 정리
    records = [line.strip().split(",") for line in lines]
    names = [r[0] for r in records]
    dates = set([r[1] for r in records]) # 중복 제거한 총 날짜 수
    total_days = len(dates)

    print(f"\n--- 출석 현황 (총 {total_days}일 기준) ---")
    unique_names = set(names)
    for name in unique_names:
        count = names.count(name)
        rate = (count / total_days) * 100
        print(f"{name}: {count}회 출석 ({rate:.1f}%)")

# 기존 코드 마지막 부분에 calculate_rate() 호출 추가
# ... (이름 입력받고 저장하는 코드) ...
calculate_rate()