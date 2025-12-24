"""
Tests for refactored calculator module.
These tests verify that the refactored code maintains the same behavior.
"""
import pytest
from calculator_refactored import Calculator, DataProcessor, FileHandler


class TestCalculator:
    """Test the refactored Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add_valid_numbers(self):
        """Test adding two valid numbers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(0, 0) == 0
    
    def test_add_invalid_type(self):
        """Test add with invalid type."""
        with pytest.raises(TypeError):
            self.calc.add("5", 3)
        with pytest.raises(TypeError):
            self.calc.add(5, "3")
    
    def test_subtract_valid_numbers(self):
        """Test subtracting two valid numbers."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-5, 3) == -8
        assert self.calc.subtract(0, 0) == 0
    
    def test_multiply_valid_numbers(self):
        """Test multiplying two valid numbers."""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide_valid_numbers(self):
        """Test dividing two valid numbers."""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(-6, 3) == -2
    
    def test_divide_by_zero(self):
        """Test division by zero."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)


class TestDataProcessor:
    """Test the refactored DataProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
    
    def test_format_user_data(self):
        """Test formatting user data."""
        user = {'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
        result = self.processor.format_user_data(user)
        assert 'John Doe' in result
        assert 'john@example.com' in result
        assert '30' in result
    
    def test_format_admin_data(self):
        """Test formatting admin data."""
        admin = {'name': 'Admin User', 'email': 'admin@example.com', 'age': 35}
        result = self.processor.format_admin_data(admin)
        assert 'Admin User' in result
        assert 'admin@example.com' in result
        assert '35' in result
    
    def test_format_guest_data(self):
        """Test formatting guest data."""
        guest = {'name': 'Guest User', 'email': 'guest@example.com', 'age': 25}
        result = self.processor.format_guest_data(guest)
        assert 'Guest User' in result
        assert 'guest@example.com' in result
        assert '25' in result


class TestFileHandler:
    """Test the refactored FileHandler class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.handler = FileHandler()
    
    def test_read_nonexistent_file(self):
        """Test reading a file that doesn't exist."""
        result = self.handler.read_config_file('/nonexistent/file.txt')
        assert result is None
