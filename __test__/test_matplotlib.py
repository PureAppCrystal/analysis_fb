import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
from numpy.random import randn
from matplotlib import font_manager, rc







def ex1():
    plt.plot([1, 2, 3, 4], [10, 30, 20, 40])
    plt.show()


def ex2():
    # r,c,l 을 줘서 여러개의 그래프를 배열형식으로출력 가능하다
    fig = plt.figure()

    # 첫번째것이 row 뒤에것이 column
    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 30, 20, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [10, 30, 20, 40])

    plt.show()

def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(rnd.random(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(rnd.random(100), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * rnd.random(100))

    plt.show()


def ex4():
    fig, subplots = plt.subplots(2, 2)

    print(subplots)
    subplots[0, 0].plot(np.arange(100).cumsum(), 'k--')
    subplots[0, 1].hist(np.arange(100), bins=20, color='k')

    plt.show()


def ex5():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([10, 20, 30, 40])

    plt.show()


def ex6():
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].plot(rnd.random(1000), bins=20, color='k', alpha=0.3)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


def ex7():
    fig, subplots = plt.subplots(1, 1)
    # g : 초록색, o : 도트, -- : 점선, - : 실선
    # subplots.plot([1, 2, 3, 4], [10, 30, 20, 40], 'go--')
    subplots.plot([1, 2, 3, 4], [10, 30, 20, 40], 'go-')

    plt.show()


def ex7_2():
    fig, subplots = plt.subplots(1, 1)
    # g : 초록색, o : 도트, -- : 점선, - : 실선
    # subplots.plot([1, 2, 3, 4], [10, 30, 20, 40], 'go--')
    subplots.plot([1, 2, 3, 4],
                  [10, 30, 20, 40],
                  color='k',
                  marker='o',
                  linestyle='-')

    plt.show()


def ex8():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color="g", linestyle="--", marker="o")
    plt.show()


def ex9():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(50).cumsum(), 'ko--')
    plt.show()


def ex10():
    data = rnd.random(50).cumsum()

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(data, color='#aaaaaa', linestyle='--', label='Default')
    # drawstyle =  ‘default’, ‘steps’, ‘steps-pre’, ‘steps-mid’, ‘steps-post’
    subplots.plot(data, 'k-', drawstyle='steps-mid', label='steps-mid')

    plt.legend(loc='best')
    plt.show()


def ex11():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum())

    subplots.set_xticks([0, 25, 50, 75, 100])
    subplots.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4'],
                             rotation=30,
                             fontsize='small')
    subplots.set_xlabel('Positions')
    subplots.set_title("my First Matplotlib Plot")

    plt.show()


def ex12():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum(), 'k', label='one')
    subplots.plot(randn(100).cumsum(), 'k--', label='two')
    subplots.plot(randn(100).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


def ex13():
    # font_options = {'family': 'Malgun Gothic'}
    # plt.rc('font', ** font_options)
    # plt.rc('font', family='Malgun Gothic')
    # plt.rc('axes', unicode_minus=False)
    # rc 파일 설정으로 대체

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum())

    subplots.set_xticks([0, 25, 50, 75, 100])
    subplots.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4'],
                             rotation=30,
                             fontsize='small')
    subplots.set_xlabel('포지션')
    subplots.set_title("예제13 한글처리")

    plt.savefig('ex13-plot.png', dpi=400, bbox_inches='tight')
    # plt.savefig('ex13-plot.jpeg', dpi=400, bbox_inches='tight')
    plt.savefig('ex13-plot.pdf', dpi=400, bbox_inches='tight')
    plt.savefig('ex13-plot.svg', dpi=400, bbox_inches='tight')

    plt.show()


def ex14():
    font_file = 'c:/Windows\Fonts/malgunsl.ttf'
    font_name = font_manager.FontProperties(fname=font_file).get_name()
    print(font_name)


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    ex13()
    # ex14()
