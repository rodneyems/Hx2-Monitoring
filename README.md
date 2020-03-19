# Tellos Hx2 hybrid monitoring and remoting
> This software aims to remotely monitor and operate Tellos Hx2 Hybrids.

Developed in Python this software uses the GPIO of the hybrids in conjunction with an arduino Mega to monitor which hybrids are used and also allows to disconnect the hybrids remotely (activity that was previously done in the cold room).

This software provides:
1. Monitoring status ON / OFF;
2. Sound alert when changing status;
3. Hang up call remotely;
4. Simple log with date and time of connections and disconnections;
5. Send a log to database via request.

![](/images/softwareHib.png)

## Installation

For use this Software do you need: 

- To Python 3
    - How to install in [Windows](https://phoenixnap.com/kb/how-to-install-python-3-windows).
    - How to install in [Mac](https://programwithus.com/learn-to-code/install-python3-mac/).
    - How to install in [Linux](https://docs.python-guide.org/starting/install3/linux/).
- Mega Arduino with Standard Firmata
    - How to configure [Standard Firmata](https://www.instructables.com/id/Arduino-Installing-Standard-Firmata/) on Arduino.  
    _PS.:_You need to add the command line below or your hybrids will Hang Up whenever the program is started
![](/images/commandLine.jpeg)

## Usage example

Below is a diagram of how to perform the interconnections to command remotely the 2 hybrids (Both in the same rack unit).

![](/images/circuit.jpeg)

## Software configuration

To use this software in your environment, change the following files:
- folder /audio: In this folder, there are the sounds that are reproduced in the status change. To generate the audio files [Click Here](https://ttsmp3.com/). 

- folder /images: In this folder, there are the images of the hybrids. To edit with your phone numbers, use Paint or your favorite editing software.

In my case, I use seven rack units, totaling 14 phone extensions. Adapt the code to your needs.

## Release History

* 0.0.1
    * Software Done

## Meta

Rodney Martins – rodney.martins@live.com

[https://github.com/rodneyems](https://github.com/rodneyems)

## NOTES

This is my first code and I had no previous programming knowledge. The software in question has been in use for 1 year on my job and no bugs were found.

Sorry for grammatical errors, I don't speak English very well.

Thank's
