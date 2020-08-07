import click
import pandas as pd
import zarr
from numcodecs import Zlib

@click.command()
@click.option('-i', '--input', required=True, type=click.Path(exists=True))
@click.option('-o', '--output', required=True, type=click.Path())
@click.option('-h', '--has-header', is_flag=True, flag_value=True)
def chromsizes_tsv_to_zarr(input, output, has_header):
    df = pd.read_csv(input, header=(0 if has_header else None), sep='\t')

    num_chroms = df.shape[0]

    columns = df.columns.values.tolist()
    chrom_names = df[columns[0]].values
    chrom_sizes = df[columns[1]].values

    df["name_len"] = df[columns[0]].apply(lambda name: len(name))
    max_name_len = int(df["name_len"].max())
    

    z = zarr.open(
        output,
        mode='w'
    )
    compressor = Zlib(level=1)

    z.create_dataset("names", shape=(num_chroms,), dtype=f"S{max_name_len}", compressor=compressor)
    z.create_dataset("sizes", shape=(num_chroms,), dtype="u4", compressor=compressor)
    z["names"][:] = chrom_names
    z["sizes"][:] = chrom_sizes

if __name__ == "__main__":
    chromsizes_tsv_to_zarr()