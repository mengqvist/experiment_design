# Experimental Design Generator

This package provides functions to generate various experimental designs, including Plackett-Burman and Fractional Factorial designs. These designs are used for efficient screening and analysis of multiple factors in experimental studies.

## Installation

You can install the package using pip:

```
pip install expdesign
```

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