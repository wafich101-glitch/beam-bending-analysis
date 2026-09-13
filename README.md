# Beam Bending Analysis

A Python tool that calculates and visualizes shear force and bending moment
diagrams for a simply supported beam subjected to multiple point loads.

## Overview

Given a beam of length `L` with any number of point loads at specified
positions, this script:

- Computes the support reactions using static equilibrium
- Calculates the shear force `V(x)` and bending moment `M(x)` at every
  point along the beam
- Plots the Shear Force Diagram and Bending Moment Diagram, with vertical
  markers showing each load's position

## Example

For a 6 m beam with three point loads:

```python
L = 6.0
loads = np.array([10, 15, 8])        # kN
positions = np.array([1.5, 3.0, 4.5]) # m from the left support
```

Running the script outputs the reaction forces:
RA = 16.67 kN
RB = 16.33 kN


and generates two plots showing how shear force and bending moment vary
along the beam, with each load's location marked.

## How to run

```bash
pip install numpy matplotlib
python beam_analysis.py
```

## Physics background

Reactions are found from equilibrium of forces and moments. Shear force
and bending moment at any point `x` are computed using the superposition
principle: only loads located before `x` contribute to the internal
forces at that section.

## Status

This is an early version supporting point loads only. Planned extensions:
- Distributed loads
- Multiple support configurations
- Command-line or interactive input for beam parameters

## Author

Wafi Eddine Cheribet — Materials Engineering student, ENP
