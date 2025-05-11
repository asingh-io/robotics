# robotics


### Addition code-server vm tricks 

To fix the cloned VM has the same IP follow

```
sudo hostnamectl set-hostname <new-hostname>

sudo echo -n > /etc/machine-id
sudo rm /var/lib/dbus/machine-id
```

### git setting

```
git config --global pull.rebase false
git config --global pull.ff true
git config --global user.name  "Anand Singh"
git config --global user.email  "asingh.sqm@gmail.com"
```

### Adding a keyboard shortcuts
 Add a keyboard shortcut to run the programs that we write. Ctrl-Shift-P > Preferences: Open Keyboard Shortcuts (JSON). Edit the JSON to add the keyboard shortcut to run the task. Paste in the code below at the bottom of keybindings.json.

```
[
    {
        "key" : "ctrl+shift+l",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-on-my-robot"
    },
    {
        "key" : "ctrl+alt+l",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-on-any-robot"
    },
    {
        "key" : "ctrl+shift+r",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-master_program-on-my-robot"
    },
    {
        "key" : "ctrl+alt+r",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-master_program-on-any-robot"
    }
]
```

## Run program on robot

* Turn the robot on and ensure the keyboard shortcut ctrl-shift-L runs the command, which should also run their program.
* Also, Ctrl-Shift-P > Tasks: Run task should pop up a menu with the correct entry. Watch the terminal and make sure the robot name is correct. If not, recheck that you completed step 11 correctly.
