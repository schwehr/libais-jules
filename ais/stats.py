#!/usr/bin/env python

import argparse
import datetime
import collections
import logging
import pprint
from typing import Any, Iterable, Counter as TypingCounter

from ais import nmea_queue

logger = logging.getLogger("libais")


class TrackRange:
    def __init__(self):
        self.min: float | None = None
        self.max: float | None = None

    def AddValues(self, *values: Any) -> None:
        valid_values = [v for v in values if v is not None]
        if not len(valid_values):
            raise ValueError("Must specify at least 1 value.")
        if self.min is None:
            self.min = min(valid_values)
            self.max = max(valid_values)
            return
        self.min = min(self.min, *valid_values)
        self.max = max(self.max, *valid_values)


class Stats:
    def __init__(self):
        self.counts: TypingCounter[str] = collections.Counter()
        self.queue = nmea_queue.NmeaQueue()
        self.time_range = TrackRange()
        self.time_delta_range = TrackRange()

    def AddFile(self, iterable: Iterable[str], filename: str | None = None) -> None:
        self.counts["files"] += 1

        for line in iterable:
            self.AddLine(line)

    def AddLine(self, line: str) -> None:
        self.counts["lines"] += 1
        self.queue.put(line)
        msg = self.queue.GetOrNone()
        if not msg:
            return

        self.counts[msg["line_type"]] += 1
        if "decoded" in msg:
            decoded = msg["decoded"]
            if "id" in decoded:
                self.counts["msg_VDM_%s" % decoded["id"]] += 1
            if "msg" in decoded:
                self.counts["msg_%s" % decoded["msg"]] += 1

        if "times" in msg:
            times = [t for t in msg["times"] if t is not None]
            if times:
                if self.time_range.min is None:
                    self.time_range.AddValues(*times)
                else:
                    time_delta = max(times) - self.time_range.max
                    self.time_delta_range.AddValues(time_delta)
                    self.time_range.AddValues(*times)

    def PrintSummary(self) -> None:
        pprint.pprint(self.counts)

        logger.info("time_range: [%s to %s]", self.time_range.min, self.time_range.max)

        if self.time_range.min is not None:
            logger.info("%s", datetime.datetime.utcfromtimestamp(self.time_range.min))
        if self.time_range.max is not None:
            logger.info("%s", datetime.datetime.utcfromtimestamp(self.time_range.max))

        logger.info(
            "time_delta_range: [%s to %s]",
            self.time_delta_range.min,
            self.time_delta_range.max,
        )


def main() -> None:
    logger.setLevel(logging.INFO)
    logger.info("in main")

    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", type=str, nargs="+", help="NMEA files")
    args = parser.parse_args()
    logger.info("args: %s", args)

    stats = Stats()
    for filename in args.filenames:
        stats.AddFile(open(filename), filename)

    stats.PrintSummary()
