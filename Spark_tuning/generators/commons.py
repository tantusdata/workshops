from __future__ import annotations

import csv
import datetime
import io
import os
import sys

DATE_LAST = datetime.date(2022, 12, 31)


class CSVBucketingWriter:
    def __init__(self, bucket_limit: int, file_prefix: str, columns: list[str]):
        self.bucket_limit = bucket_limit
        self.file_prefix = file_prefix
        self.columns = columns

        self.bucket_current = -1
        self.bucket_written = -1
        self._file_handler: io.TextIOWrapper | None = None
        self.writer: csv.DictWriter | None = None

    def flush(self):
        if self._file_handler is not None:
            self._file_handler.close()

        self.writer = None
        self._file_handler = None

    def write(self, row):
        if (self._file_handler is None) or self.bucket_written >= self.bucket_limit:
            self._create_bucket()

        self.bucket_written += 1
        self.writer.writerow(row)

    def _create_bucket(self):
        self.bucket_current += 1
        self.bucket_written = 0

        next_file_name = f"{self.file_prefix}-{self.bucket_current}.csv"

        if self._file_handler is not None:
            self.flush()
        else:
            os.makedirs(os.path.dirname(next_file_name), exist_ok=True)

        sys.stderr.write(f"Generating file {next_file_name}...\n")

        self._file_handler = open(next_file_name,  "w", newline="")
        self.writer = csv.DictWriter(self._file_handler, fieldnames=self.columns)
        self.writer.writeheader()
