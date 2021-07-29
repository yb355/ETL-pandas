from numpy import int32
from os import path
from utils.time_utils import CurrentDateTime
from initializing import DataFrameStrategy, ComandLineProcessor_Excel, notifier
import pandas as pd

#Change the location for the following folders.
output_folder = r"####"
input_folder = r"####"
history_folder = r"######"

def main():
	current_dt = CurrentDateTime()
	comand_line_processor = ComandLineProcessor_Excel(input_folder, history_folder)
	df_strategy = DataFrameStrategy(pd, comand_line_processor)
	raw_df = df_strategy.intitialize_data_frame()
	df = clean_data_frame(raw_df)
	df_columns_added = add_required_columns(df, current_dt)
	df_formatted = apply_format(df_columns_added)
	output_to_csv(df_formatted, current_dt)
	df_strategy.finalize()


def clean_data_frame(input_df):
	raw_df = input_df.copy()
	raw_df = raw_df.convert_dtypes()
	raw_df["Buffer"] = raw_df["Buffer"].map(lambda k: 0.0 if k =="буфер 0" else k)
	raw_df = raw_df[["SKU", "Buffer"]]
	df = raw_df.dropna()	
	df.reset_index(drop=True, inplace=True)
	return df
	

def add_required_columns(input_df, current_dt: CurrentDateTime):
	df = input_df.copy()
	df["0-Name"] = "Buf_Manual_{0} {1} {2}  {3}".format(current_dt.month_name(),
								current_dt.day(), 
								current_dt.year(), 
								current_dt.time()
	)
	df["1-Location"] = "006"
	df["3-Null"] = "null"
	df["4"] = "buffer"
	df["5-yr1"] = current_dt.year()
	df["6-month1"] = current_dt.month()
	df["7-day1"] = current_dt.day()
	df["8-yr2"] = current_dt.year()
	df["9-month2"] = current_dt.month()
	df["10-day2"] = current_dt.day()
	df["11"] = 1
	df["13-Value"] = "FixedValue"
	df["14"] = 1
	df["15"] = "Approved"
	values = [" " for i in range(1, 11)] + [current_dt.year(),
					current_dt.month(), current_dt.day()]
	for i in range(len(values)):
		df[f"{16 + i}"] = values[i]
	return df

@notifier("Dataframe finished the formatting and processing phases. Outputting to csv.")
def apply_format(input_df):
	df = input_df.copy()
	df = df[["0-Name", "1-Location", "SKU", "3-Null", "4", '5-yr1',
		'6-month1', '7-day1', '8-yr2', '9-month2', '10-day2', '11', "Buffer", '13-Value', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']]
	df = df.astype({"Buffer": int32})
	return df

@notifier("Success, the csv is created.")
def output_to_csv(formated_df, current_dt: CurrentDateTime):
	date_format, time_format = current_dt.output_format_dd_tt()
	output_name = "SEASONALITY_Calculate_Buffers_Manual{0}_{1}.csv".format(date_format, time_format)
	output_name = path.join(output_folder, output_name) 
	formated_df.to_csv(output_name, sep="|", index=False, header=False)


if __name__ == "__main__":
	main()