"""
Calculator module - REFACTORED VERSION without code duplication.
This demonstrates how to eliminate code duplication through proper abstraction.
"""


class Calculator:
    """A calculator with refactored validation logic."""
    
    MAX_VALUE = 1e308
    MIN_VALUE = -1e308
    
    def _validate_number(self, value, param_name):
        """
        Validate a single numeric input.
        
        Args:
            value: The value to validate
            param_name: Name of the parameter for error messages
            
        Raises:
            TypeError: If value is not int or float
            ValueError: If value is out of range
        """
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Expected int or float for '{param_name}', got {type(value).__name__}"
            )
        if value > self.MAX_VALUE or value < self.MIN_VALUE:
            raise ValueError(f"Value '{param_name}' is out of range: {value}")
    
    def _validate_inputs(self, a, b):
        """
        Validate both inputs for arithmetic operations.
        
        Args:
            a: First operand
            b: Second operand
            
        Raises:
            TypeError: If either value is not int or float
            ValueError: If either value is out of range
        """
        self._validate_number(a, 'a')
        self._validate_number(b, 'b')
    
    def add(self, a, b):
        """Add two numbers with validation."""
        self._validate_inputs(a, b)
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers with validation."""
        self._validate_inputs(a, b)
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers with validation."""
        self._validate_inputs(a, b)
        return a * b
    
    def divide(self, a, b):
        """Divide two numbers with validation."""
        self._validate_inputs(a, b)
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        return a / b


class DataProcessor:
    """A data processor with refactored formatting logic."""
    
    def _format_person_data(self, person_dict, defaults=None):
        """
        Format person data for display with configurable defaults.
        
        Args:
            person_dict: Dictionary containing person data
            defaults: Optional dictionary of default values
            
        Returns:
            Formatted string representation
        """
        if defaults is None:
            defaults = {
                'name': 'Unknown',
                'email': 'No email',
                'age': 'N/A'
            }
        
        name = person_dict.get('name', defaults['name'])
        email = person_dict.get('email', defaults['email'])
        age = person_dict.get('age', defaults['age'])
        
        output = f"Name: {name}\n"
        output += f"Email: {email}\n"
        output += f"Age: {age}\n"
        output += "-" * 40 + "\n"
        
        return output
    
    def format_user_data(self, user):
        """Format user data for display."""
        return self._format_person_data(user)
    
    def format_admin_data(self, admin):
        """Format admin data for display."""
        return self._format_person_data(admin)
    
    def format_guest_data(self, guest):
        """Format guest data for display."""
        return self._format_person_data(guest)


class FileHandler:
    """A file handler with refactored error handling."""
    
    def _read_file_with_error_handling(self, filepath):
        """
        Read a file with comprehensive error handling.
        
        Args:
            filepath: Path to the file to read
            
        Returns:
            File contents as string, or None if an error occurred
        """
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            print(f"Error: File not found - {filepath}")
            return None
        except PermissionError:
            print(f"Error: Permission denied - {filepath}")
            return None
        except Exception as e:
            print(f"Error: Unexpected error reading {filepath}: {e}")
            return None
    
    def read_config_file(self, filepath):
        """Read configuration file."""
        return self._read_file_with_error_handling(filepath)
    
    def read_data_file(self, filepath):
        """Read data file."""
        return self._read_file_with_error_handling(filepath)
    
    def read_log_file(self, filepath):
        """Read log file."""
        return self._read_file_with_error_handling(filepath)
