# Error_Model_Build
Use bowtie2 to determine the error rate of DNA sequencing reads. Then using InSilicoSeq, make an error model for those outputs.

## BLAST Database building

```bash
makeblastdb  -in reference_genome.fna -out reference_genome -parse_seqids -dbtype nucl
```
