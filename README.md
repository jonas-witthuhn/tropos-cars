# tropos-cars


## Installation

Before installing this package, ensure you have the following prerequisites:
* netcdf4
* netcdf-fortran
* hdf5
* cmake

Install prerequisites while creating environment (recommended)
```bash
mamba create -n tcars -c conda-forge netcdf4 netcdf-fortran hdf5 cmake
```

Activate the environment
```bash
mamba activate tcars
```

Then tcars + ecrad can be installed via:
```bash
python -m pip install git+https://github.com/jonas-witthuhn/tropos-cars
```

### Developement install

Install prerequisites while creating environment
```bash
mamba create -n tcars -c conda-forge netcdf4 netcdf-fortran hdf5 cmake
```

Activate the environment
```bash
mamba activate tcars
```
Clone the repository:
```bash
git clone https://github.com/jonas-witthuhn/tropos-cars
```

Clone the repository:
```bash
cd tropos-cars/
```

Then install in editable mode:
```bash
python -m pip install -e .
```

