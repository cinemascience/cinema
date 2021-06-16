# Examples

## Simplest example
The simplest example is a single image set with a single layer and a single channel. All other values are set to default by any application that reads this data.

|CISID.1.0|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|FILE|
|-|-|-|-|-|-|-|
|"0"|"0"|512|512|"0"|pressure|cis0000.npz|

```
CISID.1.0,CISimage,CISImageWidth,CISImageHeight,CISLayer,CISChannel,FILE
"0","0",512,512,"0",pressure,cis0000.npz
```

Adding an additional image looks like this:
|CISID.1.0|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|FILE|
|-|-|-|-|-|-|-|
|"0"|"0"|512|512|"0"|pressure|cis0000.npz|
|"0"|"1"|512|512|"0"|pressure|cis0000.npz|

```
CISID.1.0,CISimage,CISImageWidth,CISImageHeight,CISLayer,CISChannel,FILE
"0","0",512,512,"0",pressure,cis0000.npz
"0","1",512,512,"0",pressure,cis0000.npz
```

## Simplest example with additional metadata
The above example can include any number of columns of additional metadata, per the Cinema database specification. For example, including time and camera metadata could look like this. The example includes images across several time and camera positions:

|phi|theta|time|CISID.1.0|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|FILE|
|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|"0"|"0"|512|512|"0"|pressure|cis0000.npz|
|1.0|1.0|0.0|"0"|"0"|512|512|"0"|pressure|cis0001.npz|
|0.0|0.0|1.0|"0"|"1"|512|512|"0"|pressure|cis0002.npz|
|1.0|1.0|1.0|"0"|"1"|512|512|"0"|pressure|cis0003.npz|

```
CISID.1.0,CISimage,CISImageWidth,CISImageHeight,CISLayer,CISChannel,FILE
"0","0",512,512,"0",pressure,cis0000.npz
```

## Example with some data explicit 
This example provides values for the `CISImageWidth`, and `CISImageHeight` values.

|CISID.1.0|CISImage|CISImageOrigin|CISImageWidth|CISImageHeight|CISLayer|CISChannel|CISChannelType|FILE|
|-|-|-|-|-|-|-|-|-|
|"0"|"0"|UL|512|512|"0"|pressure|float|cis0000.npz|

```
CISID.1.0,CISImage,CISImageWidth,CISImageHeight,CISLayer,CISChannel,CISChanne,FlILE
"0","0",UL,512,512,"0",pressure,float,cis0000.npz
```
