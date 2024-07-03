# Experimental Design Generator
This package provides functions to generate various experimental designs, including Plackett-Burman and Fractional Factorial designs. These designs are used for efficient screening and analysis of multiple factors in experimental studies.

## Installation

This package provides multiple installation methods to suit different user needs.

### For Regular Users

If you just want to use the package, you have two options:

1. **Using pip**:
   ```
   pip install expdesign
   ```

2. **Using conda with environment.yml**:
   ```
   git clone https://github.com/yourusername/experimental-design.git
   cd experimental-design
   conda env create -f environment.yml
   conda activate expdesign
   ```

### For Developers

If you want to contribute to the project or run tests, you should set up the development environment:

1. **Using conda with environment-dev.yml**:
   ```
   git clone https://github.com/yourusername/experimental-design.git
   cd experimental-design
   conda env create -f environment-dev.yml
   conda activate expdesign-dev
   ```

2. **Using pip with requirements-dev.txt**:
   ```
   git clone https://github.com/yourusername/experimental-design.git
   cd experimental-design
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements-dev.txt
   pip install -e .
   ```

### Notes

- The development setup includes additional tools for testing, linting, and documentation.
- If you're using the development setup, make sure to activate the appropriate environment before working on the project.
- The `-e .` in the pip install command installs the package in editable mode, which is useful for development.

## Verifying Installation

After installation, you can verify that the package is working correctly by running:

```python
from expdesign import generate_pbdesign

# Generate a Plackett-Burman design for 7 factors
design = generate_pbdesign(7)
print(design)
```

If you see a matrix output without any errors, the installation was successful.

## Development Tools

If you've set up the development environment, you can use the following commands:

- Run tests: `pytest`
- Check code style: `flake8 .`
- Format code: `black .`
- Generate documentation: `cd docs && make html`

Remember to activate your development environment before running these commands.

## Usage

Here are basic examples of how to use the package:

```python
from expdesign import generate_pbdesign, generate_ffdesign

# Generate a Plackett-Burman design for 7 factors
pb_design = generate_pbdesign(7)
print("Plackett-Burman Design:")
print(pb_design)

# Generate a Fractional Factorial design for 5 factors at 2 levels (1/2 fraction)
ff_design = generate_ffdesign(5, fraction=1/2)
print("\nFractional Factorial Design:")
print(ff_design)
```

For more detailed usage instructions and examples, please refer to the documentation:
- [Plackett-Burman Designs](docs/plackett_burman.md)
- [Fractional Factorial Designs](docs/fractional_factorial.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.