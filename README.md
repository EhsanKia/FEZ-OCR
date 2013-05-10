Fez Cipher decoder in Python
=======

Requirements:
- Python 2.x
- OpenCV 2.4+
- Numpy

Limitations:
- It requires you to give the approximate size of the glyphs (in px)
- It sometimes picks up garbage in the background (if you don't crop everything else)
- It doesn't try to tell apart u/v and other mixed letter glyphs
- [Low contrast images](http://i.imgur.com/HxsFjHx.png) require manual pre-processing.

Usage:
`decoder.py <filename> <size>`
Where filename is the image file and size is the minimum size for the glyph.

The script already comes with the training data, but if you want to make your own, just use training.py.
It'll show you a bunch of glyphs and you need to press the corresponding key on your keyboard.
You can feed it your own image too (by default it's just alphabet.png).

Examples:

["w ha ha ha check out mr rectangle head ouer there"](http://i.imgur.com/RolNJil.png) (Notice the stray w here)

["the points constellate conspire to create shapes shapes to tessellate"](http://i.imgur.com/JEQ6l3n.png)

["oopuoate eoanneir osnoaamm upisbsei xtfatoaa etgelnnc ews"](http://i.imgur.com/pi1LjHI.png)
