[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QKp42A0s)
# 121CAT

1.Follow all of the steps on the [Book](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/93f2c351e3c34598b8b71bf2ebc40abe)

2. Complete the addigional features:
   ![image](https://github.com/user-attachments/assets/f99d7777-6fea-47e5-bf9a-fc452f835952)

3. Create a video of the app working with all of the additional features. Make the video small enough to render here or upload to a video service witha aviawable link.
### Video Link:
[![Video Link](https://img.youtube.com/vi/AyzPn01PsyM/0.jpg)](https://www.youtube.com/watch?v=AyzPn01PsyM)

4. Choose two snapshots of code that demonstrate the algorithm(s) used to implement the additional features. Explain the code in the screenshots.

#### Size Function
![Size Change Function](https://github.com/Aero-ComSci/121-egballl/blob/f2c3bfe3a10b4e47c516c081f2775114468c5754/images/Screenshot_889.png)
![Size List](https://github.com/Aero-ComSci/121-egballl/blob/f2c3bfe3a10b4e47c516c081f2775114468c5754/images/Screenshot_890.png)
The ```change_size()``` function randomly changes the turtle's size each time it is clicked.
 - It selects a new size from the predefined ```sizes``` list using ```rand.choice(sizes)```.
 - The function then updates the turtle's size with ```game_turtle.shapesize(new_size)```.

#### Stamp Function
![Stamp Function](https://github.com/Aero-ComSci/121-egballl/blob/3d74a1a0674bba6cfe2404c8978cbd7238da27c4/images/Screenshot_891.png)
![Color Lists](https://github.com/Aero-ComSci/121-egballl/blob/3d74a1a0674bba6cfe2404c8978cbd7238da27c4/images/Screenshot_892.png)
The ```stamp()``` function adds colorful imprints on the screen each time the player clicks the turtle.
 - It selects a random color from the predefined ```colors``` list using ```rand.choice(colors)```.
 - Sets the turtle's color to the selected color, then using ```stamp()``` to leave an imprint at the current position.
 - Then resets the turtle's color back to its original color ```spotcolor``` so that the main shape's color doesn't change permanently. 
