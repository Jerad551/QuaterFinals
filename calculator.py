"""
Calculator module with duplicated code.
This demonstrates common code duplication patterns that need refactoring.
"""


class Calculator:
    """A calculator with duplicated validation logic."""
    
    def add(self, a, b):
        """Add two numbers with validation."""
        # Duplicate validation code #1
        if not isinstance(a, (int, float)):
            raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
        if a > 1e308 or a < -1e308:
            raise ValueError(f"Value 'a' is out of range: {a}")
        if b > 1e308 or b < -1e308:
            raise ValueError(f"Value 'b' is out of range: {b}")
        
        result = a + b
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers with validation."""
        # Duplicate validation code #2
        if not isinstance(a, (int, float)):
            raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
        if a > 1e308 or a < -1e308:
            raise ValueError(f"Value 'a' is out of range: {a}")
        if b > 1e308 or b < -1e308:
            raise ValueError(f"Value 'b' is out of range: {b}")
        
        result = a - b
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers with validation."""
        # Duplicate validation code #3
        if not isinstance(a, (int, float)):
            raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
        if a > 1e308 or a < -1e308:
            raise ValueError(f"Value 'a' is out of range: {a}")
        if b > 1e308 or b < -1e308:
            raise ValueError(f"Value 'b' is out of range: {b}")
        
        result = a * b
        return result
    
    def divide(self, a, b):
        """Divide two numbers with validation."""
        # Duplicate validation code #4
        if not isinstance(a, (int, float)):
            raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
        if a > 1e308 or a < -1e308:
            raise ValueError(f"Value 'a' is out of range: {a}")
        if b > 1e308 or b < -1e308:
            raise ValueError(f"Value 'b' is out of range: {b}")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        return result


class DataProcessor:
    """A data processor with duplicated formatting logic."""
    
    def format_user_data(self, user):
        """Format user data for display."""
        # Duplicate formatting code #1
        name = user.get('name', 'Unknown')
        email = user.get('email', 'No email')
        age = user.get('age', 'N/A')
        
        output = f"Name: {name}\n"
        output += f"Email: {email}\n"
        output += f"Age: {age}\n"
        output += "-" * 40 + "\n"
        
        return output
    
    def format_admin_data(self, admin):
        """Format admin data for display."""
        # Duplicate formatting code #2
        name = admin.get('name', 'Unknown')
        email = admin.get('email', 'No email')
        age = admin.get('age', 'N/A')
        
        output = f"Name: {name}\n"
        output += f"Email: {email}\n"
        output += f"Age: {age}\n"
        output += "-" * 40 + "\n"
        
        return output
    
    def format_guest_data(self, guest):
        """Format guest data for display."""
        # Duplicate formatting code #3
        name = guest.get('name', 'Unknown')
        email = guest.get('email', 'No email')
        age = guest.get('age', 'N/A')
        
        output = f"Name: {name}\n"
        output += f"Email: {email}\n"
        output += f"Age: {age}\n"
        output += "-" * 40 + "\n"
        
        return output


class FileHandler:
    """A file handler with duplicated error handling."""
    
    def read_config_file(self, filepath):
        """Read configuration file."""
        # Duplicate error handling #1
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
    
    def read_data_file(self, filepath):
        """Read data file."""
        # Duplicate error handling #2
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
    
    def read_log_file(self, filepath):
        """Read log file."""
        # Duplicate error handling #3
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
