# Cinema Release Notes v1.0

This release is targeted at updating the Cinema toolkit to handle more types of files in Cinema databases.

Though it was originally conceived as an image database, Cinema has proved useful in a variety of 
use cases for helping scientists to organize, browse and analyze data. To adapt to this, the Cinema 
specification has been expanded to include any file type. It also includes multiple files per 
entry in a Cinema database.

For example, this is a Cinema database that includes one image and one `vti` file per 
time step: 

```
example.cdb/
    data.csv
    img/
        01.png
        02.png
        03.png
    vti/
        01.vti
        03.vti
        03.vti
```

This database would have the following `data.csv` file:

```
time,FILE,FILE grid
1.0,img/01.png,vti/01.vti
2.0,img/02.png,vti/02.vti
3.0,img/03.png,vti/03.vti
```
