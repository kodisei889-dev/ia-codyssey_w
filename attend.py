import os

def main():
    print("--- 출석 관리 시스템 (교육장) ---")
    name = input("이름을 입력하세요: ")
    date = input("날짜를 입력하세요 (예: 2023-10-27): ")

    # attendance.txt 파일에 출석 기록 저장
    with open("attendance.txt", "a", encoding="utf-8") as f:
        f.write(f"{date} : {name}\n")
    
    print(f"\n[성공] {name}님의 출석이 기록되었습니다!")

if __name__ == "__main__":
    main()