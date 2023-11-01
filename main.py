import os
import re


def find_spark_sql(file_pth):
	sql_query_pattern_1 = r'SELECT\s+.*\s+FROM\s+\w+|INSERT\s+INTO\s+\w+|UPDATE\s+\w+|DELETE\s+FROM\s+\w+|CREATE\s+TABLE\s+\w+|DROP\s+TABLE\s+\w+|SHOW\s+TABLES'
	sql_query_pattern_2 = r'(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bCREATE\b|\bDROP\b|\bALTER\b|\bFROM\b|\bJOIN\b|\bWHERE\b|\bGROUP BY\b|\bORDER BY\b|\bLIMIT\b|\bUNION\b|\bINTERSECT\b|\bEXCEPT\b|\bWITH\b|\bSET\b|`[a-zA-Z_][a-zA-Z0-9_]*`|"[a-zA-Z_][a-zA-Z0-9_]*")'
	with open(file_pth, "r+") as f:
		file = f.readlines()
		for line in file:
			'''
			# Sample input text
			line = """
			SELECT * FROM table_name
			WHERE column_name = 'value'
			"""
			'''
			matches = re.findall(sql_query_pattern_1, line, re.IGNORECASE)
			matches = re.findall(sql_query_pattern_2, line, re.IGNORECASE)

			if matches:
				print("Spark SQL queries found:")
				for match in matches:
					print(match)
			else:
				print("No Spark SQL queries found.")


def get_paths(pth, files_path):
	for i in os.listdir(pth):
		if os.path.isfile(os.path.join(pth, i)):
			if str(i).split('.')[-1] in ['java', 'scala', 'python', 'sh']:
				files_path.append(os.path.join(pth, i))
		else:
			if len(os.listdir(os.path.join(pth, i))) > 0:
				get_paths(os.path.join(pth, i), files_path)
	return files_path


if __name__ == '__main__':
	files_path = list()
	pth = r'C:\myWork\GitHub\New folder'
	files_path = get_paths(pth, files_path)
	for i in files_path:
		print(i, 'exists: ', os.path.exists(i))
		find_spark_sql(i)
