# Odd-Even Mapreduce program using Python

The following program uses **Mapreduce Programming** to calculate total number of odd and even numbers in a given dataset and calculate the sum of each.

- Use `test.sh` before running the program on hadoop in order to test for any faults.
- System does not require hadoop to run `test.sh`.
- Modify `input.txt` as per your desire.

### Running the script on hadoop

After starting the hadoop and copying the files into hdfs, following command(s) can be used to run the script

`hadoop jar {hadoop-stream-3.x.x.jar_location} -file {mapper_file_location} -mapper mapper.py -file {reduer_file_location} -reducer reducer.py -input {input_file_location_hdfs} -output {output_folder_location_hdfs}`