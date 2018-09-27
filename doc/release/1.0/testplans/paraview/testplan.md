Cinema GUI test plan for a cinema export
----------------------------------------

| Using the Macro (Easiest to reproduce)                 |
|-----------------------------|
|1. Edit waveletCinemaTest.py<br/><br/>- Change line 80 to a file path of your choice|
|2. Start a fresh ParaView|
|3. Add waveletCinemaTest.py as a new macro (This only needs to be done once. ParaView retains macros)<br/><br/>- Top menu -> Macros -> Add new macro... -> select waveletCinemaTest.py<br/><br/>![addNewMacro.jpg](figures/addNewMacro.jpg)<br/><br/>|
|4. Run the macro<br/><br/>- Macros -> waveletCinemaTest.py ... Or select the macro on your toolbar <br/><br/>![macroLocation.jpg](figures/macroLocation.jpg)<br/><br/>|
|5. The render view should look something like this when finished:<br/><br/>![paraviewWaveletScreenshot.jpg](figures/paraviewWaveletScreenshot.jpg)<br/><br/>|
|6. Open cinema and view the newly saved cdb<br/><br/>- File -> Open file-name.cdb<br/><br/>- Cinema on initial load should look like this:<br/><br/>![cinemaWaveletScreenshot.jpg](figures/cinemaWaveletScreenshot.jpg)<br/><br/>- Rotate along theta, rotate along phi. Everything should look right<br/><br/>|

| Without the Macro (Nice for seeing what the macro does)            |
|-----------------------------|
|1. Start a fresh ParaView    |
|2. Create a 40<sup>3</sup> wavelet source:<br/><br/>- Sources -> Alphabetical -> Wavelet<br/><br/>![wavelet.jpg](figures/wavelet.jpg)<br/><br/>- Change extents to -20 to 20 -> Apply</br/>![waveletProperties.jpg](figures/waveletProperties.jpg)<br/><br/>|
|3. Apply 3 contour levels:<br/><br/>- Select Wavelet1 in the Pipeline Browser -> Filters -> Alphabetical -> Contour<br/><br/>![contour.jpg](figures/contour.jpg)<br/><br/>- Contour at RTData of 140, 150, and 200. Check the "Compute Scalars" box -> Apply<br/><br/>![contourProperties.jpg](figures/contourProperties.jpg)<br/><br/>|
|4. Extract a subset and volume render it:<br/><br/>- Select Wavelet1 in the Pipeline Browser -> Filters -> Alphabetical -> Extract Subset<br/><br/>![extractSubsetLocation.jpg](figures/extractSubsetLocation.jpg)<br/><br/>- Change Z extent to -20 to 10 -> Apply<br/><br/>![extractSubsetProperties.jpg](figures/extractSubsetProperties.jpg)<br/><br/>![extractSubsetColors.jpg](figures/extractSubsetColors.jpg)<br/><br/>|
|5. Export CDB:<br/><br/>- File -> Export Scene<br/><br/>![exportScene.jpg](figures/exportScene.jpg)<br/><br/>- Choose file name and location -> ok<br/><br/>- Cinema Options: Uncheck composite, and set Camera Type to phi-theta, Save<br/><br/>![cinemaOptions.jpg](figures/cinemaOptions.jpg)<br/><br/>|
|4. After exporting, ParaView should look like this:<br/><br/>![paraviewWaveletScreenshot.jpg](figures/paraviewWaveletScreenshot.jpg)<br/><br/>|
|5. Open cinema and view the newly saved cdb<br/><br/>- File -> Open file-name.cdb <br/><br/>- Compare first screen with this screenshot:<br/><br/>![cinemaWaveletScreenshot.jpg](figures/cinemaWaveletScreenshot.jpg)<br/><br/>- Rotate along theta, rotate along phi. Everything should look right<br/><br/>|