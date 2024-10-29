from datetime import datetime, timedelta
from googletrans import Translator

translator = Translator()

class TimeLiner:
    def __init__(self, language="en"):
        self.language = language
    
    def set_language(self, language):
        """Set language for output translations."""
        self.language = language
    
    def format_time(self, dt, format_str="%Y-%m-%d %H:%M:%S"):
        """Format datetime object to a specific string format."""
        return dt.strftime(format_str)

    def time_since(self, past):
        """Get human-readable time since a past datetime."""
        delta = datetime.now() - past
        days = delta.days
        seconds = delta.seconds
        if days > 0:
            result = f"{days} days ago"
        elif seconds > 3600:
            result = f"{seconds // 3600} hours ago"
        elif seconds > 60:
            result = f"{seconds // 60} minutes ago"
        else:
            result = "just now"
        return self.translate_time_info(result)
    
    def add_time(self, dt, days=0, hours=0, minutes=0):
        """Add time to a given datetime."""
        return dt + timedelta(days=days, hours=hours, minutes=minutes)

    def subtract_time(self, dt, days=0, hours=0, minutes=0):
        """Subtract time from a given datetime."""
        return dt - timedelta(days=days, hours=hours, minutes=minutes)
    
    def get_date_range(self, start, end, step_days=1):
        """Get a list of dates between two dates."""
        delta = timedelta(days=step_days)
        current = start
        dates = []
        while current <= end:
            dates.append(current)
            current += delta
        return dates

    def translate_time_info(self, text):
        """Translate the time information to the set language."""
        try:
            translated = translator.translate(text, dest=self.language).text
            return translated
        except Exception as e:
            print(f"Translation failed: {e}")
            return text
