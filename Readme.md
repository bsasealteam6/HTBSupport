# Random HTB support scripts
## genMachines.py
### Usage
1. Run `cp .env.example .env` and place your HTB API token in the quotations.  Your HTB API token can be found [here](https://app.hackthebox.com/profile/settings), and is labeled "Account Identifier".
2. Run `sudo cp /etc/hosts /etc/hosts.template && echo '{HTB}' | sudo tee -a /etc/hosts.template` to create a template version of your hosts file with a placeholder for the HTB IP addresses.  Any edits you make in the future should be made to the /etc/hosts.template file.  This is to prevent the script from overwriting your hosts file changes.
3. 
    * `sudo python3 genMachines.py` will update your hosts file with the current HTB IP addresses.  You can run this script as often as you like, and it will only update the HTB IP addresses.
    * `genMachines.py -h` will display the help menu.
    * `genMachines.py -p` will print the current HTB IP addresses to the console, in a format that would be easy to add to your hosts file.