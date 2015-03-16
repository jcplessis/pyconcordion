# Introduction #

Since release 0.8 pyconcordion supports some of [concordion-extensions](http://code.google.com/p/concordion-extensions/). Here is a small tutorial of how to activate extensions and use them.


# Details #

By default no extension is activated, to activate them provide the extension name either when launching `concordion_folder_runner` with -e option set or by modifying the config.ini that is available in your _dist\_package_ directory.


Example to activate all the concordion-extensions : concordion\_folder\_runner -e org.concordion.ext.Extensions **your\_test\_directory**

To activate only one or several extensions you can use a comma separated list of extensions to activate. Correct values are :
  * org.concordion.ext.TimestampFormatterExtension
  * org.concordion.ext.ScreenshotExtension
  * org.concordion.ext.EmbedExtension

concordion-extensions provides:
  * a screenshot extension,
  * a logging extension (not working with pyconcordion),
  * a timestamp extension (automatically used without html tag),
  * a translator extension (not working with pyconcordion),
  * an embed html extension.

The screenshot extension is used as in concordion (no python code required), embed html is used as in concordion except you write your method in python. Check [the example in the source of this project](http://code.google.com/p/pyconcordion/source/browse/trunk/examples/screenshot/ScreenshotExample.html).
