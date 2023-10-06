import csv
import sys

import numpy

import invoice_generator
import products_generator

N_FILES = 1_000
N_INVOICES_PER_FILE = invoice_generator.N_TOTAL // N_FILES


def generate_product_id() -> int:
    return int(numpy.random.default_rng().uniform(low=0, high=products_generator.N_TOTAL))


def generate_amount() -> int:
    return int(numpy.random.default_rng().uniform(low=0, high=10))


csv_writer_field_names = ["invoice_id", "invoice_item_index", "product_id", "amount"]

if __name__ == "__main__":
    for file_index in range(N_FILES):
        sys.stderr.write(f"Generating file {file_index}/{N_FILES}...\n")

        with open(f"../data/invoice-items-{file_index}.csv", "w", newline="") as file_handle:
            csv_writer = csv.DictWriter(file_handle, fieldnames=csv_writer_field_names)
            csv_writer.writeheader()

            for row_index in range(N_INVOICES_PER_FILE):
                invoice_id = file_index * N_INVOICES_PER_FILE + row_index
                items_for_invoice = int(numpy.random.default_rng().uniform(low=3, high=7))

                for invoice_item_index in range(1, 1 + items_for_invoice):
                    product_id = generate_product_id()
                    amount = generate_amount()

                    csv_writer.writerow({
                        "invoice_id": invoice_id,
                        "invoice_item_index": invoice_item_index,
                        "product_id": product_id,
                        "amount": amount
                    })

