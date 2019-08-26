


# Image Comparison

## Table of contents . 

* [About the Program](#About-the-Program)
* [Getting Started](#Getting-Started)
* [How to Use the Program](##ow-to-Use-the-Program)
* [Solution Approach](#Solution-Approach)
* [Maintain the Program](#Maintain-the-Program)
* [Contribute and Update](#Contribute-and-Update)
* [Acknowledgments and License](#Acknowledgments-and-License)

## About the Program
A program in Python that compares two images pixel by pixel. The input and output of the program will be a format cvs file.  

## Getting Started - Steps by Steps
### Environments
The program could be run in both Windows and MacOS system, either in Python IDE or Terminal (Commend Prompt in Windows)

If you are a Mac user, you can either download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) or running in your terminal directly, followed by the below instructions.  
If you are using Windows, you could do:
- Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) - develop, test and run this program
- Download [Git](https://git-scm.com/download/win), and follow the Mac Instructions
- Running in Command Prompt directly, however you need to run the Windows version of the commands as this docs mainly cover the Linux/MacOS instruction.



### Install python  
To run this program, python 3.0 is required. If you do not have python installed, or wish to updated existing from python 2, you can do it from [download python](https://www.python.org/downloads/).

### Install Other Libraries  
The program requires Python Image Library - PIL. We can easily install  [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), which is the friendly PIL fork by running following command:
```shell
$ pip install Pillow
```
This is the same command for Windows, MacOS and Linux  Installation



## How to Use the Program

### Clone This Repo
To clone this repo, you can use various source code management tool such as [Source Tree](https://www.sourcetreeapp.com/) and [Github Desktop](https://desktop.github.com/) or simply run
```shell
git clone https://github.com/discoliver/image_comparsion.git```


### Running the Program
To run this program, simply run the ** compare.py ** script, following a cvs file path which contains pairs of images.
```shell
python compare.py filenae.csv
```
or
```shell
python compare.py absolute/path/to/yout/filenae.csv
```
If you have python 2 co-exist with python 3, you need to run
```shell
python3 compare.py filenae.csv
```
This repo has also provided an example of this input cvs file - ** images.csv **, which indicate the format should follow for this program to run.

You can also run them in PyCharm as well.


### Result and Test
After successfully run the program (See FAQ for error you might get), you should expect a **result.csv** file in your repo, which contains the information of 2 images, a similarity score and an elapsed time.

Re-run the program will automatically delete the file and regenerate the new result file.


## Solution Approach
### Backgroud
### Thoughts Gathering
### Initial Approach
### Improving
### Advantages and drawbacks
(coming)

## Maintain the Program
(coming)

## Contribute and Update
Your contribution  are warmly welcome to make this project better. Please fork the repository and create pull request if you want. Appreciate anyone to jump in and help out.

Please refer to `CONTRIBUTING.md` (coming) for more details.  

This project does not include much dependency but a few things below could help you maintain the latest version of the application.
- Github Notification when updates or new pull request has been merged (coming)
- Ensure you have the latest version of pillow
- Ensure your Python is up-to-date


## Acknowledgments and License
There are a few helpful examples and research help to shape this project, and they have demonstrated the different perspectives and methods to accomplish the test. Here are some of good references.  
  
 
[Image Module](https://pillow.readthedocs.io/en/stable/reference/Image.html), The Image module provides a class with the same name which is used to represent a PIL image.  
[Rosetta Code](https://rosettacode.org/wiki/Percentage_difference_between_images#Python), Percentage difference between images .  
[Adrian Rosebrock](https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/), How-To: Python Compare Two Images . 




This project is licensed under the MIT License - see the LICENSE.md file for details

## FAQ
(coming)
