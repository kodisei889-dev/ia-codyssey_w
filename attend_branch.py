import os
import json
import sys
from datetime import datetime

def show_attendance():
    if not os.path.exists("config.txt"):
        print("\n[!] 설정이 없습니다. 'python set_config.py'를 먼저 실행하세요.")
        sys.exit()
    
    with open("config.txt", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    start, end = config["start_date"], config["end_date"]
    allowed_weekdays = config["allowed_weekdays"]
    total_days = config["total_days"]

    if not os.path.exists("attendance.txt"):
        print("출석 기록이 없습니다.")
        return

    with open("attendance.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    official_records = []  # 정식 수업일 출석
    extra_records = []     # 수업 외 날짜 출석

    for line in lines:
        if ":" in line:
            date_str, name = [i.strip() for i in line.split(":")]
            if start <= date_str <= end:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
                if dt.weekday() in allowed_weekdays:
                    official_records.append((date_str, name))
                else:
                    extra_records.append((date_str, name))

    # 중복 제거 (하루에 여러 번 찍은 경우)
    official_set = sorted(list(set(official_records)))
    extra_set = sorted(list(set(extra_records)))

    # 1. 정식 현황 출력
    print(f"\n📅 조회 기간: {start} ~ {end} (수업일 {total_days}일)")
    print("=" * 45)
    print(f"{'이름':<10} {'출석횟수':<10} {'출석률'}")
    print("-" * 45)
    
    unique_names = sorted(set(r[1] for r in official_set))
    for name in unique_names:
        count = [r[1] for r in official_set].count(name)
        rate = (count / total_days) * 100
        print(f"{name:<10} {count:<10} {rate:.1f}%")
    
    # 2. 수업 외 날짜 출석 기록 출력 (경고성 알림)
    if extra_set:
        print("\n⚠️ [주의] 수업일이 아닌 날에 기록된 출석입니다:")
        for date, name in extra_set:
            weekday_name = ["월", "화", "수", "목", "금", "토", "일"][datetime.strptime(date, "%Y-%m-%d").weekday()]
            print(f" - {date}({weekday_name}): {name}")
        print("※ 위 기록은 공식 출석률 계산에서 제외되었습니다.")
    
    print("=" * 45)

if __name__ == "__main__":
    show_attendance()