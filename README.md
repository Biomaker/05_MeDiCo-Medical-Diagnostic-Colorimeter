
<img src="images/MeDiCo-BiomakerChallenge.jpg" alt="image"/>

## Synopsis

This project will aim to develop a low-cost colorimeter to detect colour changes in medical diagnostic assays, such as those for infectious diseases. The system will be intended for use in resource poor settings with the aim of improving diagnostic accuracy and sensitivity by removing user subjectivity from the interpretation of the test result. The system will be open-source and take a range of sample types to allow it to be easily adaptable to a large variety of colorimetric diagnostic assays.  

## Team
Andrew Stretton and Cassi Henderson      
    
<img src="images/AJS-Headshot-BiomakerChallenge.jpg" alt="image"/> <img src="images/HendersonCphoto.jpg" alt="image"/>


## Software

Explain functionality of software components (if any) as concisely as possible, developers should be able to figure out how your project solves their problem by looking at the code example. Ideally, this should be pseudo code or an abstract graphical representation of your code e.g entity relationship diagram. Consider adding a screenshot of your User Interface.

## Hardware

This device makes use of a Raspberry Pi 3 and a Pi Camera to take and process the images. A 3D printed box with sample loading drawer and several LEDs control the illumination of the sample. 

Assembly instructions:
1. Laser cut top.dxf from 3mm black PMMA.
2. Print box.stl and drawer.stl. We used PLA with 15% fill but adapt settings as needed for your printer.
3. Attach drawer handle through screw hole in center of drawer.
4. Fix 10 white LEDs in the 2 lines of holes in the top using Araldite Rapid. Allow to cure 24hr.
5. Attach Pi camera to center square hole in top. Attache camera to RaspPi as specified by manufacturer. Attach RaspPi to screen as specified by manufacturer.
6. Attach top to box using screws at each corner so Pi camera top is closest to the drawer opening.
7. Connect LEDs in parallel each with a ~200 Ohm resistor to a 9V battery. Insert a potentiometer into the circuit (see diagram).
<img src="images/circuit diagram.JPG" alt="image"/>
8. Adjust light with potentiometer to appropriate intensity. 
 

## Installation, Maintenance and Testing Guide

Provide instructions on usage, describe a test scheme and show how to run the tests with code and hardware configuration examples with some representative results.

## License

A short snippet describing the license (MIT, Apache, etc.) you have chosen to use
