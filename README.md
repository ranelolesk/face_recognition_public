## Face Recognition
Identifies a face from image(s), looks for similar faces in a set of images, separates the image files that match.

## Motivation
Needed a way to separate the pictures of a specific person in a set of tens of thousands of restored files, fast.

## Tech/framework used

<b>Built with</b>
- Python 3.7
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [tqdm](https://github.com/tqdm/tqdm)
- [opencv](https://github.com/opencv/opencv)

## Installation

- A development environment (Windows, Linux) with:
    - Python 3.3+ or 2.7
    - face_recognition
    - tqdm
    - OpenCV
    - Let you IDE do the work!

## How to use?

1) Take an image(s) of you (or the person you are looking for) and move to test_images/face_me. These images are used to reference against the dataset.
2) Put your dataset of images into test_images/face_dataset. This set of images is used for looking into matching faces.
3) Run "python executable" + "main.py"

## Credits

- [Konstantinos Mavrodis](https://dev.to/kmavrodis/going-through-10000-pictures-in-30-seconds-ad8)


## License

MIT License

Copyright (c) [2019] [Ranel Olesk]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.