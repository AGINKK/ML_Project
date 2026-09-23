from datetime import datetime, timedelta


now = datetime.now()
print("Year:", now.year)  # (current year)
print("Month:", now.month)  # Output: 9

# 2. Format a date nicely
formatted = now.strftime("%B %d, %Y")
print("Formatted Date:", formatted)  # Output: September 16, 2026

# 3. Date math (Future and past dates)
future_date = now + timedelta(days=10)
print(
    "10 days from now:", future_date.strftime("%Y-%m-%d")
) 