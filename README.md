# Audio Conversion Tool

This tool converts audio files (WAV, FLAC, etc.) to high-quality MP3s (320kbps CBR) for compatibility with older DJ hardware.

## Quick Start

### Windows
1.  Double-click **`run_converter.bat`**.

### Mac
1.  Right-click **`run_converter.command`** and select **Open**.
2.  If it says it's from an unidentified developer, click **Open** again.
    *   *Note: If it doesn't run, you might need to open Terminal, type `chmod +x ` (with a space), drag the file into the window, and hit Enter.*

The script will automatically install necessary components and create two folders:
*   `Original`: Place your audio files here.
*   `Converted`: Your MP3s will appear here.

After the first run, put your music in the `Original` folder and run the script again to convert them.

## Requirements

*   **Python**: You need **Python 3.8 or newer** installed on your computer.
    *   [Download Python Here](https://www.python.org/downloads/)
    *   **IMPORTANT**: During installation, check the box that says **"Add Python to PATH"**.

## Features

*   **High Quality**: Converts to 320kbps MP3 (Constant Bit Rate).
*   **Fast**: Uses all available processor cores to convert multiple files at once.
*   **Simple**: Just run the batch file.

## Troubleshooting

*   **"Python is not recognized..."**: This means Python is not installed or not in your PATH. Reinstall Python and make sure to check "Add Python to PATH".
