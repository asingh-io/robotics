# robotics


### Addition code-server vm tricks 

To fix the cloned VM has the same IP follow

'''
echo -n > /etc/machine-id
rm /var/lib/dbus/machine-id
'''