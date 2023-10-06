import csv
import datetime
import sys

import numpy


N_FILES = 10_000
N_ROWS_PER_FILE = 1_000

DATE_LAST = datetime.date(2022, 12, 31)


def generate_client_id() -> int:
    return int(numpy.random.default_rng().exponential(scale=100))


def generate_store_id() -> int:
    return int(numpy.random.default_rng().uniform(low=1, high=10_000))


csv_writer_field_names = ["invoice_id", "client_id", "store_id", "chain_id", "issue_date"]

for file_index in range(N_FILES):
    sys.stderr.write(f"Generating file {file_index}/{N_FILES}...\n")

    with open(f"../data/invoice-{file_index}.csv", "w", newline="") as file_handle:
        csv_writer = csv.DictWriter(file_handle, fieldnames=csv_writer_field_names)
        csv_writer.writeheader()

        for row_index in range(N_ROWS_PER_FILE):
            invoice_id = file_index * N_ROWS_PER_FILE + row_index
            client_id = generate_client_id()
            store_id = generate_store_id()
            chain_id = file_index

            issue_date = DATE_LAST - datetime.timedelta(days=row_index)

            csv_writer.writerow({
                "invoice_id": invoice_id,
                "client_id": client_id,
                "store_id": store_id,
                "chain_id": chain_id,
                "issue_date": issue_date
            })
