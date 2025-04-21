import matplotlib.pyplot as plt

# Data from the revenue by region table
years = list(range(2014, 2025))
us_canada = [8.0, 10.0, 13.0, 17.0, 22.0, 27.0, 34.0, 42.0, 50.0, 55.0, 60.0]
asia_pacific = [2.5, 3.0, 4.5, 6.0, 8.0, 10.0, 13.0, 16.0, 20.0, 25.0, 30.0]
europe = [2.0, 2.5, 3.5, 4.5, 6.0, 7.5, 9.0, 11.0, 15.0, 18.0, 20.0]
rest_of_world = [1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 10.0, 12.0, 15.0]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, us_canada, label='U.S. & Canada', marker='o')
plt.plot(years, asia_pacific, label='Asia Pacific', marker='o')
plt.plot(years, europe, label='Europe', marker='o')
plt.plot(years, rest_of_world, label='Rest of World', marker='o')

plt.title('Meta Revenue by Region (2014–2024)')
plt.xlabel('Year')
plt.ylabel('Revenue (in Billion USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.xticks(years)
plt.savefig('meta_revenue.png')