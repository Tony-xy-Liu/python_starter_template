# Project Template

`./dev.sh` automates common development tasks. Feel free to add new ones! Change `NAME` and `USER` at the top of `./dev.sh` before use. GPLv3 License included (`./LICENSE`), keep or change for your project.

External dependencies:
- [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html) / [Mamba (multithreaded Anaconda)](https://mamba.readthedocs.io/en/latest/mamba-installation.html#mamba-install)
- [Docker](https://docs.docker.com/engine/install/)
- [Singluarity (requires docker)](https://apptainer.org/admin-docs/master/installation.html)

A quick sample:

- `./dev.sh -bc` to build <b>conda package</b>
- `./dev.sh -bd` to build <b>docker container</b>
- `./dev.sh -bd` to run source
- other scripts include uploading to anaconda, running `./src` locally, and testing containers

### Setting up the environment

`./dev.sh -idev`

Creates a new conda environement using the `base.yml` and `dev.yml` files at `./envs`

### Running locally

`./dev.sh -r`

Runs the python package at `./src/*` directly

### Conda

Requires the development environment and anaconda.org account if uploading. Add dependencies under `./envs/base.yml`.

1. bump the version at `./src/<PACKAGE>/version.txt`
1. build pip package `./dev.sh -bp`
1. build conda package using the pip package `./dev.sh -bc`
1. upload to your channel `./dev.sh -uc`

### Docker / Singularity

1. configure `./Dockerfile`
1. build container `./dev.sh -bd`
1. upload to quay.io `./dev.sh -ud`
1. build singularity from docker `./dev.sh -bs` (not dependent on upload)
