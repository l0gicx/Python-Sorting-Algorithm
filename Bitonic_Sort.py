import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def bitonic_merge(arr, low, cnt, frames):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if arr[i] > arr[i + k]:
                arr[i], arr[i + k] = arr[i + k], arr[i]
        # Capture the current state of the array for visualization
        frames.append(arr.copy())
        bitonic_merge(arr, low, k, frames)
        bitonic_merge(arr, low + k, k, frames)

def bitonic_sort(arr, low, cnt, frames, up):
    if cnt > 1:
        k = cnt // 2
        # Sort in ascending order if up is true, descending otherwise
        bitonic_sort(arr, low, k, frames, 1)  # Sort first half in ascending order
        bitonic_sort(arr, low + k, k, frames, 0)  # Sort second half in descending order
        bitonic_merge(arr, low, cnt, frames)  # Merge the whole sequence

def bitonic_sort_visual(arr):
    frames = []
    n = len(arr)
    bitonic_sort(arr, 0, n, frames, 1)  # Start the bitonic sort

    # Set up modern dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')
    ax.set_facecolor('#1a1a1a')

    # Create bars with black color and white edges
    bar_rects = ax.bar(range(len(arr)), arr, 
                      color='black', 
                      edgecolor='white',
                      linewidth=1.5,
                      width=0.8)

    # Styling
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    ax.tick_params(axis='both', colors='white', labelsize=10)
    ax.set_title('Bitonic Sort Visualization', color='white', fontsize=14, pad=20)

    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')

    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)

    # Animation update function
    def update(frame):
        # Update heights
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)

        # Update status text
        status_text.set_text(f"Current Array: {frame}")

        return list(bar_rects) + [status_text]  # Convert bar_rects to a list

    # Create the animation
    anim = animation.FuncAnimation(
        fig, update,
        frames=frames,
        interval=500,  # Adjust for speed of animation
        blit=True,
        repeat=False
    )

    plt.tight_layout()
    plt.show()

# Generate random data
np.random.seed(42)
arr = np.random.randint(1, 100, 20)  # Using a range suitable for Bitonic Sort

# Run visualization
bitonic_sort_visual(arr)