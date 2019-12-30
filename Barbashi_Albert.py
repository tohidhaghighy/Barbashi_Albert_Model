import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from networkx.generators.random_graphs import barabasi_albert_graph

class Barbashi_Albert_Model:
    def __init__(self,seed):
        self.seed=seed

    def make_initial_Complete_graph(self):
        ig = nx.empty_graph(0, create_using=nx.DiGraph())
        ig.add_nodes_from([0, 1, 2, 3])
        ig.add_edges_from([(0,1), (0,2), (0,3),
                  (1,0), (1,2), (1,3),
                  (2,1), (2,0), (2,3),
                  (3,1), (3,2), (3,0),])
        return ig

    def make_Empty_graph(self):
        ig = nx.empty_graph(1, create_using=nx.Graph())
        return ig

    def show_plot(self,graph):
        fig, ax = plt.subplots(1, 1)
        nx.draw(graph, ax=ax)
        plt.show()

    def Get_Degrees(self,graph):
        degree_sequence = []
        for i,x in list(graph.degree):
            degree_sequence.append(x) 
        return degree_sequence  

    def Get_InDegree(self,graph):
        in_degree_sequence = []
        for i,x in list(graph.in_degree):
            in_degree_sequence.append(x) 
        return in_degree_sequence       

    def Get_OutDegree(self,graph):
        out_degree_sequence = []
        for i,x in list(graph.out_degree):
            out_degree_sequence.append(x) 
        return out_degree_sequence 
    
    def Destribution_Show_Graph(self,degrees):
        fig, ax = plt.subplots(1, 1)
        sns.countplot(degrees, ax=ax)
        plt.show()

    def Cluster_Coeffistiont(self,graph):
        return nx.algorithms.cluster.average_clustering(graph)
        
    def barabasi_albert(self,initial_graph, n, m, seed):
        random.seed(seed)
        #گراف اولیه
        g = initial_graph
        #تا جایی که کل نود ها اضافه شود
        while(len(g)<n):
            #در اوردن لیست درجات هر نود گراف
            node_list, degree_list = zip(*list(g.degree))
            #احتمال تک تک درجات
            probability_list = [x for x in degree_list]
            #مجموع درجات لیست
            s = sum(probability_list)
            #احتمال هر لیست درجات
            probability_list = [x/s for x in probability_list]
            # انتخاب 4 تا نود توسط احتمال
            selected_nodes = np.random.choice(np.array(node_list),4 ,replace=False ,p=probability_list)
            # لیست درجات نود
            selected_nodes = list(selected_nodes)
            #افزودن نود جدید
            g.add_node(len(g))
            # افزودن هر یال نود
            for i in range(m):
                g.add_edge(len(g)-1, selected_nodes[i])
        return g

    def directed_barabasi_albert(self,initial_graph, n, m, A, seed):
        random.seed(seed)
        # گراف اولیه
        ig = initial_graph
        # به تعداد کل نود های داده شده اجرا میشود
        while(len(ig)<n):
            # لیست درجات را در می آورد
            node_list, degree_list = zip(*list(ig.in_degree))
            # احتمال درجات را محاسبه میکند با فرمول روی سوال
            probability_list = [x+A for x in degree_list]
            s = sum(probability_list)
            probability_list = [x/s for x in probability_list]
            selected_nodes = np.random.choice(np.array(node_list),4 ,replace=False ,p=probability_list)
            selected_nodes = list(selected_nodes)
            ig.add_node(len(ig))
            for i in range(m):
                ig.add_edge(len(ig)-1, selected_nodes[i])
        return ig

    def growth_Without_PrefesionalAttachment(self,initial_graph, n, m, seed):
        random.seed(seed)
        g = initial_graph
        while(len(g)<n):
            nodes = list(g.nodes)
            selected_nodes = [random.choice(nodes) for x in range(m)]
            g.add_node(len(g))
            for i in range(m):
                g.add_edge(len(g)-1, selected_nodes[i])
        return g

    def copying_model(self,initial_graph, n, p, seed):
        random.seed(seed)
        # ایجاد نود اولیه
        g = initial_graph
        while(len(g)<n):
            # لیست نود ها
            nodes = list(g.nodes)
            # انتخاب تصادفی نود ها
            selected_node = random.choice(nodes)
            # افزودن نود جدید
            g.add_node(len(g))
            # انتخاب عدد رندوم
            rn = random.random()
            # اگر عدد رندوم از احتمال مد نظر ما کوچکتر بود به ان نود وصل میشود
            if(rn<p):
                g.add_edge(len(g)-1, selected_node)
            else:
                # وصل شدن به همسایه ها
                selected_nodes = [y for x,y in list(g.edges) if y==selected_node]
                for i in range(len(selected_nodes)):
                    g.add_edge(len(g)-1, selected_nodes[i])
        return g
        
