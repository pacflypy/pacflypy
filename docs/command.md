# Command Class

## Import the Module
```python
from pacflypy.command import command
```

## Create a Command
```python
# Main Programm 'apt'
cmd = command(programm='apt', safe_output=False, shell=False)
```

Over the Options Flags shell and safe_output talk we later.

## Add a Argument

Argument for Argument

```python
# We add 'install', '-y' and 'wget'
cmd.arg('install')
cmd.arg('-y')
cmd.arg('wget')
```

or directly as List

```python
arguments = []
arguments.extend(['install', '-y', 'wget'])
cmd.args(arguments)
```

## Get the Actually Command or the Executed Status

```python
exec_command = cmd.get_command()
status = cmd.get_executed()
```
