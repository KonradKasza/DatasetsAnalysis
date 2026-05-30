from ucimlrepo import fetch_ucirepo 
  
individual_household_electric_power_consumption = fetch_ucirepo(id=235) 
  
X = individual_household_electric_power_consumption.data.features 
y = individual_household_electric_power_consumption.data.targets 
  
print(individual_household_electric_power_consumption.metadata) 
  
print(individual_household_electric_power_consumption.variables) 

print("\n--- PIERWSZE 5 WIERSZY (DANE WEJŚCIOWE) ---")
print(X.head())

print("\n--- PODSTAWOWE STATYSTYKI OPISOWE ---")
print(X.describe())
