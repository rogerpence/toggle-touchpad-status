### Toggle touchpad status on Ubuntu 14.04 on Bonobo

`get-touchpad-id.py` is a little Python script that sets the touchpad status on System 76's Bonobo running Ubuntu 14.04.

`tp` is a Bash script uses `get-touchpad-id.py` to toggle the touchpad status. `./tp on` toggles the touch pad on and `./tp off' (or any other argument actually) toggles the keypad off. ./tp' without arguments shows a little help.

To avoid needing to type the `./` for the `tp` Bash script, add this alias:

    alias tp='./tp'
