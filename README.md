# robotics


### Addition code-server vm tricks 

To fix the cloned VM has the same IP follow

'''
sudo hostnamectl set-hostname <new-hostname>

sudo echo -n > /etc/machine-id
sudo rm /var/lib/dbus/machine-id
'''

### git setting

```
git config --global pull.rebase true
git config --global pull.ff false  
git config --global user.name  "Anand Singh"
git config --global user.email  "asingh.sqm@gmail.com"
```