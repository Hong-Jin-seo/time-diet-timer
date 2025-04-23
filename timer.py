import time

def countdown(minutes):
    total_seconds = int(minutes * 60)
    while total_seconds:
        if total_seconds == 5 * 60:
            mins, secs = divmod(total_seconds, 60)
            print(f"\n⏳ {mins:02d}:{secs:02d} (5분 남았어요!)")
        time.sleep(1)
        total_seconds -= 1

def start_pomodoro():
    print("✅ 타이머 시작됨!")
    while True:
        print("\n📚 집중 시간 시작! (25분)")
        countdown(25)
        print("\n🧘‍♀️ 휴식 시간~ (5분)")
        countdown(5)
        again = input("💬 다시 시작할까요? (y/n): ").lower()
        if again != 'y':
            print("🚀 수고했어요 다음에 또 타이머로 함께해요!")
            break

if __name__ == "__main__":
    start_pomodoro()
