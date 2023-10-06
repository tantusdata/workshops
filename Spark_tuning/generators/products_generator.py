import csv
import sys

import numpy


N_FILES = 1
N_ROWS_PER_FILE = 1_000


def generate_price() -> float:
    return int(numpy.random.default_rng().uniform(low=1, high=10_000)) / 100.0


def generate_unit() -> str:
    return str(numpy.random.default_rng().choice(["kg", "m", "m2", "m3", ""], 1)[0])


csv_writer_field_names = ["product_id", "price", "unit"]


for file_index in range(N_FILES):
    sys.stderr.write(f"Generating file {file_index}/{N_FILES}...\n")

    with open(f"../data/products-{file_index}.csv", "w", newline="") as file_handle:
        csv_writer = csv.DictWriter(file_handle, fieldnames=csv_writer_field_names)
        csv_writer.writeheader()

        for row_index in range(N_ROWS_PER_FILE):
            product_id = file_index * N_ROWS_PER_FILE + row_index
            price = generate_price()
            unit = generate_unit()

            csv_writer.writerow({
                "product_id": product_id,
                "price": price,
                "unit": unit
            })

