import pandas as pd

# 1. LOAD DATA
file_name = 'flights.csv.csv'
# We use 5000 rows to get a good mix of data
df = pd.read_csv(file_name, nrows=5000)
df = df.dropna(subset=['DEP_DELAY'])

# 2. AIRLINE-WISE DELAY ANALYSIS
airline_avg = df.groupby('AIRLINE')['DEP_DELAY'].mean().sort_values(ascending=False)

# 3. ROUTE RELIABILITY EVALUATION
route_avg = df.groupby(['ORIGIN', 'DEST'])['DEP_DELAY'].mean().sort_values(ascending=False).head(5)

# 4. DELAY RISK SCORING (The "Smart" part)
# We mark a flight as 'High Risk' if it's more than 15 mins late
df['IS_HIGH_RISK'] = df['DEP_DELAY'] > 15
risk_score = (df.groupby('AIRLINE')['IS_HIGH_RISK'].mean() * 100).sort_values(ascending=False)

# 5. PASSENGER-FOCUSED INSIGHTS
weather_issues = df[df['DELAY_DUE_WEATHER'] > 0].shape[0]
airline_issues = df[df['DELAY_DUE_CARRIER'] > 0].shape[0]

# --- PRINTING EVERYTHING FOR YOUR MAM ---
print("=== AIRLINE PERFORMANCE REPORT ===")
print("\n1. Slowest Airlines (Avg Minutes):")
print(airline_avg.head(5))

print("\n2. Highest Risk of Delay (% Chance):")
print(risk_score.head(5).map('{:.1f}%'.format))

print("\n3. Most Unreliable Routes:")
print(route_avg)

print("\n4. Why are flights delayed?")
print(f"- Weather Problems: {weather_issues} flights")
print(f"- Airline Mistakes: {airline_issues} flights")