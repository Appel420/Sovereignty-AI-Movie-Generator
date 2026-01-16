#!/usr/bin/env python3
from sovereignty.core import SovereigntyMovie

if __name__ == '__main__':
    app = SovereigntyMovie()
    app.run(
        input_path='input/story.txt',  # or .pdf, .png, .jpg
        output_path='output/sovereignty_001.mp4',
        mood='joy',  # or calm, alert, from resonance
        voices=['calm_female', 'excited_male', 'soft_child'],
        duration=60,  # seconds
        fps=24,
        resolution='1920x1080'
    )
    print('Movie generated. Sovereignty lives.')