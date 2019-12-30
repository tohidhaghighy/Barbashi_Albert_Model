from Barbashi_Albert import Barbashi_Albert_Model
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

barbashi=Barbashi_Albert_Model(1234)
ig=barbashi.make_initial_Complete_graph()

barbashi.show_plot(ig)

ig_empty=barbashi.make_Empty_graph()

#BA_graph=barbashi.barabasi_albert(ig,100,4,barbashi.seed)

#Directed_graph=barbashi.directed_barabasi_albert(ig,100,4,0.9,barbashi.seed)

Growth=barbashi.growth_Without_PrefesionalAttachment(ig_empty,100,4,barbashi.seed)

#Copying=barbashi.copying_model(ig,10,0.5,barbashi.seed)

#barbashi.show_plot(ig)
l=barbashi.Get_Degrees(Growth)
print(l)

barbashi.Destribution_Show_Graph(l)
barbashi.show_plot(Growth)

print(barbashi.Cluster_Coeffistiont(Growth))