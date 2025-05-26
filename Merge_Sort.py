import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def merge_sort_visual(arr):
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
    ax.set_title('Merge Sort Visualization', color='white', fontsize=14, pad=20)
    
    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    
    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)
    
    # Highlight color for merging
    highlight_color = '#ff4d4d'  # Bright red
    
    def update(frame):
        # Reset all bars to black
        for rect in bar_rects:
            rect.set_color('black')
        
        # Highlight the current merging elements
        if 'merge_indices' in frame:
            for index in frame['merge_indices']:
                bar_rects[index].set_color(highlight_color)
        
        # Update heights
        for rect, val in zip(bar_rects, frame['array']):
            rect.set_height(val)
        
        # Update status text
        status_text.set_text(f"Merging: {frame['merge_indices']}")
        
        return list(bar_rects) + [status_text]  # Convert bar_rects to a list
    
    def merge_sort_gen(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]        # Dividing the elements into 2 halves
            R = arr[mid:]

            # Recursive call on each half
            yield from merge_sort_gen(L)
            yield from merge_sort_gen(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                yield {'array': arr.copy(), 'merge_indices': list(range(len(arr)))}
            
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                yield {'array': arr.copy(), 'merge_indices': list(range(len(arr)))}
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                yield {'array': arr.copy(), 'merge_indices': list(range(len(arr)))}
    
    anim = animation.FuncAnimation(
        fig, update,
        frames=merge_sort_gen(arr),
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
merge_sort_visual(arr)