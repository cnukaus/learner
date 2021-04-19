-- quick profile script
EXECUTE IMMEDIATE (
  SELECT 
    STRING_AGG(
      CONCAT(
        'SELECT "', field_path, '" as field_path, ',
          'CAST(MIN(', field_path, ') as string) as max, ',
          'CAST(MAX(', field_path, ') as string) as min ',
          'COUNT(DISTINCT ', field_path, ') as count_distinct ',
        'FROM ', table_name) ,
      ' UNION ALL \n'
    ) as query
  FROM (
    SELECT CONCAT('`', table_catalog, '.', table_schema, '.', table_name, '`') as table_name, field_path, data_type
    FROM project.dataset.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS
    WHERE table_name = 'table_name'
      AND data_type NOT LIKE 'STRUCT%'
  )
)
