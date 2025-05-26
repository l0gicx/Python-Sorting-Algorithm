# Sorting Algorithms Visualizer 🌀

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-orange.svg)
![Algorithms](https://img.shields.io/badge/17-Sorting_Algorithms-green.svg)

Interactive visualization of 17 sorting algorithms with Matplotlib animations.

## Table of Contents
- [Algorithms](#-featured-algorithms)
- [Quick Start](#-quick-start)


## 🌟 Featured Algorithms

### Comparison Sorts
| Algorithm        | Best Case | Worst Case | Stable |
|------------------|-----------|------------|--------|
| Bubble Sort      | O(n)      | O(n²)      | Yes    |
| Bitonic Sort     | O(log²n)  | O(log²n)   | No     |
| Comb Sort        | O(n logn) | O(n²)      | No     |
| Cocktail Shaker  | O(n)      | O(n²)      | Yes    |
| Gnome Sort       | O(n)      | O(n²)      | Yes    |
| Heap Sort        | O(n logn) | O(n logn)  | No     |
| Insertion Sort   | O(n)      | O(n²)      | Yes    |
| Merge Sort       | O(n logn) | O(n logn)  | Yes    |
| Quick Sort       | O(n logn) | O(n²)      | No     |
| Selection Sort   | O(n²)     | O(n²)      | No     |
| Shell Sort       | O(n logn) | O(n²)      | No     |
| Strand Sort      | O(n)      | O(n²)      | Yes    |

### Non-Comparison Sorts
| Algorithm        | Complexity | Stable |
|------------------|------------|--------|
| Counting Sort    | O(n+k)     | Yes    |
| Radix Sort       | O(nk)      | Yes    |
| Pigeonhole Sort  | O(n+k)     | Yes    |

### Esoteric Sorts
| Algorithm        | Notes                      |
|------------------|----------------------------|
| Bogo Sort        | O((n+1)!) - Random shuffles|
| Sleep Sort       | O(n + max_value) - Threads |

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/l0gicx/sorting-visualizer.git
cd sorting-visualizer

# Install dependencies
pip install -r requirements.txt

# Run any algorithm
python bitonic_sort.py
