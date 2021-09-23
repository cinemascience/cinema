# Cinema Toolkit, v2.0 (October  2021)

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

# Cinema Toolkit code and repositories

Many Cinema-related repositories can be found on the [github cinema group](https://github.com/cinemascience),
however, those repositories are not automatically considered to be part of the official supported 
Cinema releases. Supported Cinema repositories are included here, in the Cinema toolkit.

# Update to Cinema 2.0

The Cinema toolkit is updated with this release to track the [cinemasci module](https://github.com/cinemascience/cinemasci), where the bulk of new work is now being released. This new model of the Cinema Toolkit depricates command line tools, and embraces a single python module that contains a useful set of components for reading, writing and viewing Cinema databases. 

Major updates for this release of the toolkit:

- [The Cinema Composable Image Set specification](https://github.com/cinemascience/cinema/blob/master/specs/dietrich/01/extensions/cis/1.0/cis_specification_v1-0.md) The CIS specification supports composable images, which allow interactive coloring and manipulation (such as layer on/off control, etc.), and allows scientists access to float values from within the images.

<p align="center">
<img width="75%" src="https://raw.githubusercontent.com/wiki/cinemascience/cinemasci/img/capability_figure.png"></img>
</p>

- [Jupyter Notebook support]() Jupyter notebooks are a very flexible way for scientists to interact with Cinema databases. In conjunction with the CIS image format, this provides novel ways to analyze and present Cinema databases. Included in the `cinemasci` module are renderers and viewers providing reference implementations for Jupyter-based viewers.

<center>
<img width="75%" src="https://github.com/cinemascience/cinemasci/wiki/img/viewer_figure.png"></img>
</center>

# The Cinema Ecosystem

The Cinema ecosystem consists of database specifications, writers,
[viewers](http://cinemaviewer.org) and algorithms. Among the many use cases for
Cinema are two common ones:

- If you have a scientific dataset, and you'd like to create a Cinema database,
  you can easily export one using the Cinema writers incorporated into 
[ParaView](http://paraview.org) and [VisIt](http://visit.llnl.gov).
- You can write your own database, using your current data, by referencing one
  of the database specifications in this repository.

# Cinema Binder examples

The Cinema ecosystem consists of database specifications, writers,
[viewers](http://cinemaviewer.org) and algorithms. Among the many use cases for
Cinema are two common ones:

# Cinema Open Source releases

All of the Cinema open source code can be found under the `cinemascience` group at
`https://github.com/cinemascience`. This repository collects the officially released
code. Other repositories under the `cinemascience` organization are considered
*experimental*, and are not supported as production code by the Cinema team, but 
are viable projects dedicated either to experimental applications, algorithms or
viewers.

# Cinema Release 

The Cinema toolkit consists of the following directories and repositories. Version information, test plans and documentation can be found in the individual repositories: 

- `specs/`, a set of specifications for Cinema databases
- `cinemasci/`
    - the [`cinemasci`](https://github.com/cinemascience/cinemasci) module, which now contains the bulk of the components, including viewers. 

# Checking out this toolkit 

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

