import os, sys


def build_ith_fold(datasets, k_fold, valid_id):
    train_text = []
    valid_text = []

    for id in range(k_fold):
        if id == valid_id:
            valid_text = datasets[id]
        else:
            train_text += datasets[id]

    return train_text, valid_text


def get_datasets(root_path, k_fold):
    datasets = []
    for id in range(k_fold):
        part_path = root_path + os.path.sep + 'data' + str(id) + '.txt'
        with open(part_path, 'r') as f:
            # print([line.replace('\n', '') for line in f.readlines()])
            # datasets.append([line.replace('\n', '') for line in f.readlines()])
            datasets.append(f.readlines())
    return datasets


def save_datasets(root_path, train_text, valid_text):
    train_path = root_path + os.path.sep + 'train.txt'
    valid_path = root_path + os.path.sep + 'valid.txt'

    with open(train_path, 'w') as f:
        f.writelines(train_text)
    with open(valid_path, 'w') as f:
        f.writelines(valid_text)


if __name__ == '__main__':
    args = sys.argv
    arg_name = ['--source', '--k-fold']
    root_path, k_fold = None, None
    index = 1
    while index < len(args):
        if arg_name[0] in args[index]:
            root_path = args[index + 1]
            index = index + 2
        elif arg_name[1] in args[index]:
            k_fold = args[index + 1]
            index = index + 2
        else:
            exit(0)
    if not root_path or not k_fold:
        exit(0)

    k_fold = int(k_fold)
    # print(root_path, k_fold)

    datasets = get_datasets(root_path, k_fold)
    # for data in datasets:
    #     print(len(data), data)
    # for i in range(k_fold):
    train_text, valid_text = build_ith_fold(datasets, k_fold, 6)
    print(len(datasets), len(train_text), len(valid_text))
    save_datasets(root_path, train_text, valid_text)
        # ith_train()
    print('success')