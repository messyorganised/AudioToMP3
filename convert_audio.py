import os
import sys
import subprocess
import static_ffmpeg
import concurrent.futures
import time

# Initialize static_ffmpeg to ensure binaries are available
static_ffmpeg.add_paths()

def convert_single_file(source_path, dest_path):
    """
    Converts a single audio file to MP3 using ffmpeg with 320k CBR.
    Returns (success, message).
    """
    # ffmpeg -i input.wav -b:a 320k -y output.mp3
    # User requested to maintain bitrate as much as possible. 
    # MP3 max is 320k. We use CBR 320k as it's the industry standard for high-quality MP3s.
    cmd = [
        "ffmpeg",
        "-i", source_path,
        "-b:a", "320k", 
        "-y", # Overwrite output files without asking
        "-v", "error", # Suppress output unless error
        dest_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True, f"Converted: {os.path.basename(source_path)}"
        else:
            return False, f"FAILED: {os.path.basename(source_path)} - {result.stderr}"
    except Exception as e:
        return False, f"ERROR: {os.path.basename(source_path)} - {e}"

def convert_audio_batch(source_dir, dest_dir):
    """
    Converts all audio files in source_dir to MP3 format in dest_dir using parallel processing.
    """
    if not os.path.exists(source_dir):
        # Create source dir if it doesn't exist so user knows where to put files
        os.makedirs(source_dir)
        print(f"Created source directory: {source_dir}")
        print(f"Please put your audio files in '{source_dir}' and run the script again.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")

    supported_formats = ('.wav', '.flac', '.ogg', '.m4a', '.wma', '.aiff')
    
    files = [f for f in os.listdir(source_dir) if f.lower().endswith(supported_formats)]
    
    if not files:
        print(f"No supported audio files found in '{source_dir}'.")
        return

    print(f"Found {len(files)} files to convert.")
    
    start_time = time.time()
    
    # Use ThreadPoolExecutor for parallel processing
    max_workers = os.cpu_count() or 4
    print(f"Starting conversion with {max_workers} parallel workers...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {}
        for filename in files:
            source_path = os.path.join(source_dir, filename)
            name_without_ext = os.path.splitext(filename)[0]
            dest_filename = f"{name_without_ext}.mp3"
            dest_path = os.path.join(dest_dir, dest_filename)
            
            future = executor.submit(convert_single_file, source_path, dest_path)
            future_to_file[future] = filename

        for future in concurrent.futures.as_completed(future_to_file):
            success, message = future.result()
            print(message)

    elapsed_time = time.time() - start_time
    print(f"Batch conversion completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    # Define paths relative to the script location (Portable Mode)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Look for folders in the same directory as the script
    source_directory = os.path.join(script_dir, "Original")
    destination_directory = os.path.join(script_dir, "Converted")

    print("Starting Batch Audio Conversion...")
    print(f"Source: {source_directory}")
    print(f"Destination: {destination_directory}")
    
    convert_audio_batch(source_directory, destination_directory)
    input("Press Enter to exit...") # Keep window open
