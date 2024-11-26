import pandas as pd

# Maak een dictionary met gegevens
data = {
    'Naam': ['John', 'Alice', 'Bob'],
    'Leeftijd': [25, 30, 35],
    'Stad': ['New York', 'Londen', 'Parijs']
}

# Converteer de dictionary naar een DataFrame
df = pd.DataFrame(data)

# Print de DataFrame
print(df)