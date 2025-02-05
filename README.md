# Media File Transcriptor
This repository contains the program for transcripting any kind of mp3, mp4, mkv or related files of multimedia extensions

## Overview
This Python script processes a directory of media files by:


I). Scanning a folder and its respective subfolders for audio and video files.

II). Transcribing the detected media files using OpenAI's Whisper model.

III). Saving the transcriptions in both .txt and .json formats.

## Prerequisites

- Python 3.8 or higher versions

- OpenAI's Whisper( for Speech-to-Text Conversion )

- FFmpeg(Multimedia framework used to handle audio, video and image processing. Required for OpenAI's Whisper model)

- tqdm(for the progress bar that indicates the status of the process)

- argparse(for command line arguement)

- json(to save the output in json format)

- os & pathlib (for file handling and directory creation)

## Working of Code

- function "find_media_files" : A list of popular media file extensions are declared inside the function (for e.g: .mp3, .mp4, .wav, .mkv, .flac).
                                This function recursively scans the input directory for media files with the specified extensions. For traversing
                                through subdirectories of the input directory, os.walk() method is used.

- function "transcribe_media" : This function uses the Tiny(smallest) model of OpenAI's Whisper Speech-to-Text conversion model to transcribe audio/video files.
                                After transcribing it returns the transcribed text.

- function "save_transcription" : This function saves the returned text in .txt and .json formats.

- function "main" : The main function initializes the parser element and uses it to take command line inputs from the user. It then loads the Whisper model and runs the
                    execution on the provided input folder and saves the input in the provided output folder.



