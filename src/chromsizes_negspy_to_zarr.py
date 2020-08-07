import click
import pandas as pd
import zarr
from numcodecs import Zlib
import negspy.coordinates as nc

@click.command()
@click.option('-a', '--assembly', required=True, type=str)
@click.option('-o', '--output', required=True, type=click.Path())
@click.option('-h', '--has-header', is_flag=True, flag_value=True)
def chromsizes_negspy_to_zarr(assembly, output, has_header):
    chrom_order = nc.get_chromorder(assembly)
    chrom_info = nc.get_chrominfo(assembly)
    
    chrom_rows = [
        {
            0: chrom_name,
            1: chrom_info.chrom_lengths[chrom_name]
        }
        for chrom_name in chrom_order
    ]

    df = pd.DataFrame(columns=[0, 1], data=chrom_rows)

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
    chromsizes_negspy_to_zarr()