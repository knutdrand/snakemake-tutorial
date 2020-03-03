include: "bdg2bw.sm"

rule get_bed_file:
    output:
        "bed_files/{name}.bed"
    shell:
        "python scripts/generate_bed_files.py > {output}"

rule get_bed_graph:
    output:
        "bed_graphs/{name}.bdg"
    shell:
        "python scripts/generate_bed_graphs.py > {output}"
