\===============================
📦 Environment Setup Instructions
=================================

To install the required Python libraries, open your command prompt (CMD) and run the following command **after navigating to the folder where your `requirements.txt` file is located**.

Example:
cd pc\documents\image\_from\_pdf

Then run:
pip install -r requirements.txt

This will install the following Python packages:

* opencv-python
* matplotlib
* numpy
* Pillow
* pdf2image

NOTE: The above installation **does NOT include Poppler**, which is required by `pdf2image`.

Please download and install Poppler for Windows from:  [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)

After downloading:

1. Extract the ZIP file.
2. Copy the path to the `bin/` folder.
3. Add that path to your Windows environment `PATH` variable.

Now you're done setting up the environment!

---

## How to Use the Code

1. When you open the code, you'll find a section where you need to provide the **path to your PDF** file.
   → Just copy the path to your PDF and paste it there.

2. Next, provide the **path to the folder** where you want the extracted images to be saved.
   → Copy your destination folder path and paste it there.

3. That’s it! Just **run the code**, wait a few minutes, and the images will be ready in your output folder.

Enjoy your image extraction pipeline! 
