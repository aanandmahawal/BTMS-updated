import pandas as pd
import numpy as np

np.random.seed(42)

data = []

for _ in range(1000):
    voltage = np.random.uniform(3.0, 4.5)
    current = np.random.uniform(0.5, 5.0)
    ambient = np.random.uniform(15, 45)
    cycle = np.random.randint(1, 1000)

    power = voltage * current
    heat = current**2 * 0.015

    # Simulated outputs
    soh = 1 - (cycle / 1500) - (heat * 0.05)
    soh = max(0.5, min(1, soh))

    risk = 1 if (heat > 0.5 or ambient > 40) else 0

    data.append([voltage, current, power, heat, ambient, cycle, soh, risk])

df = pd.DataFrame(data, columns=[
    'voltage','current','power','heat','ambient','cycle','soh','risk'
])

df.to_csv("battery_data.csv", index=False)

print("Dataset created!")