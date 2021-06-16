# Meaning

To control access and reconstruction of the images, it's useful to look at the parameters
and how they define images.

An image is a logical collection of layers defined by a set of parameters. Therefore, we
expect all of the non-CIS parameters for a specific image to be the same. For example, this
table shows two images, where an image is defined by `time, phi, theta` tuples. Thus, when any
of these three parameters change, we would expect a new image.

|time|phi|theta|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|CISChannelVar|CISChannelType|FILE|
|-|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|0|512|512|0|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|0|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|0|temperature|float|temperature|cis0002.npz|
|0.0|0.0|0.0|0|512|512|1|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|1|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|1|temperature|float|temperature|cis0002.npz|
|1.0|0.0|0.0|1|512|512|0|||depth|cis0003.npz|
|1.0|0.0|0.0|1|512|512|0|pressure|float|pressure|cis0004.npz|
|1.0|0.0|0.0|1|512|512|0|temperature|float|temperature|cis0005.npz|
|1.0|0.0|0.0|1|512|512|1|||depth|cis0003.npz|
|1.0|0.0|0.0|1|512|512|1|pressure|float|pressure|cis0004.npz|
|1.0|0.0|0.0|1|512|512|1|temperature|float|temperature|cis0005.npz|

In practice, we expect all images to have the same layers and all layers to have the same channels.
In this case, not having a channel would be the same as the channel having nothing in it. Therefore,
these three datasets have the same content:

### Case 1: All channels have data

|time|phi|theta|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|CISChannelVar|CISChannelType|FILE|
|-|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|0|512|512|0|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|0|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|0|temperature|float|temperature|cis0002.npz|
|0.0|0.0|0.0|0|512|512|1|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|1|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|1|temperature|float|temperature|cis0002.npz|

### Case 2: Some channels have no files

|time|phi|theta|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|CISChannelVar|CISChannelType|FILE|
|-|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|0|512|512|0|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|0|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|0|temperature|float|temperature||
|0.0|0.0|0.0|0|512|512|1|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|1|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|1|temperature|float|temperature|cis0002.npz|

### Case 2: Some channels are not present 

In this case, `layer 1` has no `pressure` values. In practice this means that if that layer were to be displayed, 
we would see a 512x512 blank image.

|time|phi|theta|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|CISChannelVar|CISChannelType|FILE|
|-|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|0|512|512|0|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|0|pressure|float|pressure|cis0001.npz|
|0.0|0.0|0.0|0|512|512|0|temperature|float|temperature|cis0002.npz|
|0.0|0.0|0.0|0|512|512|1|||depth|cis0000.npz|
|0.0|0.0|0.0|0|512|512|1|temperature|float|temperature|cis0002.npz|

