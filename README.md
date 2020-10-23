# Nu's dad company (RFID Reader) example code
This code is for educational purpose only. Feel free to use this code on your own risk.

## Required hardwares
* Raspberry pi
* RDM6300 RFID Reader (125Khz)
* 2 resistors for voltage dividing (5v to 3v output)
* Raspi power supply

## Required libraries
* **pyserial**: install using the command `python -m pip install pyserial`

## Prepare Raspi to run the code
* Disable all bluetooth services
  * Open the file `/boot/config.txt` and add this line `dtoverlay=disable-bt`
  * run the following commands.
    `sudo systemctl disable hciuart.service`
    `sudo systemctl disable bluealsa.service`
    `sudo systemctl disable bluetooth.service`
* Enable `UART` and disable `SSH serial`
