import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot library

# Function to draw scatter points
def draw_multiple_points():
    x_number_list = [1, 4, 9, 16, 25]  # List of x-coordinates
    y_number_list = [1, 2, 3, 4, 5]  # List of y-coordinates

    # Create a scatter plot
    plt.scatter(x_number_list, y_number_list, s=10)  # Plot points with size 10

    # Add title and labels to the plot
    plt.title("Extract Number Root")  # Title of the graph
    plt.xlabel("Number")  # Label for the x-axis
    plt.ylabel("Extract Root of Number")  # Label for the y-axis

    # Display the scatter plot
    plt.show()

# Ensure the function runs only when the script is executed directly
if __name__ == '__main__':
    draw_multiple_points()
