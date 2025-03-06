from datetime import datetime

def format_date(date_str):
    """Convert date string to formatted date"""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')

def calculate_reading_time(text):
    """Calculate reading time in minutes"""
    words = len(text.split())
    return round(words / 200)  # Assuming average reading speed of 200 words per minute
