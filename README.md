# pacflypy

## Module Website

[Documentation](http://pacflypy.readthedocs.io/)

Hey I'm Pacflypy, a Hobby Programmer

This is a Module for Better Python Development

## Command Class

The Command Class in pacflypy is a class for Run Commands in the Terminal,

but stop, before you think that's to simple, Here few Examples:

```python
from pacflypy.command import command

# We Run a Simple Command Without Safing the Output
# We Initial the Command, for example, we use: 'apt-get install -y wget axel'
cmd = command(programm='apt-get', safe_output=False, shell=False)
cmd.arg('install')
cmd.arg('-y')
cmd.arg('wget')
cmd.arg('axel')
# Now we Print fast the COmmand to Terminal, but this is not Important
print(cmd.get_command()) # This will Show you the Full Command as String also, 'apt-get install -y wget axel'
# Now we run the command
cmd.run() # More need you not, this will Execute the Command

# Now we will become the Architecture with dpkg
cmd = command(programm='dpkg', safe_output=True, shell=False) # Initialize the Command
cmd.arg('--print-architecture')
print(cmd.get_command()) # This will Show you the Full Command as String also, 'dpkg --print-architecture'
cmd.run() # More need you not, this will Execute the Command and Safe the Output and now we get him
stdout = cmd.get_stdout() # Get the stdout
stderr = cmd.get_stderr() # Get the stderr
print('The Architecture is: ' + stdout)
```

Maybe that is to Complex, but the pacflypy modul includes a wrapper to this Here an Example with the Same Commands

```python
from pacflypy.system import run # Include the Wrapper in the Namespace

# We will run 'apt-get install -y wget axel'
run('apt-get install -y wget axel')

# For Safing Output
stdout, stderr = run('dpkg --print-architecture', safe_output=True)
print('The Architecture is: ' + stdout)
```

Crazy, that was Really Fast. But the Command Class have few Feutures more, maybe you want make 2 commands with the same programm, for example:

```python
from pacflypy.command import command
# We use APT
cmd = command(programm='apt')
cmd.arg('update')
cmd.run()
print(cmd.get_command())
cmd.reset()
cmd.arg('install')
cmd.arg('-y')
cmd.arg('wget')
cmd.arg('axel')
print(cmd.get_command())
cmd.run()
```

But the Pacflypy Modul have not only the Nice command class, maybe you want a little bit Style for your Terminal, for example:

```python
from pacflypy.style import styling

# We take now, red, blue, green and cyan
red, blue, green, cyan = styling.color(2), styling.color(3), styling.color(1), styling.color(6)
# Now we will print the red text
print(red + 'Hello World' + styling.reset)
print(blue + 'Hello World' + styling.reset)
print(green + 'Hello World' + styling.reset)
print(cyan + 'Hello World' + styling.reset)

# We take Styling, bold and italic
bold, italic = styling.style(1), styling.style(2)
print(bold + 'Hello World' + styling.reset)
print(italic + 'Hello World' + styling.reset)

# Maybe you want a little bit more, for example, Color and Style
green_bold = styling.pair(1, 1)
print(green_bold + 'Hello World' + styling.reset)

# Or use directly the Print Function
styling.print(text='Hello World', style=1, color=1)
```

But you must Now, Colors and Styles have an Code for example:

```python
"""
        Color Codes:
        0 - Reset
        1 - Green
        2 - Red
        3 - Blue
        4 - Yellow
        5 - Black
        6 - Cyan
        7 - Magenta
        8 - White
        Style Codes:
        0 - Reset
        1 - Bold
        2 - Italic
        3 - Underline
        4 - Strike
        5 - Reverse
        6 - Hidden
"""
```

With this Codes you can use the Style and Color Codes in your Project and this better as with the 'curses' Module

## Control File Rendering

Yes i have a Little Modul included for Control File Rendering, i don't know why, but i have fill it

Here for Example

```python
import pacflypy.control as control
import pacflypy.system as system

user = 'whoami'
path = system.path.join('home', user, 'control')
with open(path, 'r') as f:
    data = control.load(f)
    print(data)
package_name = data['Package']
package_version = data['Version']
package_architecture = data['Architecture']
package_maintainer = data['Maintainer']
package_description = data['Description']
# And Many many more, here you can find all Data from a Control File
```

Now we Create a Control File with my Module

```python
import pacflypy.control as control

data = {
    "Package": "test",
    "Version": "1.0",
    "Architecture": "all",
    "Maintainer": "Pacflypy",
    "Description": "This is a Test Package"
}

with open('control', 'w') as f:
    control.dump(file=f, data=data)
```

And now you have successfully create a Control File, but the Pacflypy Modul have not only the Control File Rendering.
