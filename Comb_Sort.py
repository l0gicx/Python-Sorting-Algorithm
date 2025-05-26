import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def comb_sort_visual(arr):
    n = len(arr)
    frames = []
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        # Update the gap for the next comb
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        sorted = True

        for i in range(n - gap):
            # Capture the current state of the array for visualization
            frames.append(arr.copy())
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

        # Capture the state after each pass
        frames.append(arr.copy())

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
    ax.set_title('Comb Sort Visualization', color='white', fontsize=14, pad=20)

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
arr = np.random.randint(1, 100, 20)  # Using a range suitable for Comb Sort

# Run visualization
comb_sort_visual(arr)