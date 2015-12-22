


![mypic](http://claritytele.com/wp-content/uploads/2015/04/logo.png)

# Physical Computing : #
## Connecting a computer to the real world ##

** Resources: **
Raspberry Pi (any model),  SD card with Raspbian Jessie, breadboard, Pi leaf pin label, 220 Ohm resistors, Variety of Colours of LED, Variety of coloured link wires with socket to connect to GPIO pin.

### Introduction ###
In this series we are going to look at connecting our computer to stuff and then using our programs to react to events and control things.


1. The Electrical Circuit
1. Lights and switches
2. Lets look at a Raspberry Pi
1. Scratch meets the real world
1. Letting Python out of its cage


Appendices & Data Sheets
1. Raspberry Pi pin numbering
1. LEDs current calculation
1. Resistor Colour Codes
1. Pi Leaf


<div class="page-break" />
### The Electrical Circuit ###
We are going to make a little **light** turn on and off by pressing a **switch**.

We need to use a power source (a **battery**) to push an electrical current down some wire and through the bulb and back to the battery.  This current flowing around a loop or **circuit** will make the bulb light up.

A switch is just a handy way to break the circuit and so stop the flow of electricity.

Electricity only flows through **conductors** like wire, tin foil, water, nails ... It won't flow through insulators like plastic, wood, clay ...

Lets use a battery, a switch, some wire and a bulb to make a torch.  You have some wire with "crocodile clips" to make the circuit.

![Diag: a torch circuit]()

There are a few things in your tray can you use your torch circuit to test all the things ... which ones are conductors? which ones are insulators?

#### Introducing the Breadboard ####
Crocodile clips are a bit big and clumsy.  The breadboard is much neater, especially when you are using small lights like LED's.

Lets use the torch circuit to test the breadboard.  There are lots of wires joining holes together in the breadboard.  Can you use your torch circuit to find the pattern ... which holes are connected?





<div class="page-break" />
### Lights and switches ###
Lets make a new torch circuit using a press switch and LED.

![torch](https://cdn.tutsplus.com/mac/uploads/2013/10/completecircuit.png)

LED stands for light-emitting diode, which means that much like their diode cousins, they’re polarized. There are a handful of identifiers for finding the positive and negative pins on an LED. You can try to find the longer leg, which should indicate the positive, anode pin.

Or, if someone’s trimmed the legs, try finding the flat edge on the LED’s outer casing. The pin nearest the flat edge will be the negative, cathode pin.



<div class="page-break" />
### Look at a Raspberry Pi ###

|     |   |
| :------------- | :------------- |
|![pi versions](Pi_Versions_bb.png)       | Here you can see three versions of the Raspberry Pi.  Each one has a set of metal pins sticking out of the board at the top left of the picture. <br/><br/>The pins are used to send signals to and from the computer.  Many of they can be used for almost anything and controlled by your programmes. So they are called General Purpose Input Output pins, or GPIO for short. <br/><br/>On your Pi there should already be a piece of paper labeling the pins.<br/><br/>Each pin can turn on or off,or go HIGH or LOW in computing terms. When the pin is HIGH it outputs 3.3 volts (3v3); when the pin is LOW it is off    |

![Traffic Lights](single_LED_bb.png)

<div class="page-break" />
### Scratch Meets the Real World. ###


![Traffic Lights](traffic_light_LEDs_bb.png)

<div class="page-break" />
### Letting the Python out of its computer ###
