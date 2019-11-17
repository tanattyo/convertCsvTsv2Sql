echo taxonomy
python3 tsv2sql.py taxonomy.tsv > taxonomy.sql
echo specimen_data
python3 tsv2sql.py specimen_data.tsv > specimen_data.sql
