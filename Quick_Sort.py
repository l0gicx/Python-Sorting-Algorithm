import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def quick_sort_visual(arr):
    n = len(arr)
    
    # Set up modern dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    # Create bars with black color and white edges
    bar_rects = ax.bar(range(n), arr, 
                      color='black', 
                      edgecolor='white',
                      linewidth=1.5,
                      width=0.8)
    
    # Styling
    ax.set_xlim(0, n)
    ax.set_ylim(0, int(1.1 * max(arr)))
    ax.tick_params(axis='both', colors='white', labelsize=10)
    ax.set_title('Quick Sort Visualization', color='white', fontsize=14, pad=20)
    
    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    
    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)
    
    # Highlight color for pivot and partitioning
    pivot_color = '#ff4d4d'  # Bright red
    partition_color = '#ffa500'  # Orange
    
    def update(frame):
        # Reset all bars to black
        for rect in bar_rects:
            rect.set_color('black')
        
        # Highlight the pivot
        if 'pivot_index' in frame:
            pivot_index = frame['pivot_index']
            bar_rects[pivot_index].set_color(pivot_color)
        
        # Highlight the partitioned elements
        if 'partition_indices' in frame:
            for index in frame['partition_indices']:
                bar_rects[index].set_color(partition_color)
        
        # Update heights
        for rect, val in zip(bar_rects, frame['array']):
            rect.set_height(val)
        
        # Update status text
        status_text.set_text(f"Pivot Index: {frame['pivot_index']}")
        
        return list(bar_rects) + [status_text]  # Convert bar_rects to a list
    
    def quick_sort_gen(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            yield {'array': arr.copy(), 'pivot_index': pivot_index, 'partition_indices': list(range(low, high + 1))}
            yield from quick_sort_gen(arr, low, pivot_index - 1)
            yield from quick_sort_gen(arr, pivot_index + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]  # Choosing the last element as pivot
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    anim = animation.FuncAnimation(
        fig, update,
        frames=quick_sort_gen(arr, 0, n - 1),
        interval=500,  # Adjust for speed of animation
        blit=True,
        repeat=False
    )
    
    plt.tight_layout()
    plt.show()

# Generate random data
np.random.seed(42)
arr = np.random.randint(1, 100, 20)

# Run visualization
quick_sort_visual(arr)