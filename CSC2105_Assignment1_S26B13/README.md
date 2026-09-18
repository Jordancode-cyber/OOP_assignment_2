Name: FETA JORDAN
Registration Number: S26B13/131

NAME MANGLING
Name mangling is a technique that allows Python to automatically rename variables or methods prefixed with two leading underscores (__) inside a class. 
Its primary purpose is to prevent accidental name collisions when a class is extended or inherited by subclasses.

PROPERTY
@property is a built-in Python decorator that turns a class method into a readable "getter" attribute. It allows a method to be accessed using simple dot notation without invoking parentheses () explicitly
WHY:
It forces code to change from attribute access to function calls. 
@property allows developers to start with simple public attributes without breaking existing code

EXCEPTION HANDLING RESEARCH
Try: Encloses the block of code that might potentially raise an exception or error during execution.
Except: Catches and handles specific exceptions raised inside the try block, preventing program crash.
Else: Executes code only if no exceptions were raised in the try block.
Finally: Executes cleanup code regardless of whether an exception occurred or was handled.
ValueError: A built-in exception raised when a function receives an argument of correct type but invalid value.

FILE HANDLING RESEARCH
CORE FUNCTIONS:
open(): Opens a specified file path and returns a file object to interact with.
read(): Reads the contents of an open file and returns them as a string.   
write(): Writes a string of data to an open file.   
close(): Closes an open file connection, releasing memory and committing changes to disk.

FILE MODES AND USE CASES:
(Read Only(r)): Opens a file for reading; raises FileNotFoundError if missing. 
Use case: Reading stored transaction history.
(Write Only(w)): Creates a new file or completely overwrites an existing file. 
Use case: Generating a fresh daily summary report.
(Append Only(a)): Appends new data to the end of a file without destroying existing contents. 
Use case: Logging individual transaction entries continuously.   