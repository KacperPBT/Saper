# Button

## Class **Buton**

### Short descripton

### Used libraries

- pygame
- time

### What it does

#### __init__

##### Arguments

- coordinates - position top left
  - *tuply (x, y)*
- images (1, 2, 3) - pictures of button in state:
  - 1: standby, 
  - 2: after left click (if not given it's set the same picture as image1)
  - 2: after right click (if not given it's set the same picture as image2)
  - *already loaded by pygame* or *path to file* (all in one type)
- scale - scale to given pictures
  
##### Action

- set images that wasn't given to alternative one
- if images was given by giving paths to file, automatically load all pictures
- scales pictures (all pictures take width and height of **image1**) 

#### draw_l

##### Arguments

- surface
- blocker