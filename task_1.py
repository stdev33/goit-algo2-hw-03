import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def create_logistics_network():
    G = nx.DiGraph()

    # Додавання вершин (термінали, склади, магазини)
    terminals = ["Термінал 1", "Термінал 2"]
    warehouses = ["Склад 1", "Склад 2", "Склад 3", "Склад 4"]
    stores = [f"Магазин {i}" for i in range(1, 15)]

    nodes = terminals + warehouses + stores
    G.add_nodes_from(nodes)

    # Додавання ребер (шляхів) та пропускної здатності
    capacities = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 1", "Склад 4", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10),
    ]

    for u, v, cap in capacities:
        G.add_edge(u, v, capacity=cap)

    return G


def compute_max_flow(G, source, sink):
    flow_value, flow_dict = nx.maximum_flow(
        G, source, sink, flow_func=nx.algorithms.flow.edmonds_karp
    )
    return flow_value, flow_dict


def display_results(flow_dict):
    results = []
    for src, targets in flow_dict.items():
        for dst, flow in targets.items():
            if flow > 0:
                results.append([src, dst, flow])

    df = pd.DataFrame(
        results, columns=["Термінал/Склад", "Магазин", "Фактичний потік (од.)"]
    )
    return df


if __name__ == "__main__":

    G = create_logistics_network()

    # Обчислення максимального потоку
    source = "Термінал 1"
    sink = "Магазин 14"  # Припустимо, що це найвіддаленіший магазин
    max_flow, flow_dict = compute_max_flow(G, source, sink)

    df_results = display_results(flow_dict)
    print(f"Максимальний потік: {max_flow}")
    print(df_results)

    # Візуалізація мережі
    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="black",
        node_size=3000,
        font_size=10,
    )
    edge_labels = {(u, v): G[u][v]["capacity"] for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Логістична мережа")
    plt.show()
