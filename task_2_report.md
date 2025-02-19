# 📊 Performance Analysis: OOBTree vs Dict for Range Queries

## **Introduction**
This project compares the performance of two data structures—**OOBTree** and **Dict**—when performing **range queries** on a dataset of 100,000 items.  
The goal is to determine which structure is more efficient for retrieving items within a given range of **ID** and **Price**.

## **Implementation**
1. **Data Storage**:
   - **OOBTree**: Uses **ID** as the key and stores item attributes as values.
   - **Dict**: Uses **ID** as the key and stores item attributes as values.

2. **Range Query Functionality**:
   - **OOBTree**: Uses `items(min_id, max_id)` to quickly retrieve the required range and then filters by `Price`.
   - **Dict**: Uses **linear search**, iterating over all items to check if they match both the `ID` and `Price` criteria.

3. **Performance Measurement**:
   - We execute **100 range queries** and record the total execution time using `timeit`.

## **Results**
 - Total range_query time for OOBTree: 0.136087 seconds
 - Total range_query time for Dict: 0.501977 seconds

| Data Structure | Execution Time (100 Queries) | Complexity |
|---------------|----------------------------|------------|
| **OOBTree**   | **0.136 s**                 | `O(log n + k)` |
| **Dict**      | **0.502 s**                 | `O(n)` |

## **Analysis**
1. **Both OOBTree and Dict return the correct number of results (3981 items), ensuring correctness.**
2. **OOBTree is significantly faster (≈3.7x) than Dict for range queries**, as it efficiently retrieves items using a **balanced tree structure**.
3. **Dict is slower because it performs a full scan (`O(n)`)**, whereas **OOBTree operates in `O(log n + k)`, making it scalable for large datasets**.
4. **The results align with theoretical expectations**, confirming that **OOBTree is the better choice for efficient range queries**.

## **Conclusion**
- **OOBTree is the preferred data structure for performing range queries efficiently, especially on large datasets**.
- **Dict remains useful for general-purpose operations but is significantly slower for range-based retrieval**.

**This study confirms that OOBTree outperforms Dict in range queries, demonstrating its suitability for structured data access.**