from datetime import date, timedelta

def get_date_in_n_days(n):
    today = date.today()
    future_date = today + timedelta(days=n)
    return future_date.strftime("%d %b %Y")  # Format the date

date_in_5_days = get_date_in_n_days(5)

print(date_in_5_days)