import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def selection_sort_visual(arr):
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
    ax.set_title('Selection Sort Visualization', color='white', fontsize=14, pad=20)
    
    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    
    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)
    
    # Highlight color for current minimum
    highlight_color = '#ff4d4d'  # Bright red
    
    def update(frame):
        # Reset all bars to black
        for rect in bar_rects:
            rect.set_color('black')
        
        # Highlight the current minimum element
        if 'min_index' in frame:
            min_index = frame['min_index']
            bar_rects[min_index].set_color(highlight_color)
        
        # Update heights
        for rect, val in zip(bar_rects, frame['array']):
            rect.set_height(val)
        
        # Update status text
        status_text.set_text(f"Current Minimum Index: {frame['min_index']}")
        
        return list(bar_rects) + [status_text]  # Convert bar_rects to a list
    
    def selection_sort_gen():
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            
            # Swap the found minimum element with the first element
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield {'array': arr.copy(), 'min_index': min_index}
    
    anim = animation.FuncAnimation(
        fig, update,
        frames=selection_sort_gen,
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
selection_sort_visual(arr)