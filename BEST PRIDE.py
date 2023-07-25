import matplotlib.pyplot as plt

# Coordinates of traverse
northing = [50.5210, 50.86944]
easting = [115.3903, 115.65083]

# Create figure
fig, ax = plt.subplots()

# Set limits of axes
ax.set_xlim([min(easting), max(easting)])
ax.set_ylim([min(northing), max(northing)])

# Create vertical lines
for i in range(len(easting)):
    ax.axvline(easting[i], ymin=0, ymax=1, color='gray', linestyle='--')

# Create horizontal lines
for i in range(len(northing)):
    ax.axhline(northing[i], xmin=0, xmax=1, color='gray', linestyle='--')

# Create grid labels
for i in range(len(easting)):
    ax.text(easting[i], max(northing) + 2, str(easting[i]), ha='center', va='bottom', fontsize=8)
for i in range(len(northing)):
    ax.text(min(easting) - 2, northing[i], str(northing[i]), ha='right', va='center', fontsize=8)

# Add title and axis labels
ax.set_title('Index Diagram of Traverse')
ax.set_xlabel('Easting (m)')
ax.set_ylabel('Northing (m)')

# Show plot
plt.show()
