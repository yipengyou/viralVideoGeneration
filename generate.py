import moviepy.editor as mp
from moviepy.editor import ColorClip, CompositeVideoClip, TextClip, VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

def generate_video(video_path, text_content, output_path="output.mp4"):
    """
    Combines a video with a string of text displayed at the bottom.

    Args:
        video_path (str): The path to the input video file.
        text_content (str): The text string to display.
        output_path (str): The path to save the output video.
    """
    try:
        video = VideoFileClip(video_path)
        print(video.duration)
        # Create a TextClip for the text
        txt_clip = TextClip(text_content, fontsize=50, color='white',
                            font='Arial', bg_color='black',
                            size=(video.w, None)) # Width of the video, auto height

        # Set the duration of the text clip to match the video
        txt_clip = txt_clip.set_duration(video.duration)

        # Position the text clip at the bottom of the video
        # (x, y) = ('center', video.h - txt_clip.h - 20)  # 20 pixels from the bottom
        txt_clip = txt_clip.set_position(('center', 'bottom'))

        # Composite the video and the text clip
        final_clip = CompositeVideoClip([video, txt_clip])

        # Write the output video file
        final_clip.write_videofile(output_path, codec="libx264", fps=video.fps)

        print(f"Video generated successfully: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_video.mp4' with the actual path to your video file
    # Replace 'Your text goes here!' with the text you want to display
    # generate_video("your_video.mp4", "Your text goes here!", "output_with_text.mp4")
    print("Please provide a video path and text content to generate a short clip.")
    generate_video(input("Video path: "), input("Text content: "))