import time
import sys

# Total time in seconds (5 minutes)
total_seconds = 5 * 60

# Cute emojis for the timer
clock_emoji = "⏰"
sparkle_emoji = "✨"
heart_emoji = "❤️"

print(f"{sparkle_emoji*3} Let's start the 5-minute timer! {sparkle_emoji*3}\n")

try:
    for remaining in range(total_seconds, 0, -1):
        minutes = remaining // 60
        seconds = remaining % 60
        timer_display = f"{clock_emoji} {minutes:02d}:{seconds:02d} {heart_emoji}"
        # \r moves cursor to beginning so it overwrites previous line
        print(timer_display, end="\r")
        time.sleep(1)
    print(f"\n{sparkle_emoji*3} Time's up! {sparkle_emoji*3} {heart_emoji*5}")
except KeyboardInterrupt:
    print("\nTimer stopped! 😢")