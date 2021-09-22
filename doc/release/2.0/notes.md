# Cinema Release Notes v2.0

This release updates the Cinema Toolkit with an entirely new set of repositories, to reflect
the new focus of development for Cinema components. In particular, all officially released Cinema
Toolkit software is included in the `cinemasci` Python module.

## Cinema Specification

## Cinema Submodules

## Testing

Cinema testing is currently handled in the submodules. Each module either has internal unit testing (in the case of `cinema_lib`), or test plans. We are currently upgrading test plans as part of our software release process.

**Third Party Test Plans**

One component of the Cinema Ecosystem is third party applications that read, write, analyze and view Cinema databases. With this release, we include test plans for important third party applications so that we can continuously improve our releases.

- [ParaView](testplans/paraview/testplan.md)
