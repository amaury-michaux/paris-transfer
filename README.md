# Paris Transfer

A 2D driving simulation project built progressively in Python. The goal is to study how a neural driver generalizes to unfamiliar roads and recovers after a deviation, using a network implemented in NumPy.

## Current status

This first Pygame prototype displays a straight road, a dashed centerline and a car represented by a rectangle. The car is still stationary: vehicle dynamics, sensors and the neural driver have not been implemented yet. No learning or generalization results are available at this stage.

## Development roles and AI assistance

The development workflow assigns the following responsibilities:

| Contributor | Role |
|---|---|
| **Project author — Amaury Michaux** | Owns the research question, design decisions and final implementation. Writes and understands the core simulation, neural-network and evaluation code, validates changes and interprets the evidence. Chooses when to request assistance with a specific implementation task. |
| **Codex** | Acts as a research mentor: explains concepts, helps define interfaces and experiments, examines evidence and suggests the next useful step. Provides hints and diagnostics by default. When requested, edits documentation, manages GitHub publication or implements a scoped change. |
| **Gemini Flash** | Serves as the code-review and debugging partner: checks submitted functions, dimensions, units, gradients and edge cases; suggests tests and correction hints. The default review workflow leaves implementation and corrections with the author. |

These roles describe the working agreement. Assistance recorded so far includes Codex preparing and translating documentation, running a headless prototype check and managing GitHub publication. Codex has not written or modified the simulator code. No completed Gemini review is recorded in this repository yet.

AI feedback is checked against tests, replays and observed results. Substantial AI-generated or AI-modified implementations should be identified with the affected component and how they were validated.

### Public project and local working material

Project code, relevant tests, reproducible configurations, methods and selected results belong in this repository, including AI-assisted work that contributes to the deliverable. Personal mentoring notes, Codex/Gemini instructions, prompts, conversations, standalone learning exercises and drafts stay local. The `.gitignore` documents this boundary: `.local/mentoring/` holds guidance and session notes, `.local/exercises/` holds learning exercises, and `.local/scratch/` holds drafts and trials. All of `.local/` is excluded from Git.

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
