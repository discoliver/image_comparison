# Image Comparison

## Table of contents  

* [About the Program](#About-the-Program)
* [Getting Started](#Getting Started)
* [How to Use the Program](#How-to-Use-the-Program)
* [Solution Approach](#Solution-Approach)
* [Maintain the Program](#Maintain-the-Program)
* [Contribute and Update](#Contribute-and-Update)
* [Acknowledgments and License](#Acknowledgments-and-License)

## About the Program
A program written in Python that aim to help an internal user to automate this process of comparing two images.   

With a given input cvs file and an output result csv file, the program reduce the tedious manual work by comparing images pixel by pixel.  

The goal of this project is to reduce automate process and boost efficiency by [eliminating toil](https://landing.google.com/sre/sre-book/chapters/eliminating-toil/) and making work interesting.

## Getting Started
### Environments
The program could be run in both Windows and MacOS, either in Python IDE or Command Line (Commend Prompt or Terminal).

If you are a Mac user, you can either download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) or running in your terminal directly, followed by the below instructions.  

If you are using Windows, you could do:
- Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) - develop, test and run this program
- Download [Git](https://git-scm.com/download/win), and follow the Mac Instructions
- Running in Command Prompt directly, however you need to run the Windows version of the commands as this docs mainly cover the Linux/MacOS instruction.

### Install python  
To run this program, python 3 is required. If you do not have python installed, or wish to updated existing from python 2, you can do it from [download python](https://www.python.org/downloads/).

### Install Other Libraries  
The program requires Python Image Library - PIL. We can easily install  [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), which is the friendly PIL fork by running following command:
```shell
$ pip3 install Pillow
```
This is the same command for Windows, MacOS and Linux  Installation

## How to Use the Program

### Clone This Repo
To clone this repo, you can use various source code management tool such as [Source Tree](https://www.sourcetreeapp.com/) and [Github Desktop](https://desktop.github.com/) or simply run
```shell
git clone https://github.com/discoliver/image_comparsion.git
```


### Running the Program
To run this program, simply run the **compare.py** script, following a cvs file path which contains pairs of images. Run the following command in your Terminal/Command Prompt or Pycharm Terminal.  
```shell
python3 compare.py filename.csv
```  
or
```shell
python3 compare.py absolute/path/to/your/filename.csv
```  
This repo has also provided an example of this input cvs file **images.csv**, which indicates the format should follow to use this program.  



### Result and Test
How do you know if this program works? This project includes a [images](https://github.com/discoliver/image_comparison/tree/master/Test/images) folder, which contains a test set of images, as well as an example of input file, [images.cvs](https://github.com/discoliver/image_comparison/blob/master/Test/images.csv).

Therefore, you could simply run the command below to see the test result.  
```shell
python3 compare.py Test/images.csv
```

For the test details and method, please visit [Test&Result.md](https://github.com/discoliver/image_comparison/blob/master/Docs/Test%26Result.md) for more details.


## Solution Approach

Please visit [SOLUTION.md](https://github.com/discoliver/image_comparison/blob/master/Docs/SOLUTION.md) for the methodology and approach used in this program.  

## Maintain the Program
To Maintain this application, please go through this README carefully and [contact me](mailto:b96wang@edu.uwaterloo.ca?subject=[GitHub]%20Source%20Han%20Sans) if you have any question. Additional knowledge transfer session will be hold.

Ensuring that you have understood the logic of the program is fundamental to maintain this project, however, there are couple tips can help as well.  

1. Read error log - details catch error and debug output is written in the script.
2. Check your environment - although this program does not require many dependencies, you still have to check you have correct version of python, and other libraries installed.  
3. Always test it when you contribute this program; Work in specific topic branches and keep the commit history clean, with proper tag if necessary.  
4. Refer to [FAQ](#FAQ) session for common question.

## Contribute and Update
Your contribution are warmly welcomed to make this project better. Please fork the repository and create pull request if you want. Appreciate anyone to jump in and help out.

This project does not include much dependency but a few things below could help you maintain the latest version of the application.
- Contact the author to add the user to the [Github Notification](https://help.github.com/en/articles/about-email-notifications-for-pushes-to-your-repository). When new merge, push or other activities happens you will receive the updates.
- Ensure you have the latest version of pillow
- Ensure your Python is up-to-date

## Acknowledgments and License
There are a few helpful examples and research help to shape this project, and they have demonstrated the different perspectives and methods to accomplish the test. Here are some of good references.  

[Image Module](https://pillow.readthedocs.io/en/stable/reference/Image.html), The Image module provides a class with the same name which is used to represent a PIL image.  
[Rosetta Code](https://rosettacode.org/wiki/Percentage_difference_between_images#Python), Percentage difference between images .  
[Adrian Rosebrock](https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/), How-To: Python Compare Two Images .

This project is licensed under the MIT License.

## FAQ
Frequently asked questions about this program can be found below.  

### How to ensure this program works?
There are some test files in the image folders, which covers different case from modification, contrast adjustment and image rotation. Feel free to contribute more test case or contact the author if you needed.  


### Is there any additional Training resource about this program?  
Yes. You have found detailed material in [image similarity](https://rosettacode.org/wiki/Percentage_difference_between_images) and [python image library](https://pillow.readthedocs.io/en/stable/).
Additionally, a knowledge transfer session and detailed walk through will be provided when delivering this program. You can also contact the author for quick help.

### What if I have received error?  
Check the console output to quickly categorize the error either in:  
- Your system environment, either python or related libraries is setup incorrectly.  
- Your input csv contains wrong format.  
- ~~Your image mode is not RGB or the format we do not support.~~ This has been fixed by this [fix](https://github.com/discoliver/image_comparison/commit/830cdd09a56e861a5aa52604328442d17531594e)

### Can I input cvs files with different format?  
Unfortunately, you have to follow the format of the provided csv example.

### Does this program restrict to MacOS?  
This program can be running on MacOS, Windows and Linux, as long as you have configured correctly. (See getting started)
The easiest way to run on Windows is to get Git Bash and follow the MacOS instruction, but you can always run in Windows Command Prompt or Pycharm IDE.  
