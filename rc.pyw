import cv2
import time

def record_webcam(duration_seconds=10, output_filename="output.mp4", fps=20.0):
    """
    Records video from the webcam for a specified duration.
    
    :param duration_seconds: Number of seconds to record.
    :param output_filename: Path/name of the destination file.
    :param fps: Frames per second for the output video.
    """
    # 0 is usually the default built-in webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Retrieve camera resolution settings
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    # 'mp4v' works well for cross-platform .mp4 output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

    print(f"Recording started... Will capture for {duration_seconds} seconds.")
    start_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Write frame to file
            out.write(frame)

            # Display recording preview window (optional)
            cv2.imshow('Recording... (Press Q to stop early)', frame)

            # Check if duration limit reached
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration_seconds:
                print("Recording finished.")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Recording stopped early by user.")
                break

    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print(f"Saved video to: {output_filename}")

if __name__ == "__main__":
    record_webcam(duration_seconds=60, output_filename="rec.mp4")
