# Plackett-Burman Designs

Plackett-Burman designs are used for screening experiments to identify the most important factors among a large set of factors. These designs are particularly efficient when only main effects are of interest and interactions can be assumed to be negligible.

## Function: `generate_pbdesign`

### Parameters:
- `num_factors` (int): The number of factors to include in the design.

### Returns:
- `numpy.ndarray`: The Plackett-Burman design matrix.

### Example:

```python
from expdesign import generate_pbdesign

# Generate a Plackett-Burman design for 7 factors
design = generate_pbdesign(7)
print(design)
```

### Notes:
- The number of runs in a Plackett-Burman design is always a multiple of 4.
- The design matrix consists of +1 and -1 values, where +1 represents the high level of a factor and -1 represents the low level.
- The first column of the design is always all +1s.

For more information on interpreting and analyzing Plackett-Burman designs, refer to standard texts on Design of Experiments.