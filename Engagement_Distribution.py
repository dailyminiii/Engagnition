import os
import csv
import matplotlib.pyplot as plt

def plot_distribution(distribution):
    labels = list(distribution.keys())
    zero_counts = [distribution[label]["0"] for label in labels]
    one_counts = [distribution[label]["1"] for label in labels]
    two_counts = [distribution[label]["2"] for label in labels]
    others_counts = [distribution[label]["others"] for label in labels]

    bar_width = 0.2
    r1 = range(len(labels))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]

    plt.bar(r1, zero_counts, width=bar_width, color='#a6cee3', edgecolor='grey', label='0')
    plt.bar(r2, one_counts, width=bar_width, color='#fdbf6f', edgecolor='grey', label='1')
    plt.bar(r3, two_counts, width=bar_width, color='#b2df8a', edgecolor='grey', label='2')
    plt.bar(r4, others_counts, width=bar_width, color='#fb9a99', edgecolor='grey', label='others')

    plt.xlabel('Conditions', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(labels))], labels)
    plt.legend()
    plt.show()

def aggregate_by_condition_percentage(engagment_distribution):
    condition_distribution = {}
    total_distribution = {"0": 0, "1": 0, "2": 0, "others": 0}  # 모든 조건을 합한 분포
    grand_total_counts = 0  # 모든 조건의 전체 항목 수

    for condition_name, sub_values in engagment_distribution.items():
        condition_distribution[condition_name] = {"0": 0, "1": 0, "2": 0, "others": 0}
        total_counts = 0  # 해당 조건의 전체 항목 수

        for sub_name, file_values in sub_values.items():
            for file_name, counts in file_values.items():
                condition_distribution[condition_name]["0"] += counts["0"]
                condition_distribution[condition_name]["1"] += counts["1"]
                condition_distribution[condition_name]["2"] += counts["2"]
                condition_distribution[condition_name]["others"] += counts["others"]
                total_counts += sum(counts.values())

                # 전체 항목 수 및 분포 업데이트
                grand_total_counts += sum(counts.values())
                total_distribution["0"] += counts["0"]
                total_distribution["1"] += counts["1"]
                total_distribution["2"] += counts["2"]
                total_distribution["others"] += counts["others"]

        # 조건별 백분율로 계산
        if total_counts > 0:
            for key in condition_distribution[condition_name]:
                condition_distribution[condition_name][key] = (condition_distribution[condition_name][key] / total_counts) * 100
        else:
            for key in condition_distribution[condition_name]:
                condition_distribution[condition_name][key] = 0.0

    # 'Total' 조건의 백분율 계산
    if grand_total_counts > 0:
        for key in total_distribution:
            total_distribution[key] = (total_distribution[key] / grand_total_counts) * 100
    else:
        for key in total_distribution:
            total_distribution[key] = 0.0

    condition_distribution["Total"] = total_distribution

    return condition_distribution


def get_eng_distribution(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        counts = {"0": 0, "1": 0, "2": 0, "others": 0}

        for row in reader:
            try:
                value = row[1]  # 두 번째 열의 값
                if value == "0":
                    counts["0"] += 1
                elif value == "1":
                    counts["1"] += 1
                elif value == "2":
                    counts["2"] += 1
                else:
                    counts["others"] += 1
            except IndexError:
                continue  # 행에 값이 없는 경우 건너뛴다

    return counts


if __name__ == '__main__':
    root_path = './Engagnition Dataset/'  # Set your path to data directory here
    engagment_distribution = {}  # Dictionary to store SNR values

    for condition_names in os.listdir(root_path):
        engagment_distribution[condition_names] = {}
        print(condition_names)

        for sub_name in os.listdir(root_path + condition_names):
            engagment_distribution[condition_names][sub_name] = {}
            print(sub_name)

            for file_name in os.listdir(root_path + condition_names +'/' + sub_name):
                file_path = root_path + condition_names +'/' + sub_name + '/' + file_name

                if file_name == 'LabelingData.csv':
                    engagment_distribution[condition_names][sub_name][file_name] = {}
                    distributionNum = get_eng_distribution(file_path)
                    engagment_distribution[condition_names][sub_name][file_name]['0'] = distributionNum['0']
                    engagment_distribution[condition_names][sub_name][file_name]['1'] = distributionNum['1']
                    engagment_distribution[condition_names][sub_name][file_name]['2'] = distributionNum['2']
                    engagment_distribution[condition_names][sub_name][file_name]['others'] = distributionNum['others']

    print(engagment_distribution)

    # 조건별 백분율 분포를 출력
    condition_distribution_percentage = aggregate_by_condition_percentage(engagment_distribution)
    print("\nCondition-wise Distribution (%):")
    for condition, counts in condition_distribution_percentage.items():
        print(f"{condition}: {counts}")

    # 그래프 그리기
    plot_distribution(condition_distribution_percentage)

