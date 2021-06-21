# Keywords

The following are reserved keywords that implement the CIS extension metadata:

|Keyword| Required | Type | Default | Definition |
|-|-|-|-|-|
|CISImage           |X|string|N/A|ID of the image. Any unique string on the path CISID|
|CISVersion         |X|string|N/A|version number of the CIS extension specification|
|CISImageFlags      | |string|Null|List of image flags (see below)|
|CISImageWidth      |X|int   |N/A|Integer, number of pixels in width|
|CISImageHeight     |X|int   |N/A|Integer, number of pixels in height|
|CISLayer           |X|string|N/A|ID of the layer. Any unique string on the path CISID/CISImage| 
|CISLayerOffsetX    | |int   |0|Integer, number of pixels to offset layer origin|
|CISLayerOffsetY    | |int   |0|Integer, number of pixels to offset layer origin|
|CISLayerWidth      | |int   |CISImageWidth|Integer, number of pixels in width|
|CISLayerHeight     | |int   |CISImadeHeight|Integer, number of pixels in height|
|CISChannel         |X|string|N/A|ID of the channel. Any unique string on the path CISID/CISImage/CISLayer, with the exception of the reserved keywords (see below)| 
|CISChannelVar      | |string|N/A|Variable for the channel, if different from the Channel ID|
|CISChannelVarType  | |string|float|Type of data in the channel. One of: string, int, float|
|CISChannelVarMin   | |string|Derived from channel|Channel variable global min|
|CISChannelVarMax   | |string|Derived from channel|Channel variable global max|
|CISChannelColormap | |string|N/A|A colormap definition for the channel|


### CISChannel keywords

- CISShadow is the name of a layer's shadow channel
- CISDepth is the name of a layer's depth channel

### CISImageFlags keywords

- IMAGES_INDEPENDENT images DO NOT have the same set of layers and channels. 
    Default, if this flag is not included, is that all images 
    have the same layers, and all layers have the same channels.

# Removed

|Keyword| Required | Type | Default | Definition |
|-|-|-|-|-|
|CISOrigin          | |string|UL |One of "UL, UR, LL, LR"|

