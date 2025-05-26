import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def bubble_sort_visual(arr):
    n = len(arr)
    
    # Set up modern dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')  # Increased width to 12
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
    ax.set_title('Bubble Sort Visualization', color='white', fontsize=14, pad=20)
    
    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    
    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)
    
    # Highlight color for swaps
    highlight_color = '#ff4d4d'  # Bright red
    
    def update(frame):
        # Reset all bars to black
        for rect in bar_rects:
            rect.set_color('black')
        
        # Highlight compared elements
        if 'compare' in frame:
            i, j = frame['compare']
            bar_rects[i].set_color(highlight_color)
            bar_rects[j].set_color(highlight_color)
        
        # Update heights
        for rect, val in zip(bar_rects, frame['array']):
            rect.set_height(val)
        
        # Update status text
        status_text.set_text(f"Iterations: {frame['iteration']}\n"
                            f"Comparisons: {frame['comparisons']}\n"
                            f"Swaps: {frame['swaps']}")
        
        return list(bar_rects) + [status_text]  # Convert bar_rects to a list
    
    def bubble_sort_gen():
        swaps = 0
        comparisons = 0
        iteration = 0
        
        for i in range(n):
            swapped = False
            iteration += 1
            for j in range(0, n-i-1):
                comparisons += 1
                yield {'array': arr.copy(), 
                      'compare': (j, j+1), 
                      'iteration': iteration,
                      'comparisons': comparisons,
                      'swaps': swaps}
                
                if arr[j] > arr[j+1]:
                    swaps += 1
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    yield {'array': arr.copy(), 
                          'compare': (j, j+1), 
                          'iteration': iteration,
                          'comparisons': comparisons,
                          'swaps': swaps}
            
            if not swapped:
                break
    
    anim = animation.FuncAnimation(
        fig, update,
        frames=bubble_sort_gen,
        interval=50,  # Smoother animation
        blit=True,
        repeat=False
    )
    
    plt.tight_layout()
    plt.show()

# Generate random data
np.random.seed(42)
arr = np.random.randint(1, 100, 20)

# Run visualization
bubble_sort_visual(arr)