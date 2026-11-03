import calendar
import json
from datetime import datetime, timedelta

def get_date_range(start_str, end_str):
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
    return [(start + timedelta(days=x)) for x in range((end - start).days + 1)]

def set_config():
    print("=== 출석 조회 설정 ===")
    print("1: 월 단위 조회 / 2: 특정 기간 조회")
    choice = input("선택: ")

    if choice == "1":
        year_month = input("조회할 년-월을 입력하세요 (예: 2026-11): ")
        year, month = map(int, year_month.split("-"))
        last_day = calendar.monthrange(year, month)[1]
        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-{last_day}"
    else:
        start_date = input("시작 날짜 (YYYY-MM-DD): ")
        end_date = input("종료 날짜 (YYYY-MM-DD): ")

    print(f"\n📍 설정 기간: {start_date} ~ {end_date}")
    print("수업 요일을 선택하세요:")
    print("1: 모든 날짜 (매일) / 2: 평일만 (월-금) / 3: 주말만 (토-일) / 4: 평일 + 특정 주말")
    
    day_choice = input("선택: ")
    allowed_weekdays = []

    if day_choice == "1":
        allowed_weekdays = [0, 1, 2, 3, 4, 5, 6]
    elif day_choice == "2":
        allowed_weekdays = [0, 1, 2, 3, 4]
    elif day_choice == "3":
        allowed_weekdays = [5, 6]
    elif day_choice == "4":
        allowed_weekdays = [0, 1, 2, 3, 4]
        if input("토요일 수업이 있나요? (y/n): ").lower() == 'y': allowed_weekdays.append(5)
        if input("일요일 수업이 있나요? (y/n): ").lower() == 'y': allowed_weekdays.append(6)

    # 수업 일수 자동 계산
    all_days = get_date_range(start_date, end_date)
    class_days = [d for d in all_days if d.weekday() in allowed_weekdays]
    
    config_data = {
        "start_date": start_date,
        "end_date": end_date,
        "allowed_weekdays": allowed_weekdays,
        "total_days": len(class_days)
    }

    with open("config.txt", "w", encoding="utf-8") as f:
        json.dump(config_data, f, ensure_ascii=False, indent=4)
    
    print(f"\n✅ 설정 완료! 총 수업 일수는 {len(class_days)}일입니다.")

if __name__ == "__main__":
    set_config()