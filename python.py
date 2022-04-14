import matplotlib.pyplot as plt
measuret_data = [25, 13, 45, 77, 89]

plt.plot(measuret_data)
plt.show()

measuret_data_str = [str(item) for item in measuret_data]

with open("data.txt", "w") as outfile:
    outfile.write("\n".join(measuret_data_str))