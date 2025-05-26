import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def insertion_sort_visual(arr):
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
    ax.set_title('Insertion Sort Visualization', color='white', fontsize=14, pad=20)
    
    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    
    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)
    
    # Highlight color for current element
    highlight_color = '#ff4d4d'  # Bright red
    
    def update(frame):
        # Reset all bars to black
        for rect in bar_rects:
            rect.set_color('black')
        
        # Highlight the current element being inserted
        if 'current' in frame:
            current_index = frame['current']
            bar_rects[current_index].set_color(highlight_color)
        
        # Update heights
        for rect, val in zip(bar_rects, frame['array']):
            rect.set_height(val)
        
        # Update status text
        status_text.set_text(f"Current Index: {frame['current']}")
        
        return list(bar_rects) + [status_text]  # Convert bar_rects to a list
    
    def insertion_sort_gen():
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            # Move elements of arr[0..i-1] that are greater than key
            # to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                yield {'array': arr.copy(), 'current': j + 1}
                j -= 1
            
            arr[j + 1] = key
            yield {'array': arr.copy(), 'current': i}
    
    anim = animation.FuncAnimation(
        fig, update,
        frames=insertion_sort_gen,
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
insertion_sort_visual(arr)