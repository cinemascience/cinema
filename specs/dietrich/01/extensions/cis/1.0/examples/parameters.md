# Examples With Paramters

One of the powerful things about Cinema is the mapping of metadata to extracts. The Simple examples show how to map CIS attributes to files. These examples show how to expand that to more attributes.

## Simplest example with additional metadata
The above example can include any number of columns of additional metadata, per the Cinema database specification. For example, including time and camera metadata could look like this. The example includes images across several time and camera positions:

|phi|theta|time|CISID|CISVersion|CISimage|CISImageWidth|CISImageHeight|CISLayer|CISChannel|FILE|
|-|-|-|-|-|-|-|-|-|-|-|
|0.0|0.0|0.0|0|1.0|i000|512|512|l000|depth|cis0000.npz|
|0.0|0.0|0.0|0|1.0|i000|512|512|l000|pressure|cis0001.npz|
|0.0|0.0|0.0|0|1.0|i001|512|512|l000|depth|cis0000.npz|
|0.0|0.0|0.0|0|1.0|i001|512|512|l000|pressure|cis0001.npz|

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
