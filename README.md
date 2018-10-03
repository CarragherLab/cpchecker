cpchecker
==========

A simple command-line tool to check for failed cellprofiler jobs on eddie.

To install:

```
python setup.py install --user
```

To use:

```
cpchecker config.yaml
```

Where `config.yaml` is the `cptools` configuration file used to create the cellprofiler job.

`cpchecker` looks in the results directory for missing results files, and returns a the task IDs of jobs which have not produced any results.