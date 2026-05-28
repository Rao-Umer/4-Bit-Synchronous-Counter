NUM_BITS = 4
COUNT_START = 1
COUNT_END = 10


class SynchronousCounter:

    def __init__(self, start: int = COUNT_START, stop: int = COUNT_END) -> None:
        if not (0 <= start <= 15 and 0 <= stop <= 15):
            raise ValueError("start and stop must be in the range 0-15 for a 4-bit counter.")
        if start > stop:
            raise ValueError("start must be less than or equal to stop.")

        self._start = start
        self._stop = stop
        self._state = start
        self._clock_count = 0

    @property
    def state(self) -> int:
        return self._state

    @property
    def bits(self) -> str:
        return format(self._state, f"0{NUM_BITS}b")

    @property
    def clock_count(self) -> int:
        return self._clock_count

    def clock_pulse(self) -> None:
        next_state = self._compute_next_state()
        self._state = next_state
        self._clock_count += 1

    def reset(self) -> None:
        self._state = self._start
        self._clock_count = 0

    def get_flip_flop_outputs(self) -> dict:
        bits = self.bits
        return {
            "Q3": int(bits[0]),
            "Q2": int(bits[1]),
            "Q1": int(bits[2]),
            "Q0": int(bits[3]),
        }

    def _compute_next_state(self) -> int:
        if self._state >= self._stop:
            return self._start
        return self._state + 1


def _header() -> None:
    print("=" * 52)
    print("  4-Bit Synchronous Counter  (Count: 1 -> 10)")
    print("=" * 52)
    print(f"  {'Clock':^6} | {'Decimal':^7} | {'Q3':^4} {'Q2':^4} {'Q1':^4} {'Q0':^4}")
    print("-" * 52)


def _row(clock: int, decimal: int, ff: dict) -> None:
    print(
        f"  {clock:^6} | {decimal:^7} | "
        f"{ff['Q3']:^4} {ff['Q2']:^4} {ff['Q1']:^4} {ff['Q0']:^4}"
    )


def _footer() -> None:
    print("=" * 52)


def run_simulation(cycles: int = 1) -> None:
    counter = SynchronousCounter(start=COUNT_START, stop=COUNT_END)

    pulses_per_cycle = COUNT_END - COUNT_START + 1
    total_pulses = pulses_per_cycle * cycles

    _header()
    _row(0, counter.state, counter.get_flip_flop_outputs())

    for _ in range(total_pulses):
        counter.clock_pulse()
        _row(counter.clock_count, counter.state, counter.get_flip_flop_outputs())

    _footer()
    print(f"\n  Simulation complete — {counter.clock_count} clock pulse(s) applied.\n")


if __name__ == "__main__":
    run_simulation(cycles=1)
