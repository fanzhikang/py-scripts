from numpy import *
import operator

def classify0(inX, dataset, labels, k):
    """
    inX inX 是输入的测试样本，是一个[x, y]样式的
    dataset 是训练样本集
    labels 是训练样本标签
    k 是top k最相近的
    """
    dataSetSize = dataset.shape[0]
    
      # tile属于numpy模块下边的函数
      # tile（A, reps）返回一个shape=reps的矩阵，矩阵的每个元素是A
      # 比如 A=[0,1,2] 那么，tile(A, 2)= [0, 1, 2, 0, 1, 2]
     # tile(A,(2,2)) = [[0, 1, 2, 0, 1, 2],
     #                  [0, 1, 2, 0, 1, 2]]
     # tile(A,(2,1,2)) = [[[0, 1, 2, 0, 1, 2]],
      #                    [[0, 1, 2, 0, 1, 2]]] 
      # 上边那个结果的分开理解就是：
      # 最外层是2个元素，即最外边的[]中包含2个元素，类似于[C,D],而此处的C=D，因为是复制出来的
      # 然后C包含1个元素，即C=[E],同理D=[E]
      # 最后E包含2个元素，即E=[F,G],此处F=G，因为是复制出来的
      # F就是A了，基础元素
      # 综合起来就是(2,1,2)= [C, C] = [[E], [E]] = [[[F, F]], [[F, F]]] = [[[A, A]], [[A, A]]]
    # 这个地方就是为了把输入的测试样本扩展为和dataset的shape一样，然后就可以直接做矩阵减法了。
      # 比如，dataset有4个样本，就是4*2的矩阵，输入测试样本肯定是一个了，就是1*2，为了计算输入样本与训练样本的距离
      # 那么，需要对这个数据进行作差。这是一次比较，因为训练样本有n个，那么就要进行n次比较；
    # 为了方便计算，把输入样本复制n次，然后直接与训练样本作矩阵差运算，就可以一次性比较了n个样本。
     # 比如inX = [0,1],dataset就用函数返回的结果，那么
    # tile(inX, (4,1))= [[ 0.0, 1.0],
     #                    [ 0.0, 1.0],
     #                    [ 0.0, 1.0],
     #                    [ 0.0, 1.0]]
     # 作差之后
     # diffMat = [[-1.0,-0.1],
    #            [-1.0, 0.0],
     #            [ 0.0, 1.0],
     #            [ 0.0, 0.9]]
    diffMat = tile(inX, (dataSetSize, 1)) - dataset

    sqDiffMat = diffMat **2
    
    # axis=1表示横轴
    sqDistance = sqDiffMat.sum(axis=1)

    # 对平方和开根号
    distance = sqDistance **0.5

    # 按照升序进行快速排序，返回的是原数组的下标。
    # 比如，x = [30, 10, 20, 40]
    # 升序排序后应该是[10,20,30,40],他们的原下标是[1,2,0,3]
    # 那么，numpy.argsort(x) = [1, 2, 0, 3]
    sortedDistIndicies = distance.argsort()

    # 存放最终结果及相应投票数
    classCount={}

    for i in range(k):
        # index = sortedDistIndicies[i]是第i个最相近的样本下标
        # voteIlabel = labels[index]是样本index对应的分类结果('A' or 'B')
        votelabel = labels[sortedDistIndicies[i]]
        # classCount.get(voteIlabel, 0)返回voteIlabel的值，如果不存在，则返回0
        # 然后将票数增1
        classCount[votelabel] = classCount.get(votelabel,0) + 1

    # 结果分类进行排序，返回得票最多的结果
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createDataSet():
    group = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0. , 0. ],
        [0. , 0. ]
    ])
    labels = ['A','A','B','B']
    return group, labels
    
if __name__ == "__main__":
    dataset, labels = createDataSet()
    inX = [0.1, 0.1]
    className = classify0(inX, dataset, labels, 3)
    print('the class of test sample is '+className)