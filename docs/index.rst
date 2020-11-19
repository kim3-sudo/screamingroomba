Screaming Roomba Documentation
##############################

*Note: This is a living document, so it'll probably change between this time and the next time you read it, if I'm actively working on this project.*

About the Screaming Roomba
**************************

The Screaming Roomba is a modified and retrofitted standard Roomba that can move as normal but senses collisions and makes noise based off of that. To accomodate the new logical electronics, the succ has been removed. This low-cost project can hopefully allow enthusiasts to get into physical motor control and robotic design.

The inspiration for this project is the venerable Michael Reeves and his screaming roomba. However, I'd like this project to be more open to community involvement by making the plans open and not requiring any special tools. This project should be mostly buildable with a pair of scissors, a precision screwdriver kit (we recommend `iFixit's Pro Tech Toolkit <https://www.ifixit.com/Store/Tools/Pro-Tech-Toolkit/IF145-307>`_), a wire stripper, some side cutters, and a few hours. The robot is designed to be hacked, and there's still plenty of input/output left in the GPIO pins of the Raspberry Pi that is being used. This additional input and output could be used to run LEDs, piezo-speakers, or anything else that could ordinarily be run off of GPIO.

.. toctree::
  :maxdepth: 1
  :caption: Build Guide

  guide/tools
  guide/assembly
  guide/software_installation

.. toctree::
  :maxdepth: 1
  :cpation: Operation
  
  operation/testing
  operation/checklist
