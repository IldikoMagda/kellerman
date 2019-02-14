library(biomaRt)
#listMarts()
ensembl = useMart("ensembl")
#listDatasets(ensembl)
ensembl = useDataset("hsapiens_gene_ensembl",mart=ensembl)
filters = listFilters(ensembl)
attributes = listAttributes(ensembl)
data = read.csv(file.choose(), header = TRUE, sep = ",")
accession = data$target_uniprot

result = getBM(attributes = c('ensembl_gene_id', 'external_gene_name', 'chromosome_name', 'uniprotswissprot', 'start_position', 'end_position', 'strand', 'band'), 
      filters = 'uniprotswissprot', values = accession,
      mart = ensembl)

save(result,file="result.csv")
write.csv(result, file = "result.csv")
