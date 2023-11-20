import pandas as pd
from datetime import datetime
import re

with open(r"C:\Users\Subhajit Paul\Desktop\whatsapp_chat_analyzer\WhatsApp Chat with TNU 4th YEAR CSE (20-24).txt", "rb") as f:
    data = f.read().decode("utf-8")

pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

messages = re.split(pattern, data)[1:]
dates = re.findall(pattern, data)
df = pd.DataFrame({'user_message': messages, 'message_date': dates})
d = lambda x: datetime.strptime(x, '%m/%d/%y, %H:%M - ')
print(df['message_date'].apply(d))
