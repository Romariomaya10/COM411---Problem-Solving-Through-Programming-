
import matplotlib.pyplot as plt

times = ["20.00", "20.30", "21.00", "21.30", "22.00"]
arsenal_fanbase = [3000000, 1200000, 800000, 800000, 1200000]

plt.plot(times, arsenal_fanbase, "r--")

plt.xlabel("Times")
plt.ylabel("Status of Arsenal Fanbase (mlns)")

plt.show()