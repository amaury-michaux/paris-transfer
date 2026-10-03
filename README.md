# Paris Transfer

A 2D driving simulation project built progressively in Python. The goal is to study how a neural driver generalizes to unfamiliar roads and recovers after a deviation, using a network implemented in NumPy.

## Current status

This first Pygame prototype displays a straight road, a dashed centerline and a car represented by a rectangle. The car is still stationary: vehicle dynamics, sensors and the neural driver have not been implemented yet. No learning or generalization results are available at this stage.

## Installation and launch

The current development environment uses Python 3.14.6. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m scripts.demo
```

Interactive execution requires a graphical environment.

## Controls

- `R`: reset the car's position.
- `Escape` or closing the window: quit.

## Prototype verification

A headless smoke check using SDL's `dummy` drivers exercised drawing one frame, the reset key, exiting with `Escape` and shutting down Pygame. Installed dependency consistency was also checked with `python -m pip check`. This check does not validate the window's appearance on a real display.

## Next step

Add vehicle movement with explicit units and a fixed simulation timestep, then verify straight-line motion. Rendering should read the simulation state so that future evaluations can run without a window.
