import streamlit as st
import pandas as pd
import click
from pycellbase.cbclient import CellBaseClient
from pycellbase.cbconfig import ConfigClient

from biomutant.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="BioMutant")
def biomutant():
    cc = ConfigClient({
        'rest': {'hosts': ['https://ws.zettagenomics.com/cellbase']},
        'species': 'hsapiens',
        'version': 'v5',
    })
    cbc = CellBaseClient(cc)
    mc = cbc.get_meta_client()
    st.title("Biomutant")

    # species = mc.get_species()
    # st.write(species)
    # st.write("hi2")

    versions = mc.get_versions()
    st.write(versions)



if __name__ == "__main__":
    biomutant()
