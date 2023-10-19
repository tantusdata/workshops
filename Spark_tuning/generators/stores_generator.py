import random
import string

import numpy

from commons import CSVBucketingWriter

N_ROWS_PER_FILE = 10_000_000
N_ROWS_TOTAL = 100_000


def generate_name() -> str:
    return "".join(random.sample(string.ascii_lowercase, 8))


def generate_location_lat() -> float:
    return float(numpy.random.default_rng().uniform(low=-90, high=90))


def generate_location_long() -> float:
    return float(numpy.random.default_rng().uniform(low=-180, high=180))


COLUMNS = ["store_id", "name", "location_lat", "location_long"]

if __name__ == "__main__":
    final_buckets = CSVBucketingWriter(N_ROWS_PER_FILE, "../data/stores/stores", COLUMNS)

    for row_index in range(N_ROWS_TOTAL):
        row = {
            "store_id": row_index,
            "name": generate_name(),
            "location_lat": generate_location_lat(),
            "location_long": generate_location_long()
        }

        final_buckets.write(row)

    final_buckets.flush()
