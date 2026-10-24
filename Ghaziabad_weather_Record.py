import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Ghaziabad weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=28.64&longitude=77.48&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

'''
*
*
*
'''


#dat frame creation with the help of pandas 
#extrcting daily data 
daily_data = data['daily']

#creating a dataframe
data_frame = pd.DataFrame({
    'date': daily_data['time'],
    'maximum_temperature': daily_data['temperature_2m_max'],
    'minimum_temperature': daily_data['temperature_2m_min']
})

#converting json date string to datetime
data_frame['date'] = pd.to_datetime(data_frame['date'])
print(data_frame)

'''
*
*
*
'''
#visualising data with the help of matplotlib
# Create the plot
plt.figure(figsize=(10, 5.5))
plt.plot(data_frame['date'], data_frame['maximum_temperature'], marker='o', label='Maximum Temperature')
plt.plot(data_frame['date'], data_frame['minimum_temperature'], marker='o', label='Minimum Temperature')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Ghaziabad Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()


'''
*
*
*
'''

#saving it into a csv file

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
data_frame.to_csv('data/Ghaziabad_weather.csv', index=False)
print("Data saved to data/Ghaziabad_weather.csv")
print("so cold in ghaziabad")





