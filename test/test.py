import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from tqdm import tqdm
import re
import pandas as pd
import networkx as nx
import operator
import numpy as np
data =pd.read_csv('news_title_networkx.csv')

target = ['청년', '일자리','복지','센터','도로','관광']

data = data[(data['word1'].isin(target) | data['word2'].isin(target))]
data = data[data['word1'] != '울산']
data = data[data['word2'] != '울산']
data = data[data['word1'] != '울주군']

data = data[data['word2'] != '울주군']
data = data.reset_index(drop = True)
print(data)
# data = data[(data['word1']== '복지') | (data['word2'] == '복지')]
# data = data[(data['word1'] != '울산') |  (data['word2'] != '울산')]
# data = data[(data['word1'] != '울주군') | (data['word2'] != '울주군')]
print(len(data))
def make_network(data, file_name, mode, scale):
    # 단어쌍 동시 출현 빈도수를 담았던 networkx
    G_centrality = nx.Graph()
    #     FG = nx.from_pandas_edgelist(data, source = 'word1', target = 'word2')
    #     FG.nodes()
    #     dgr = nx.degree_centrality(FG)
    #     pgr = nx.pagerank(FG) #페이지 링크
    for ind in range(len(np.where(data['freq'] >= mode)[0])):
        G_centrality.add_edge(data['word1'][ind], data['word2'][ind])

    dgr = nx.degree_centrality(G_centrality)  # 연결 중심성
    #   btw = nx.betweenness_centrality(G_centrality) #매개 중심성
    cls = nx.closeness_centrality(G_centrality)  # 근접 중심성
    #     egv = nx.eigenvector_centrality(G_centrality) #고유벡터 중심성
    pgr = nx.pagerank(G_centrality)  # 페이지 링크

    sorted_dgr = sorted(dgr.items(), key=operator.itemgetter(1), reverse=True)
    #   sorted_btw = sorted(btw.items(), key = operator.itemgetter(1), reverse = True)
    sorted_cls = sorted(cls.items(), key=operator.itemgetter(1), reverse=True)
    #     sorted_egv = sorted(egv.items(), key = operator.itemgetter(1), reverse = True)
    sorted_pgr = sorted(pgr.items(), key=operator.itemgetter(1), reverse=True)

    # 단어 네트워크를 그려줄 Graph 선언
    G = nx.Graph()

    # 노드  #노드사이즈는 pgr 로 하는거고 (지금은 dgr이고)
    for i in range(len(sorted_pgr)):
        G.add_node(sorted_pgr[i][0], nodesize=sorted_dgr[i][1])
    #         print(sorted_pgr[i][0],sorted_pgr[i][1] )
    # 간선 간선 사이즈는 freq로 하고있네
    for ind in range(len(np.where(data['freq'] > mode)[0])):
        G.add_weighted_edges_from([(data['word1'][ind], data['word2'][ind], int(data['freq'][ind]) )])
        # 노드 크기 조정
    sizes = [G.nodes[node]['nodesize'] * 1000 for node in G]

    options = {
        'edge_color': '#FFDEA2',
        #         'width': 1,
        'with_labels': True,
        'font_weight': 'regular'

    }

    # 폰트 설정을 위한 font_manager import
    import matplotlib.font_manager as fm
    import matplotlib.pyplot as plt

    fm._rebuild()
    font_fname = 'C:\\Windows\\Fonts\\a한글나라BM.otf'
    fontprop = fm.FontProperties(fname=font_fname, size=18).get_name()

    nx.draw(G,
            node_size=sizes,
            pos=nx.spring_layout(G, k=3.5, iterations=20, scale=scale),
            **options,
            font_family=fontprop,
            node_shape='h',
            # cmap=plt.cm.Blues,
            alpha=0.9
            )

    ax = plt.gca()
    plt.rcParams['figure.figsize'] = (50, 50)
    ax.collections[0].set_edgecolor('#555555')
    plt.savefig('%s_network.jpg' % file_name, dpi = 1000)

make_network(data, 'test', 10, 100)
