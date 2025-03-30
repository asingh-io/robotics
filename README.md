# robotics


### Addition code-server vm tricks 

To fix the cloned VM has the same IP follow

'''
sudo hostnamectl set-hostname <new-hostname>

sudo echo -n > /etc/machine-id
sudo rm /var/lib/dbus/machine-id
'''