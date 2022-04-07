# sverchok-gis-scripts

Basic scripts to import GIS data into blender, through the sverchok addon.

For use with the SNLite node.


## 3rd party libraries

These scripts rely on the geopandas library, which like any 3rd party library, can be tricky to install with blender. 

### using pip

To install geopandas, I used pip, and referenced this page: http://www.codeplastic.com/2019/03/12/how-to-install-python-modules-in-blender/

### common errors

While doing this, I ran into a few issues. Here are brief descriptions of these issues and the solutions I found: 

- "Install Microsoft Visual Studio C++" If you get an error like this, see this thread: https://stackoverflow.com/questions/48541801/microsoft-visual-c-14-0-is-required-get-it-with-microsoft-visual-c-build-t, and start with the steps described in the top answer.
- Cannot install fiona. Fiona is another library that will be installed with geopandas, but I ran into the same issue described here: https://stackoverflow.com/questions/50876702/cant-install-fiona-on-windows. Luckily, following the steps in the top answer solved it for me, which was installing fiona directly with the wheel file found here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
  - I had to do the same steps for the GDAL library, the wheel files can be found on the same site: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

### other

This is a comprehensive thread about geopandas installation issues, worth a read if you are stuck installing geopandas: https://github.com/geopandas/geopandas/issues/1812
