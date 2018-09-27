#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Wavelet'
wavelet1 = Wavelet()

# Properties modified on wavelet1
wavelet1.WholeExtent = [-20, 20, -20, 20, -20, 20]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1734, 2208]

# show data in view
wavelet1Display = Show(wavelet1, renderView1)
# trace defaults for the display properties.
wavelet1Display.Representation = 'Outline'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(Input=wavelet1)

# Properties modified on contour1
contour1.ComputeScalars = 1
contour1.Isosurfaces = [140.0, 150.0, 200.0]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')

# set active source
SetActiveSource(wavelet1)

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=wavelet1)

# Properties modified on extractSubset1
extractSubset1.VOI = [-20, 20, -20, 20, -20, 10]

# show data in view
extractSubset1Display = Show(extractSubset1, renderView1)
# trace defaults for the display properties.
extractSubset1Display.Representation = 'Outline'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractSubset1Display, ('POINTS', 'RTData'))

# rescale color and/or opacity maps used to include current data range
extractSubset1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractSubset1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
extractSubset1Display.SetRepresentationType('Volume')

# export view
#TODO: Change /path/to/file to your path
ExportView('/path/to/file/wavelet.cdb', view=renderView1, ViewSelection='\'RenderView1\' : [\'image_%t.png\', 1, 0, 1, 867, 1104, {"composite":False, "floatValues":True, "noValues":False, "camera":"phi-theta", "phi":[-180,-150,-120,-90,-60,-30,0,30,60,90,120,150],"theta":[-90,-64,-38,-12,13,38,63,88], "roll":[1], "initial":{ "eye": [0,0,168.227], "at": [0,0,0], "up": [0,1,0] }, "tracking":{ "object":"None" } }]',
    TrackSelection='',
    ArraySelection="'wavelet1' : ['RTData'], 'extractSubset1' : ['RTData'], 'contour1' : ['RTData']")

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 168.22733705710414]
renderView1.CameraParallelScale = 44.11035966680601

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
