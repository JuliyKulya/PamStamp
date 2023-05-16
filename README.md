# PamStamp
The main functionalities of the project can be summarized as follows:

- GUI Development: The code utilizes the tkinter library to create a graphical user interface window for the application.

- File Selection: The application allows the user to select and open two separate files (major and minor string files) using the file dialog.

- Data Parsing and Processing: The code reads and processes the data from the selected files, ignoring the first lines. It extracts the relevant data points such as time, major strain, and minor strain, and stores them in separate lists.

- Velocity Calculation: The application calculates the velocity by comparing the strain values at different time intervals and storing the results in the 'rychlost' list.

- Graphical Representation: Using the matplotlib library, the code plots three different graphs: velocity, major strain, and minor strain. The graphs are displayed in a separate window, with each line plotted in a different color. A legend is also included to distinguish the plotted lines.

- User Interaction: The application includes buttons for opening the file dialog and initiating the calculations.
