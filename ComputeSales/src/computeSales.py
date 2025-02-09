import json
import sys
import os
import time


def load_catalogue(catalogue_file):
    try:
        print(f"Loading catalogue from: {os.path.abspath(catalogue_file)}")
        with open(catalogue_file, 'r') as file:
            catalogue = json.load(file)
            # Validate that all prices are numbers
            for product, price in catalogue.items():
                if not isinstance(price, (int, float)):
                    raise ValueError(
                        f"Invalid price for product {product}: {price}"
                    )
            return catalogue
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading catalogue: {e}")
        return {}


def load_sales(sales_file):
    try:
        print(f"Loading sales from: {os.path.abspath(sales_file)}")
        with open(sales_file, 'r') as file:
            sales = json.load(file)
            # Validate that all quantities are numbers
            for sale in sales:
                if not isinstance(sale['quantity'], (int, float)):
                    raise ValueError(
                        f"Invalid quantity for product {sale['product']}: {sale['quantity']}"
                    )
            return sales
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading sales: {e}")
        return []


def compute_sales(catalogue, sales):
    total_sales = 0
    sales_details = []
    for sale in sales:
        try:
            product_id = sale['product']
            quantity = sale['quantity']
            if product_id in catalogue:
                if not isinstance(quantity, (int, float)):
                    raise ValueError(
                        f"Invalid quantity for product {product_id}: {quantity}"
                    )
                item_total = catalogue[product_id] * quantity
                total_sales += item_total
                sales_details.append({
                    'product': product_id,
                    'quantity': quantity,
                    'unit_price': catalogue[product_id],
                    'total_price': item_total
                })
        except KeyError as e:
            print(f"Error processing sale: {e}")
        except TypeError as e:
            print(f"Invalid data type encountered: {e}")
        except ValueError as e:
            print(f"Error in sale data: {e}")
    return total_sales, sales_details


def process_sales_data(catalogue, sales_records):
    sales_summary = {}
    for record in sales_records:
        product = record['product']
        quantity = record['quantity']
        if product in catalogue:
            if product not in sales_summary:
                sales_summary[product] = 0
            sales_summary[product] += catalogue[product] * quantity
    return sales_summary


def main():
    start_time = time.time()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_catalogue_file = os.path.join(script_dir, '..', 'data', 'catalogue.json')
    default_sales_file = os.path.join(script_dir, '..', 'data', 'sales_records.json')
    sales_results_file = os.path.join(script_dir, '..', 'data', 'SalesResults.txt')

    if len(sys.argv) == 1:
        use_defaults = input("Do you want to use the default paths? (yes/no): ").strip().lower()
        if use_defaults == 'yes':
            catalogue_file = default_catalogue_file
            sales_file = default_sales_file
        else:
            catalogue_file = input("Enter the path for the catalogue file: ").strip()
            sales_file = input("Enter the path for the sales file: ").strip()
    elif len(sys.argv) == 3:
        catalogue_file = sys.argv[1]
        sales_file = sys.argv[2]
    else:
        print("Usage: python computeSales.py <catalogue_file.json> <sales_file.json>")
        sys.exit(1)

    catalogue = load_catalogue(catalogue_file)
    if not catalogue:
        print("Failed to load catalogue. Exiting.")
        sys.exit(1)

    sales = load_sales(sales_file)
    if not sales:
        print("Failed to load sales. Exiting.")
        sys.exit(1)

    total, sales_details = compute_sales(catalogue, sales)

    result_message = (
        "Sales Summary Report\n"
        "====================\n"
        f"Total Sales: ${total:.2f}\n\n"
        "Details:\n"
    )
    for detail in sales_details:
        result_message += (
            f"Product: {detail['product']}\n"
            f"  Quantity: {detail['quantity']}\n"
            f"  Unit Price: ${detail['unit_price']:.2f}\n"
            f"  Total Price: ${detail['total_price']:.2f}\n\n"
        )

    end_time = time.time()
    elapsed_time = end_time - start_time
    result_message += f"Time elapsed: {elapsed_time:.2f} seconds\n"
    print(result_message)

    # Write the result to SalesResults.txt in the data folder
    with open(sales_results_file, 'w') as result_file:
        result_file.write(result_message)


if __name__ == "__main__":
    main()
