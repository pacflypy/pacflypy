pacflypy
========

Hey, I'm Pacflypy, a hobby programmer.

This is a module for better Python development.

Command Class
--------------

The Command Class in pacflypy is a class for running commands in the terminal.

But wait, before you think that's too simple, here are a few examples:

.. code-block:: python

    from pacflypy.command import command

    # We run a simple command without saving the output
    # We initialize the command, for example, we use: 'apt-get install -y wget axel'
    cmd = command(program='apt-get', safe_output=False, shell=False)
    cmd.arg('install')
    cmd.arg('-y')
    cmd.arg('wget')
    cmd.arg('axel')
    # Now we quickly print the command to the terminal, but this is not important
    print(cmd.get_command())  # This will show you the full command as a string, also 'apt-get install -y wget axel'
    # Now we run the command
    cmd.run()  # That's all you need, this will execute the command

    # Now we will get the architecture with dpkg
    cmd = command(program='dpkg', safe_output=True, shell=False)  # Initialize the command
    cmd.arg('--print-architecture')
    print(cmd.get_command())  # This will show you the full command as a string also, 'dpkg --print-architecture'
    cmd.run()  # That's all you need, this will execute the command and save the output and now we get it
    stdout = cmd.stdout()  # Get the stdout
    stderr = cmd.stderr()  # Get the stderr
    print('The architecture is: ' + stdout)

Maybe that is too complex, but the pacflypy module includes a wrapper for this. Here is an example with the same commands:

.. code-block:: python

    from pacflypy.system import run  # Include the wrapper in the namespace

    # We will run 'apt-get install -y wget axel'
    run('apt-get install -y wget axel')

    # For saving output
    stdout, stderr = run('dpkg --print-architecture', safe_output=True)
    print('The architecture is: ' + stdout)

Crazy, that was really fast. But the Command Class has a few more features, maybe you want to make 2 commands with the same program, for example:

.. code-block:: python

    from pacflypy.command import command
    # We use APT
    cmd = command(program='apt')
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

But the Pacflypy module has not only the nice command class, maybe you want a little bit of style for your terminal, for example:

.. code-block:: python

    from pacflypy.style import styling

    # We take now, red, blue, green, and cyan
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

    # Maybe you want a little bit more, for example, color and style
    green_bold = styling.pair(1, 1)
    print(green_bold + 'Hello World' + styling.reset)

    # Or use directly the Print Function
    styling.print(text='Hello World', style=1, color=1)

But you must know, colors and styles have a code, for example:

.. code-block:: python

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

With these codes, you can use the style and color codes in your project, and this is better than with the 'curses' module.

Control File Rendering
----------------------

Yes, I have a little module included for control file rendering, I don't know why, but I have filled it.

Here for example:

.. code-block:: python

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
    # And many many more, here you can find all data from a control file

Now we create a control file with my module:

.. code-block:: python

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

And now you have successfully created a control file, but the Pacflypy module has not only the control file rendering.