# Fractional Factorial Designs

Fractional Factorial designs are used when a full factorial design is not feasible due to resource constraints. These designs allow for the estimation of main effects and some interactions with fewer experimental runs than a full factorial design.

## Function: `generate_ffdesign`

### Parameters:
- `num_factors` (int): The number of factors in the design.
- `fraction` (float): The fraction of the full factorial design to use (e.g., 1/2, 1/4, 1/8).

### Returns:
- `numpy.ndarray`: The Fractional Factorial design matrix.

### Example:

```python
from expdesign import generate_ffdesign

# Generate a 1/2 fraction of a 2^5 factorial design
design = generate_ffdesign(5, fraction=1/2)
print(design)
```

### Notes:
- The design matrix consists of +1 and -1 values, where +1 represents the high level of a factor and -1 represents the low level.
- The resolution of the design depends on the chosen fraction. Higher resolutions allow for clearer separation of main effects and interactions.
- Care should be taken in choosing generators for the fractional design to avoid confounding of important effects.

For more information on constructing and analyzing Fractional Factorial designs, refer to standard texts on Design of Experiments.