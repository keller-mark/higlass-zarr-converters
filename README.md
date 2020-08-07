# higlass-zarr-converters

## chromsizes-tsv to zarr

```sh
python src/chromsizes_tsv_to_zarr.py --help
python src/chromsizes_tsv_to_zarr.py \
    -i data/chromsizes/hg38.tsv \
    -o data/chromsizes/hg38.zarr
```

## chromsizes-csv to zarr

```sh
python src/chromsizes_csv_to_zarr.py --help
python src/chromsizes_csv_to_zarr.py \
    -i data/chromsizes/hg38.csv \
    -o data/chromsizes/hg38.zarr
```

## chromsizes-negspy to zarr

Browse available assemblies [here](https://github.com/pkerpedjiev/negspy/tree/a3a0046170548ccac44aa5b09faf3bcc37d5ce39/negspy/data).

```sh
python src/chromsizes_negspy_to_zarr.py --help
python src/chromsizes_negspy_to_zarr.py \
    -a hg38 \
    -o data/chromsizes/hg38.zarr
```