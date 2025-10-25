from moviepy.editor import ColorClip, CompositeVideoClip, TextClip, VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings


change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

def generate_video(video_path, text_content, output_path):
    """
    Combines a video with a string of text displayed at the bottom.

    Args:
        video_path (str): The path to the input video file.
        text_content (str): Path to the text file.
        output_path (str): The path to save the output video.
    """
    try:
        video = VideoFileClip("inputClips/" + video_path).resize(.6)

        # Create a background color clip with the same dimensions and duration as the video
        background_clip = ColorClip(size=(VideoFileClip(video_path).w, VideoFileClip(video_path).h), color=(255,255,0), duration=video.duration)
        # Read text content from the provided file path
        with open("inputText/" + text_content, 'r') as f:
            text_lines = f.readlines()
                
        # Join lines to form the full text, stripping newlines
        full_text = "".join(text_lines).strip()

        txt_clip = TextClip(full_text, fontsize=25, color='black', font='Helvetica-Bold', bg_color='yellow', 
                            size=(background_clip.w, None), method='caption')

        # Set the duration of the text clip to match the video
        txt_clip = txt_clip.set_duration(video.duration)
        

        # Create the title text clip
        title_clip = TextClip("Mcat Question Challenge", fontsize=30, color='black',
                              font='Helvetica-Bold', bg_color="yellow",
                              size=(background_clip.w, None))
        title_clip = title_clip.set_duration(video.duration)
        title_clip = title_clip.set_position(('center', 'top'))

        # Position the video on the background, below the title
        video = video.set_position(("center", title_clip.h))

        # Position the text clip at the bottom of the video
        txt_clip = txt_clip.set_position(('center', video.h))

        # Composite all elements onto the background
        final_clip = CompositeVideoClip([background_clip, title_clip, video, txt_clip])

        # Write the output video file
        final_clip.write_videofile(output_path, codec="libx264", fps=video.fps)

        print(f"Video generated successfully: {"outputs/" + output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_video.mp4' with the actual path to your video file
    # Replace 'Your text goes here!' with the text you want to display
    # generate_video("your_video.mp4", "Your text goes here!", "output_with_text.mp4")
    print("Please provide a video path and text content to generate a short clip.")
    generate_video(input("Video path: "), input("Text content: "), input("Output path: "))