import matplotlib.pyplot as plt
import numpy as np


# 读取数据
def out_data(filename:str):
    full_path = filename + '\out'
    t1_y = []
    t2_y = []
    t3_y = []

    t1_x = []
    t2_x = []
    t3_x = []

    with open(full_path) as f:
        contents = f.readlines()

        t1_first = contents[4]
        t1_first = float(t1_first[0:t1_first.find('\t')])
        t2_first = contents[44]
        t2_first = float(t2_first[0:t2_first.find('\t')])
        t3_first = contents[78]
        t3_first = float(t3_first[0:t3_first.find('\t')])

        for index in range(4, 41):
            line = contents[index].strip()
            pos = line.find('\t')
            t1_y.append(float(line[pos+1:]))
            t1_x.append(float(line[0:pos]) - t1_first)

        for index in range(44, 75):
            line = contents[index].strip()
            pos = line.find('\t')
            t2_y.append(float(line[pos+1:]))
            t2_x.append(float(line[0:pos]) - t2_first)

        for index in range(78, 104):
            line = contents[index].strip()
            pos = line.find('\t')
            t3_y.append(float(line[pos + 1:]))
            t3_x.append(float(line[0:pos]) - t3_first)

    f.close()
    return np.array(t1_y), np.array(t2_y), np.array(t3_y), np.array(t1_x), np.array(t2_x), np.array(t3_x)


def in_data(filename:str):
    full_path = filename + '\in'

    p1 = []
    p2 = []
    p3 = []
    p4 = []

    x1 = []
    x2 = []
    x3 = []
    x4 = []

    with open(full_path) as f:
        contents = f.readlines()

        t1_first = contents[4]
        t1_first = float(t1_first[0:t1_first.find('\t')])
        t4_first = contents[133]
        t4_first = float(t4_first[0:t4_first.find('\t')])
        t2_first = contents[47]
        t2_first = float(t2_first[0:t2_first.find('\t')])
        t3_first = contents[90]
        t3_first = float(t3_first[0:t3_first.find('\t')])

        for index in range(4, 44):
            line = contents[index].strip()
            pos = line.find('\t')
            p1.append(float(line[pos+1:]))
            x1.append(float(line[0:pos]) - t1_first)

        for index in range(47, 87):
            line = contents[index].strip()
            pos = line.find('\t')
            p2.append(float(line[pos+1:]))
            x2.append(float(line[0:pos]) - t2_first)

        for index in range(90, 130):
            line = contents[index].strip()
            pos = line.find('\t')
            p3.append(float(line[pos + 1:]))
            x3.append(float(line[0:pos]) - t3_first)

        for index in range(133, 173):
            line = contents[index].strip()
            pos = line.find('\t')
            p4.append(float(line[pos + 1:]))
            x4.append(float(line[0:pos]) - t4_first)

    f.close()

    return np.array(p1), np.array(p2), np.array(p3), np.array(p4), np.array(x1), np.array(x2), np.array(x3), np.array(x4)


def p_out_data(filename:str):
    full_path = filename + '\p_out'
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    x1 = []
    x2 = []
    x3 = []
    x4 = []

    with open(full_path) as f:
        contents = f.readlines()

        t1_first = contents[4]
        t1_first = float(t1_first[0:t1_first.find('\t')])
        t4_first = contents[133]
        t4_first = float(t4_first[0:t4_first.find('\t')])
        t2_first = contents[47]
        t2_first = float(t2_first[0:t2_first.find('\t')])
        t3_first = contents[90]
        t3_first = float(t3_first[0:t3_first.find('\t')])

        for index in range(4, 44):
            line = contents[index].strip()
            pos = line.find('\t')
            p1.append(float(line[pos+1:]))
            x1.append(float(line[0:pos]) - t1_first)

        for index in range(47, 87):
            line = contents[index].strip()
            pos = line.find('\t')
            p2.append(float(line[pos+1:]))
            x2.append(float(line[0:pos]) - t2_first)

        for index in range(90, 130):
            line = contents[index].strip()
            pos = line.find('\t')
            p3.append(float(line[pos + 1:]))
            x3.append(float(line[0:pos]) - t3_first)

        for index in range(133, 173):
            line = contents[index].strip()
            pos = line.find('\t')
            p4.append(float(line[pos + 1:]))
            x4.append(float(line[0:pos]) - t4_first)

    f.close()
    return np.array(p1), np.array(p2), np.array(p3), np.array(p4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t1_y, t2_y, t3_y, t1_x, t2_x, t3_x = out_data()
    in_1, in_2, in_3, in_4, x_1, x_2, x_3, x_4 = in_data()
    out_1, out_2, out_3, out_4 = p_out_data()

    plt.figure(figsize=(5, 5.5))
    plt.rc('font', family='Times New Roman', size=15)
    font1 = {'weight':'bold', 'family':'Times New Roman', 'size':15}
    plt.plot(X,  bleu_16, marker='*', label='full', color='orange', ms=8, linewidth=2.5)
    plt.subplots_adjust(left=0.15, right=0.99, top=0.9, bottom=0.1)
    plt.plot(X, base_bleu, label='base', color='g', ms=8, linewidth=2.5)
    plt.legend(fontsize=15, loc="best")
    plt.xlim((0, 1))
    plt.ylim((33.8, 36))
    my_x_ticks = np.arange(0, 1, 0.1)
    my_y_ticks = np.arange(33.8, 36, 0.2)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.xlabel("λ", size=15, font=font1, labelpad=10)
    plt.ylabel("BLEU", size=15, font=font1, labelpad=10)
    plt.title("Python Bleu performance", size=15, font=font1, pad=10)
    plt.tight_layout()
    plt.savefig('bleu_p_lambda.pdf', format="pdf", bbox_inches="tight")
    plt.show()

