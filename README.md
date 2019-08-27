# Image Comparison

## Table of contents  

* [About the Program](#About-the-Program)
* [Getting Started](#Getting-Started)
* [How to Use the Program](#How-to-Use-the-Program)
* [Solution Approach](#Solution-Approach)
* [Maintain the Program](#Maintain-the-Program)
* [Contribute and Update](#Contribute-and-Update)
* [Acknowledgments and License](#Acknowledgments-and-License)

## About the Program
A program written in Python that aims to help an internal user to automate the manual process of comparing two images.   

With a given input cvs file containing image pairs, and produced a result csv file including similarity score, the program reduces the tedious repetitive work by comparing the images pixel by pixel.  

The goal of this project is to automate the manual process, reduce operational cost,  boost efficiency and make work interesting. Please see more details on [eliminating toil by Google SRE](https://landing.google.com/sre/sre-book/chapters/eliminating-toil/)

## Getting Started
### Environments
The program could be run in both Windows and MacOS, either in Python IDE or Command Line (Command Prompt or Terminal).  


If you are a Mac user, you can either download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) or running in your terminal directly, followed by the below instructions.  

If you are using Windows, you could do:
- Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) - develop, test and run this program
- Download [Git Bash](https://git-scm.com/download/win) or [Linux Bash](https://itsfoss.com/bash-on-windows/), and follow the Mac Instructions.  
- Running in Command Prompt directly, however you need to run the Windows version of the commands as this docs mainly cover the Linux/MacOS instruction.

You could also set up your virtual environment for your python project. You could have isolated space to run a project with python 2.7 or python 3.7. To find more details, [check this](https://docs.python-guide.org/dev/virtualenvs/).


### Install python  
To run this program, python 3 is required. If can download [python 3](https://www.python.org/downloads/) or [update from existing python 2] (https://docs.python.org/3/howto/pyporting.html).  

For MacOS user (or Windows user with bash), the following command could be useful to install python with [brew](https://docs.brew.sh/Homebrew-and-Python) and check the version you have.
```shell
$ python --version
Python 2.7.15  

$ brew install python3  

$ python3 --version
Python 3.7.0
```  

### Install Other Libraries  
The program requires Python Image Library - PIL. We can easily install  [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), which is the friendly PIL fork by running the following command:
```shell
$ pip3 install Pillow
```
This is the same command for Windows, MacOS and Linux Installation

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
If you have your own input cvs already
```shell
python3 compare.py absolute/path/to/your/filename.csv
```  
This repo has also provided an example of this input cvs file **images.csv**, which indicates the format should follow to use this program.  If you want to run this test, you could do the command below:  
```shell
python3 compare.py images.csv
```  
Knowledge transfer session and a demo will be provided to the user and all questions could be answered. Also feel free to [contact me](mailto:b96wang@edu.uwaterloo.ca?subject=[GitHub]%20Source%20Han%20Sans) if you have additional questions.


### Result and Test
How do you know if this program works? This project includes an [images](https://github.com/discoliver/image_comparison/tree/master/Test/images) folder, which contains a test set of images, as well as an example of the input file, [images.cvs](https://github.com/discoliver/image_comparison/blob/master/Test/images.csv).

Therefore, you could simply run the command below to see the test result.  
```shell
python3 compare.py Test/images.csv
```

For the test details and method, please visit [Test&Result.md](https://github.com/discoliver/image_comparison/blob/master/Docs/Test%26Result.md) for more details.


## Solution Approach

Please visit [SOLUTION.md](https://github.com/discoliver/image_comparison/blob/master/Docs/SOLUTION.md) for the methodology and approach used in this program.  

## Maintain the Program

One of the initial goals is to make this project less dependent on a low effort to maintain. In this case, this project dose not require much human effort to update and maintain as it involves minimal dependency.


Go through this README carefully and ensure that you have understood the logic of the program are fundamental to maintain this project. Also I will provide support with demo & knowledge transfer session and [email contact](mailto:b96wang@edu.uwaterloo.ca?subject=[GitHub]%20Source%20Han%20Sans).  

If you would like to continue to build on this project and make improvements, please check [how to contribute this project](#Contribute-and-Update).

There are couple tips can help troubleshoot as well.  

1. Read error log - details catch errors and debug output is written in the script.
2. Check your environment - although this program does not require many dependencies, you still have to check you have the correct version of python, and other libraries installed.  
3. Always test it when you contribute this program; Work in specific topic branches and keep the commit history clean, with a proper tag if necessary.  
4. Refer to [FAQ](#FAQ) session for common questions.

## Contribute and Update
Your contribution are warmly welcomed to make this project better. Please fork the repository and create pull request if you want.

This project does not include many dependencies but a few things below could help you maintain the latest version of the application.
- Contact the author to add the user to the [Github Notification](https://help.github.com/en/articles/about-email-notifications-for-pushes-to-your-repository). When new merge, push or other activities happen you will receive the updates. Always [check the project status](https://stackoverflow.com/questions/6335681/git-how-do-i-get-the-latest-version-of-my-code) with git repo.  The latest version will always be on Master branch and other develop branch might include improvement in progress. You can find more on [branching strategy](https://www.atlassian.com/git/tutorials/comparing-workflows).  

```shell
git fetch origin
git status
git pull
```  
- Ensure you have the latest version of [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
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
There are a test set of [images](https://github.com/discoliver/image_comparison/tree/master/Test/images) and a [sample input file](https://github.com/discoliver/image_comparison/blob/master/Test/images.csv), which covers different cases from image modification, contrast adjustment and image rotation. Also, please refer to the [test and result](https://github.com/discoliver/image_comparison/blob/master/Docs/Test%26Result.md) session for detail test methodology and analysis.

Feel free to contribute more test case or [contact the author]((mailto:b96wang@edu.uwaterloo.ca?subject=[GitHub]%20Source%20Han%20Sans)) if you needed.  


### Is there any additional Training resource about this program?  
Yes. You have found detailed material in [image similarity](https://rosettacode.org/wiki/Percentage_difference_between_images) and [python image library](https://pillow.readthedocs.io/en/stable/).  

Internally, a knowledge transfer session and detailed walkthrough will be provided when delivering this program. You can also contact the author for quick help.

### What if I have received errors?  
Check the console output to quickly categorize the error either in:  
- Your system environment, either python or related libraries is set up incorrectly.  
- If the image's absolute path in csv input file is wrong, the program will complaint.  
- Your input csv contains wrong formats, please followed this [example format](https://github.com/discoliver/image_comparison/blob/master/Test/images.csv).    
- ~~Your image mode is not RGB or the format we do not support.~~ This has been fixed by this [fix](https://github.com/discoliver/image_comparison/commit/830cdd09a56e861a5aa52604328442d17531594e)
- Google the error message should give you the best answer.

### Can I input cvs files with a different format?  
Unfortunately, you have to follow the format of the provided csv example. However, this can be quickly changed if the original request changes.

### Does this program restrict to MacOS?  
This program can be running on MacOS, Windows and Linux, as long as you have configured correctly. (See getting started)
The easiest way to run on Windows is to get Git Bash and follow the MacOS instruction, but you can always run in Windows Command Prompt or Pycharm IDE.  

### What maintenance work needed to keep the latest version of this program?
Theoretically, no efforts needed as this program require few dependencies. But you can refer [Contribute and Update](https://github.com/discoliver/image_comparison#contribute-and-update) if needed. 