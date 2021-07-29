class DataFrameStrategy:
    def __init__(self, pandas, processor):
        self.pd = pandas
        self.processor = processor

    def intitialize_data_frame(self):
        raw_df = self.processor.create_file(self.pd)
        raw_df = self.processor.parse_required_columns(raw_df)
        return raw_df
    
    def finalize(self):
        self.processor.move_files()


