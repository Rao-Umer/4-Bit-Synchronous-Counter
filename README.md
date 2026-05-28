# 4-Bit-Synchronous-Counter
# 4-Bit Synchronous Counter (1 → 10)

A clean Python simulation of a **4-bit synchronous up-counter** that counts from **1 to 10**. The project models the behaviour of real digital logic — four edge-triggered flip-flops (Q0–Q3) driven by a common clock — entirely in software, making it a useful reference for both digital electronics students and Python developers exploring hardware concepts.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Extending the Counter](#extending-the-counter)
- [License](#license)

---

## Overview

| Property | Value |
|---|---|
| Counter type | Synchronous (all flip-flops share one clock) |
| Bit width | 4 bits (Q3, Q2, Q1, Q0) |
| Count range | 1 – 10 (decimal) |
| Count direction | Up |
| Reset behaviour | Auto-rolls back to 1 after reaching 10 |
| Language | Python 3.8+ |
| Dependencies | None (standard library only) |

In a physical synchronous counter the flip-flop outputs all change **simultaneously** on the rising edge of the clock, unlike a ripple counter where the change propagates bit by bit. This simulation honours that constraint: the next state is computed in full before it is committed to the register.

---

## How It Works

```
Clock pulse N
      │
      ▼
┌─────────────────────────────────┐
│   Compute next state (N+1)      │  ← combinational logic
│   If state == 10 → next = 1     │
│   Else           → next += 1    │
└────────────────┬────────────────┘
                 │ simultaneous update
                 ▼
        Q3  Q2  Q1  Q0
         │   │   │   │
        [FF][FF][FF][FF]  ← flip-flops (state register)
```

Each "clock pulse" the `SynchronousCounter.clock_pulse()` method:

1. Calls `_compute_next_state()` to determine what the count should become.
2. Atomically replaces `self._state` with the result — mimicking the synchronous flip-flop update.
3. Increments the internal clock counter.

The 4-bit binary representation is derived on demand from the decimal state, matching what you would read off the Q3–Q0 output lines of a real IC such as the **74HC163**.

---

## Project Structure

```
4-bit-synchronous-counter/
│
├── four_bit_counter.py   # Main simulation — counter class + display helpers
└── README.md             # This file
```

---

## Getting Started

No external packages are required. All you need is Python 3.8 or newer.

### Clone the repository

```bash
git clone https://github.com/<your-username>/4-bit-synchronous-counter.git
cd 4-bit-synchronous-counter
```

### Run the simulation

```bash
python three_bit_counter.py
```

That's it — no `pip install`, no virtual environment setup needed.

---

## Usage

### Run a single cycle (default)

```python
from four_bit_counter import run_simulation

run_simulation(cycles=1)   # counts 1 → 10 once
```

### Run multiple cycles

```python
run_simulation(cycles=3)   # counts 1 → 10 three times in a row
```

### Use the counter class directly

```python
from four_bit_counter import SynchronousCounter

counter = SynchronousCounter(start=1, stop=10)

for _ in range(10):
    print(counter.state, counter.bits, counter.get_flip_flop_outputs())
    counter.clock_pulse()
```

### Custom range (e.g. 0 → 15, full 4-bit)

```python
counter = SynchronousCounter(start=0, stop=15)
```

### Reset the counter

```python
counter.reset()   # Forces state back to `start` immediately
```

---

## Sample Output

```
====================================================
  4-Bit Synchronous Counter  (Count: 1 → 10)
====================================================
  Clock  | Decimal |  Q3   Q2   Q1   Q0
----------------------------------------------------
    0    |    1    |   0    0    0    1
    1    |    2    |   0    0    1    0
    2    |    3    |   0    0    1    1
    3    |    4    |   0    1    0    0
    4    |    5    |   0    1    0    1
    5    |    6    |   0    1    1    0
    6    |    7    |   0    1    1    1
    7    |    8    |   1    0    0    0
    8    |    9    |   1    0    0    1
    9    |   10    |   1    0    1    0
   10    |    1    |   0    0    0    1
====================================================

  Simulation complete — 10 clock pulse(s) applied.
```

> **Reading the table** — each row is a snapshot of the four flip-flop outputs (Q3 = MSB, Q0 = LSB) captured on the rising edge of the clock. Clock 0 is the initial state before any pulse is applied.

---

## Extending the Counter

The `SynchronousCounter` class is intentionally kept minimal and easy to build on:

| Idea | How |
|---|---|
| Count **down** | Change `_compute_next_state` to decrement and wrap at `start` |
| **BCD counter** (0–9) | Set `start=0, stop=9` |
| Full 4-bit range (0–15) | Set `start=0, stop=15` |
| Add a clock frequency | Call `clock_pulse()` inside a `time.sleep()` loop |
| Export to CSV | Collect rows into a list and write with `csv.writer` |
| Visualise waveforms | Plot Q0–Q3 over time with `matplotlib` |

---

## License

This project is released under the **MIT License** — feel free to use, modify, and distribute it. See [`LICENSE`](LICENSE) for the full text.

---

*Built with Python. Inspired by the 74HC163 4-bit synchronous binary counter.*
