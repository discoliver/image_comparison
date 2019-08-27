
# Solution Approach - Pixel by Pixel Comparison

## Table of contents  

* [Background](#Background)
* [Thoughts Gathering](#Thoughts-Gathering)
* [Initial Approach](##Initial-Approach)
* [Improving](#Improving)
* [Advantages and Drawbacks](#Advantages-and-Drawbacks)


## Background
Image similarity is popular topics with various techniques to approach. In this particular case, we would like like to help an internal user automate his manual process and reduce the operational cost - or to eliminate toil, from [Google SRE](https://landing.google.com/sre/sre-book/chapters/eliminating-toil/). Therefore, the accuracy, stability , performance and comprehensive documents are important criterias.  

## Thoughts Gathering
From couple lines of code to well-developed dedicated application product, tools can be used for image similarity are based on some common theory or principle. Starting research on this topic, I found out couple of techniques to accomplish this task.  
- **Individual Pixel Compare**: Compare RGB value of every individual Pixel.  
- **Structural Similarity Index (SSIM)**:  Compare group of pixels.  
- **Comparing histograms**: Examine the distribution of values in each sample.  
- **Feature matching**: Popular [OpenCV module (features2d)](https://docs.opencv.org/3.0-beta/modules/features2d/doc/features2d.html) to find the homography and overlapping.  
- **Keypoint Matching**: Focus on the certain parts of an image contains more information than others.  
- And much more.   

This project starts with the simplest and most straight forward solution, Individual Pixel Compare, based on the several criteria below.  
1. Accuracy
2. Simplicity with low development cost
3. Easy to understand and maintain
4. Stability without frequent update

However, if more time allowed and more information provided, other solutions could be implement and tailored to this definitely.  

## Initial Approach
The original workflow of this approach demonstrate as below:

1. Import the Image files into `image_list` from cvs.  
2. For every row of data in cvs (every element in `image_list`), create image `i1` and `i2`.  
```python
i1 = Image.open(image_row[0])
i2 = Image.open(image_row[1])
```
3. For each pixel from `i1` and `i2`, subtract the RBG value accordingly and sum up the absolute difference from R, G, B. For example, for the data pair (pixel 1 from `i1` and `i2`): ((176, 207, 148, 255), (255, 255, 255, 255)), we calculate the `dif` value from pixel 1 as below:  
```matlab
dif = abs(176 - 255) + abs(207 - 255) + abs(148 - 255)
```  

For more details, take a look at the data demonstration shown below.  
---
#### Test with pure color, with accurate result
![test data](Docs/data.png)  

The last digital, 255 is The alpha channel which stays with 255 all the time for fully visible.  

4. We record the time `elapsed_time` after complete calculation, and convert `dif` into score of range [0, 1].  

5. Import the data, `dif` and `elapsed_time`into new cvs output file, `result.cvs`.  

## Improving  
Understanding the [drawbacks](#Advantages-and-Drawbacks)
of this pixels approach, there are still couple of code refactoring and improvement on the program could be made.  

1. Implement resize function to solve the case that two images have different size and not able to be compared.
```python
def resize(i1, i2):
   if i1.size != i2.size:
       (width, height) = (i1.width, i1.height)
       i2 = i2.resize((width, height))
```  

2. Create user-defined functions for reusable code blocks, which are more organized, easy to maintain and support modular design approach.  

3. Add comments, error catch and debug script for future improvement, development and maintenance.  


## Advantages and Drawbacks
As mentioned earlier, individual pixel comparison approach is relative fast and simple, easy to understand and maintain. However, I do resize there are couple of drawback in this approach.  

1.  Individual pixel comparison ignore the structural histograms and are easily affect by noise and grit.  

2. Images that are rotated, scaled or skewed can be identified as very different as this approach cannot match homography.  
