import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import threading

def sleep_sort(arr):
    frames = []
    threads = []

    def sleep_and_add(num):
        time.sleep(num)  # Sleep for the value of the number
        frames.append(num)  # Capture the number after sleeping

    # Create a thread for each number in the array
    for num in arr:
        thread = threading.Thread(target=sleep_and_add, args=(num,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return frames

def sleep_sort_visual(arr):
    frames = sleep_sort(arr)

    # Set up modern dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')
    ax.set_facecolor('#1a1a1a')

    # Create bars with black color and white edges
    bar_rects = ax.bar(range(len(arr)), [0] * len(arr), 
                      color='black', 
                      edgecolor='white',
                      linewidth=1.5,
                      width=0.8)

    # Styling
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    ax.tick_params(axis='both', colors='white', labelsize=10)
    ax.set_title('Sleep Sort Visualization', color='white', fontsize=14, pad=20)

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
        for rect, val in zip(bar_rects, range(len(frame))):
            rect.set_height(frame[val])

        # Update status text
        status_text.set_text(f"Current Array: {frame}")

        return list(bar_rects) + [status_text]  # Convert bar_rects to a list

    # Create the animation
    anim = animation.FuncAnimation(
        fig, update,
        frames=[frames[:i+1] for i in range(len(frames))],
        interval=500,  # Adjust for speed of animation
        blit=True,
        repeat=False
    )

    plt.tight_layout()
    plt.show()

# Generate random data
np.random.seed(42)
arr = np.random.randint(1, 10, 10)  # Using a small range suitable for Sleep Sort

# Run visualization
sleep_sort_visual(arr)