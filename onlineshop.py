from ucimlrepo import fetch_ucirepo 
  
online_shoppers_purchasing_intention_dataset = fetch_ucirepo(id=468) 
  
X = online_shoppers_purchasing_intention_dataset.data.features 
y = online_shoppers_purchasing_intention_dataset.data.targets 
  
print(online_shoppers_purchasing_intention_dataset.metadata) 
print(online_shoppers_purchasing_intention_dataset.variables) 

print("\n--- PIERWSZE 5 WIERSZY (DANE WEJŚCIOWE) ---")
print(X.head())

print("\n--- PODSTAWOWE STATYSTYKI OPISOWE ---")
print(X.describe())
