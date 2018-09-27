# Cinema Toolkit

The Cinema toolkit has been developed by Los Alamos National Laboratory, as part
of the [Cinema Project](http://cinemascience.org).

Cinema is an innovative way of capturing, storing and exploring extreme scale
scientific data. It is a highly interactive image-based approach to data
analysis and exploration that promotes investigation of large scientific
datasets, and is easily integrated into your existing workflows through
extensions to widely used open source tools. This novel approach supports
interactive exploration of a wide range of results, while still significantly
reducing data movement and storage.

Extreme scale scientific simulations are leading a charge to exascale
computation, and data analytics runs the risk of being a bottleneck to
scientific discovery. Due to power and I/O constraints, we expect in situ
visualization and analysis will be a critical component of these workflows.
Options for extreme scale data analysis are often presented as a stark contrast:
write large files to disk for interactive, exploratory analysis, or perform in
situ analysis to save detailed data about phenomena that a scientists knows
about in advance. With Cinema, we have developed a novel framework for a third option – a highly
interactive, compact and scalable way to explore data.

# The Cinema Ecosystem

The Cinema ecosystem consists of database specifications, writers,
[viewers](http://cinemaviewer.org) and algorithms. Among the many use cases for
Cinema are two common ones:

- If you have a scientific dataset, and you'd like to create a Cinema database,
  you can easily export one using the Cinema writers incorporated into 
[ParaView](http://paraview.org) and [VisIt](http://visit.llnl.gov).
- You can write your own database, using your current data, by referencing one
  of the database specifications in this repository.

# Cinema Open Source releases

All of the Cinema open source code can be found under the `cinemascience` group at
`https://github.com/cinemascience`. This repository collects the officially released
code. Other repositories under the `cinemascience` organization are considered
*experimental*, and are not supported as production code by the Cinema team.

# Cinema Release 

**[Current Release Notes](doc/release/1.0/notes.md)**

The Cinema toolkit consists of the following directories and repositories. Version information, test plans and documentation can be found in the individual repositories: 

- `specs/`, a set of specifications for Cinema databases
- `viewers/`
    - `cinema_components`, a set of components that can be used to build browser-based cinema viewers 
    - `cinema_explorer`, the main browser-based cinema viewer, based on `cinema_components`
    - `cinema_compare`, a simple comparison viewer for one or more databases 
- `writers/`
    - `cinema_lib`, the cinema python library and `cinema` command line tool

# Submodules in this repository 

Please note that this repository contains submodules, so you will have to update
those modules after cloning:
````
git submodule update --init --recursive
````

# Cinema mailing list

Please mail `cinema-info@lanl.gov` with any questions.

# Acknowledgements
Cinema is a research project managed by the 
[Data Science at Scale Team](http://datascience.dsscale.org) 
team at Los Alamos National Laboratory.

