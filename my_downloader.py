
# Import YouTube class from pytube library.
from pytube import YouTube


# Create a function to do the downloading.
def download_youtube_video(url, output_path):
    # Put the function details in a try...except block to capture errors, if any.
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the first available video format with the highest resolution
        video = youtube.streams.get_highest_resolution()

        # Download the video to the specified output path
        video.download(output_path)

        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Usage Example.

# Define a variable for the video url
video_url = "https://www.youtube.com/watch?v=jsaW4l28P3Y"  # Replace with your YouTube video URL

# Define a variable for the output directory
output_directory = "This PC/Downloads"  # Replace with your desired output directory
# If the output directory does not exist, Python will create one for you.

# Call the function with the arguments.
download_youtube_video(video_url, output_directory)
