2.0.2 * 2011-11-18
------------------

  * Removing of linked element now removes `<a>` as well
  * Fixed white space recognition in passed strings
  * Added special case for path that has only one Catmull-Rom curve
  * Fixed toTransformString method
  * Fixed animateWith method
  * Fixed “target” attribute clearing
  * Fixed bug with changing fill from image to solid colour
  * fixed renderfix method

2.0.1 * 2011-11-18
------------------

  * Global variables leakage fix
  * `toFront` fix for elements with links
  * Gradient clean up
  * Added `letter-spacing` attribute
  * Fixed hsb methods
  * Fixed image flickering
  * Improved `toTransformString` method on `matrix`
  * Fixed drag'n'drop
  * New method [Paper.add](http://raphaeljs.com/reference.html#Paper.add)
  * Fix for `clip-path`
  * Doc update

2.0.0 * 2011-10-03
------------------

  * Completely changed transformation handling:
    * `translate()`, `rotate()` and `scale()` are deprecated
    * `translation`, `rotation` and `scale` attributes are removed (!)
    * new method `transform()` and new attribute `transform` were introduced
    * chaining of transformations now allowed
    * matrix transformation introduced
    * see [docs](http://raphaeljs.com/reference.html#Element.transform)
  * Animation API was updated (see [docs](http://raphaeljs.com/reference.html#Raphael.animation))
    * delay, repeat, [setTime](http://raphaeljs.com/reference.html#Element.status), [status](http://raphaeljs.com/reference.html#Element.setTime)
  * New methods:
    * [Paper.setViewBox](http://raphaeljs.com/reference.html#Paper.setViewBox)
    * [Paper.setStart](http://raphaeljs.com/reference.html#Paper.setStart)
    * [Paper.setFinish](http://raphaeljs.com/reference.html#Paper.setFinish)
    * [Paper.forEach](http://raphaeljs.com/reference.html#Paper.forEach)
    * [Paper.getById](http://raphaeljs.com/reference.html#Paper.getById)
    * [Paper.getElementByPoint](http://raphaeljs.com/reference.html#Paper.getElementByPoint)
    * [Element.data](http://raphaeljs.com/reference.html#Element.data)
    * [Element.glow](http://raphaeljs.com/reference.html#Element.glow)
    * [Element.onDragOver](http://raphaeljs.com/reference.html#Element.onDragOver)
    * [Element.removeData](http://raphaeljs.com/reference.html#Element.removeData)
    * [Raphael.fullfill](http://raphaeljs.com/reference.html#Raphael.fullfill)
    * [Raphael.matrix](http://raphaeljs.com/reference.html#Raphael.matrix)
    * [Raphael.parseTransformString](http://raphaeljs.com/reference.html#Raphael.parseTransformString)
    * [Set.clear](http://raphaeljs.com/reference.html#Set.clear)
    * [Set.exclude](http://raphaeljs.com/reference.html#Set.exclude)
    * [Set.forEach](http://raphaeljs.com/reference.html#Set.forEach)
    * [Set.splice](http://raphaeljs.com/reference.html#Set.splice)
  * VML completely rewritten
  * `getBBox` was fixed to take transformations into account
  * [eve](http://raphaeljs.com/reference.html#eve) was added to the project
  * Whole new [documentation](http://raphaeljs.com/reference.html)
  * Various bug fixes
