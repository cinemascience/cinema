# Cinema Release Notes v1.3

This release is targeted at updating the Cinema toolkit to handle more types of files in Cinema databases.
It includes updates to the Cinema specification, previously released Cinema code, and additions to the
Cinema viewers.

## Cinema Specification

This release of Cinema includes an updated `Cinema data specification`.

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

## Cinema Submodules

The following submodules have been updated to accomodate the new specification. See the documentation,
examples and test plans in each submodule for more information on changes.

- `viewers/`
    - `cinema_components`, a set of components that can be used to build browser-based cinema viewers 
    - `cinema_explorer`, the main browser-based cinema viewer, based on `cinema_components`
- `writers/`
    - `cinema_lib`, the cinema python library and `cinema` command line tool

The following submodules have been added for this release:
    - `cinema_compare`, a simple comparison viewer for one or more databases 


