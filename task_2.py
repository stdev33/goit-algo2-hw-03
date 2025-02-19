import os
import csv
import timeit
from BTrees.OOBTree import OOBTree


current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "generated_items_data.csv")


def load_data_from_csv(file_path):
    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                {
                    "ID": int(row["ID"]),
                    "Name": row["Name"],
                    "Category": row["Category"],
                    "Price": float(row["Price"]),
                }
            )
    return data


def add_item_to_tree(dst_tree, it):
    dst_tree[it["ID"]] = it


def add_item_to_dict(dst_dictionary, it):
    dst_dictionary[it["ID"]] = it


def range_query_tree(target_tree, min_id, max_id, min_price, max_price):
    return [
        it
        for _, it in target_tree.items(min_id, max_id)
        if min_price <= it["Price"] <= max_price
    ]


def range_query_dict(target_dictionary, min_id, max_id, min_price, max_price):
    return [
        it
        for key, it in target_dictionary.items()
        if min_id <= key <= max_id and min_price <= it["Price"] <= max_price
    ]


if __name__ == "__main__":
    items_data = load_data_from_csv(csv_file_path)

    tree = OOBTree()
    dictionary = {}

    for item in items_data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_id = 10000
    max_id = 20000
    min_price = 100
    max_price = 300

    print(
        f"OOBTree in ID range [{min_id},{max_id}] and Price range [{min_price},{max_price}] found {len(range_query_tree(tree, min_id, max_id, min_price, max_price))} items"
    )
    print(
        f"Dict in ID range [{min_id},{max_id}] and Price range [{min_price},{max_price}] found {len(range_query_dict(dictionary, min_id, max_id, min_price, max_price))} items"
    )

    print(f"Total items in OOBTree: {len(tree)}")
    print(f"Total items in Dict: {len(dictionary)}")

    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_id, max_id, min_price, max_price), number=100
    )
    dict_time = timeit.timeit(
        lambda: range_query_dict(dictionary, min_id, max_id, min_price, max_price),
        number=100,
    )

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
