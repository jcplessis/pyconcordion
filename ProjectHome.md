_PyConcordion_ is a Python port of [Concordion](http://www.concordion.org/).

That is :
  * Write your specification in HTML with Concordion instrumentation
  * Write your fixture in Python just like you would write a fixture in Java
  * Run your tests either individually or with the folder runner
  * Look at the Concordion report


# Alternative #

Another tool to use concordion in python is available at https://github.com/johnjiang/pyconcordion2 thanks to John Jiang. The work is still in progress and in an `alpha` version but it's 100% python thus easier to install/use.

# Latest version #
New release is out : version 0.10
  * Adding support for `concordion:run`

# How to try it ? #

First be sure to have :
  * python (version >= 2.5)
  * a Java JDK (version >= 1.5), if your system does not contain one please download it from [Sun Microsystem](http://java.sun.com/javase/downloads/index.jsp).

To try it :
  * download latest PyConcordion release (a .tgz file)
  * extract the tgz file
  * run `python setup.py install` in your command line from the extract directory
  * if **java** and **javac** are in your `PATH` skip this
    * either set your `PATH` to include **java** and **javac**
    * or modify config.ini from your local dist\_packages directory and set **java\_command** and **javac\_command** to point the place these commands are available
  * run command `concordion_folder_runner *your_test_directory*` (under linux this will work, under windows you may have to do something like `python C:\Python26\Scripts\concordion_folder_runner *your_test_directory*`)

You can take a look at the [two minutes example](TwoMinutesExample.md) to see how to write a test. More tests are available in the source repository and you may check [Concordion Tutorial](http://www.concordion.org/Tutorial.html) for Concordion syntax. See CurrentRestrictions for more details.