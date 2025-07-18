# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KABILAN M

*INTERN ID*: CT04CH1571

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH



### **Task Description: 5-Day Weather Forecast Visualization using Python**

####  **Objective:**

Build a Python application that fetches the 5-day weather forecast for **London** from the **OpenWeatherMap API** and visualizes the temperature trend using a line chart.



#### **Tools & Libraries Used:**

* **requests** – to make API calls and fetch weather data.
* **matplotlib** – to plot temperature data.
* **seaborn** – to enhance plot styling.
* **datetime** – to convert string dates into Python datetime objects.

All dependencies are listed in `req.txt`:

```txt
requests
matplotlib
seaborn
```


####  **How It Works:**

1. **API Request:**

   * The app makes a GET request to OpenWeatherMap’s 5-day forecast endpoint for London using your API key.
   * The response contains forecast data at 3-hour intervals.

2. **Data Processing:**

   * The script extracts the **date/time** (`dt_txt`) and **temperature** (`temp`) for each forecast entry.
   * It then converts the date string into a Python `datetime` object for proper plotting.

3. **Data Visualization:**

   * A line plot is created using Seaborn and Matplotlib.
   * X-axis: Date and Time
   * Y-axis: Temperature (°C)
   * The graph shows temperature trends over the 5-day period with data points every 3 hours.

4. **Output:**

   * The resulting graph is saved as **`weather_forecast.png`**, which visually represents temperature changes over the selected period.


####  **Final Output:**

The output image (`weather_forecast.png`) clearly shows fluctuations in temperature for London over a span of 5 days. Peaks and drops indicate changing weather patterns (e.g., daytime highs and nighttime lows).


#### **Usage Instructions:**

1. Install dependencies:

   ```bash
   pip install -r req.txt
   ```
2. Run the script:

   ```bash
   python app.py
   ```
3. Check the current directory for `weather_forecast.png`.


