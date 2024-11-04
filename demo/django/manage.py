#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access system-specific parameters and functions

def main():
    # Set the default environment variable for Django's settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    
    try:
        # Attempt to import the function for executing Django commands from the command line
        from django.core.management import execute_from_command_line
    except ImportError as exc:  # Handle the case where the import fails
        # Raise an ImportError with a message about Django not being found
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute the command line with the arguments provided to the script
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()  # Call the main function when the script is executed directly