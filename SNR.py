import numpy as np
import os
import pandas as pd
import scipy.interpolate
import scipy.signal
import csv


def save_condition_channel_stats_to_csv(stats_dict, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        header = ['Condition', 'Channel', 'mean', 'std', 'min', 'q15', 'q25', 'q50', 'q75', 'q95', 'max']
        writer.writerow(['Condition', 'Channel', 'Mean', 'Std', 'Min', 'Q15', 'Q25', 'Q50', 'Q75', 'Q95', 'Max'])

        # Write statistics for each condition and channel
        for condition, channels in stats_dict.items():
            for channel, stats in channels.items():
                row = [condition, channel] + [stats[stat_name] for stat_name in header[2:]]
                writer.writerow(row)


def condition_channel_statistics(data_dict):
    stats_data = {}

    # Iterate through conditions, subjects, files, and channels
    for condition, subjects in data_dict.items():
        stats_data[condition] = {}
        for subject, files in subjects.items():
            for file, channels in files.items():
                for channel, snr in channels.items():
                    if channel not in stats_data[condition]:
                        stats_data[condition][channel] = []
                    stats_data[condition][channel].append(snr)

    # Calculating statistics for each condition and channel
    stats_dict = {}
    for condition, channels in stats_data.items():
        stats_dict[condition] = {}
        for channel, values in channels.items():
            values_array = np.array(values)
            stats_dict[condition][channel] = {
                'mean': np.mean(values_array),
                'std': np.std(values_array),
                'min': np.min(values_array),
                'q15': np.percentile(values_array, 15),
                'q25': np.percentile(values_array, 25),
                'q50': np.median(values_array),
                'q75': np.percentile(values_array, 75),
                'q95': np.percentile(values_array, 95),
                'max': np.max(values_array)
            }

    return stats_dict


def save_stats_to_csv(stats_dict, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        header = ['Channel', 'mean', 'std', 'min', 'q15', 'q25', 'q50', 'q75', 'q95', 'max']
        writer.writerow(header)

        # Write statistics for each channel
        for channel, stats in stats_dict.items():
            row = [channel] + [stats[stat_name] for stat_name in header[1:]]
            writer.writerow(row)


def channel_statistics(data_dict):
    # Extracting all SNR values for each channel across all conditions
    channel_data = {}

    for condition, subjects in data_dict.items():
        for subject, files in subjects.items():
            for file, channels in files.items():
                for channel, snr in channels.items():
                    if channel not in channel_data:
                        channel_data[channel] = []
                    channel_data[channel].append(snr)

    # Calculating statistics for each channel
    stats_dict = {}
    for channel, values in channel_data.items():
        values_array = np.array(values)
        stats_dict[channel] = {
            'mean': np.mean(values_array),
            'std': np.std(values_array),
            'min': np.min(values_array),
            'q15': np.percentile(values_array, 15),
            'q25': np.percentile(values_array, 25),
            'q50': np.median(values_array),
            'q75': np.percentile(values_array, 75),
            'q95': np.percentile(values_array, 95),
            'max': np.max(values_array)
        }

    return stats_dict


def save_dict_to_csv(data_dict, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(['Condition', 'Subject', 'File', 'Channel', 'SNR'])

        # Flatten the nested dictionary and write to CSV
        for condition_name, subjects in data_dict.items():
            for subject_name, files in subjects.items():
                for file_name, channels in files.items():
                    for channel_name, snr_value in channels.items():
                        writer.writerow([condition_name, subject_name, file_name, channel_name, snr_value])


def get_snr(csv_path, channel_name):
    df = pd.read_csv(csv_path)

    sn = df[channel_name].to_numpy()

    acorrsn = scipy.signal.correlate(sn, sn, 'full')

    mu = np.mean(sn)

    n0 = len(sn)
    offset = 2

    x = list(range(n0 - offset - 1, n0 + offset, 1))
    y = list(acorrsn[x])

    x0 = x.pop(offset)
    y0 = y.pop(offset)

    # interpolate by polynomial
    f_p2 = np.polyfit(x, y, 2)
    y0_int = np.polyval(f_p2, x0)

    snr_est = 10 * np.log10((y0_int - mu ** 2) / (y0 - y0_int))

    return snr_est

if __name__ == '__main__':
    root_path = './Engagnition Dataset/'  # Set your path to data directory here
    snr_data = {}  # Dictionary to store SNR values

    for condition_names in os.listdir(root_path):
        snr_data[condition_names] = {}
        print(condition_names)

        for sub_name in os.listdir(root_path + condition_names):
            snr_data[condition_names][sub_name] = {}
            print(sub_name)

            for file_name in os.listdir(root_path + condition_names +'/' + sub_name):
                print(file_name)
                file_path = root_path + condition_names +'/' + sub_name + '/' + file_name
                print(file_path)

                if file_name == 'E4AccData.csv':
                    channel_list = ['Acc_X', 'Acc_Y', 'Acc_Z', 'Acc_SVM']
                    snr_data[condition_names][sub_name][file_name] = {}

                    for channel_name in channel_list:
                        snr_value = get_snr(file_path, channel_name)
                        print(snr_value)
                        snr_data[condition_names][sub_name][file_name][channel_name] = snr_value

                elif file_name == 'E4GsrData.csv':
                    channel_list = ['GSR']
                    snr_data[condition_names][sub_name][file_name] = {}

                    for channel_name in channel_list:
                        snr_value = get_snr(file_path, channel_name)
                        snr_data[condition_names][sub_name][file_name][channel_name] = snr_value
                        print(snr_value)

                elif file_name == 'E4TmpData.csv':
                    channel_list = ['Tmp']
                    snr_data[condition_names][sub_name][file_name] = {}

                    for channel_name in channel_list:
                        snr_value = get_snr(file_path, channel_name)
                        snr_data[condition_names][sub_name][file_name][channel_name] = snr_value
                        print(snr_value)
    print(snr_data)
    # snr_data_dict: 위에서 생성한 SNR 값을 포함하는 딕셔너리
    # "output.csv": 저장할 CSV 파일의 경로
    save_dict_to_csv(snr_data, "./output.csv")

    # snr_data_dict: 위에서 생성한 SNR 값을 포함하는 딕셔너리
    stats = channel_statistics(snr_data)
    print(stats)

    # stats: channel_statistics 함수로부터 얻은 통계 요약 딕셔너리
    # "output_stats.csv": 저장할 CSV 파일의 경로
    save_stats_to_csv(stats, "./output_stats.csv")

    # snr_data_dict: 원래의 SNR 값을 포함하는 딕셔너리
    stats_by_condition_channel = condition_channel_statistics(snr_data)

    # "output_condition_channel_stats.csv": 저장할 CSV 파일의 경로
    save_condition_channel_stats_to_csv(stats_by_condition_channel, "output_condition_channel_stats.csv")
