from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.container import Docker
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.database import Postgresql
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Service
from diagrams.digitalocean.compute import K8SCluster
from diagrams.digitalocean.network import LoadBalancer
from diagrams.onprem.client import User

# Atributos para os clusters visuais no diagrama
graph_attr = {
    "fontsize": "20",
    "bgcolor": "white"
}

with Diagram("Arquitetura Detalhada - Projeto Kube-News", show=False, graph_attr=graph_attr, direction="TB"):

    usuario_final = User("Usuário Final")

    with Cluster("Ambiente de Desenvolvimento & CI/CD"):
        github = Github("GitHub Repo")
        github_actions = GithubActions("GitHub Actions")
        docker_registry = Docker("Docker Hub")

    with Cluster("Cloud Provider: DigitalOcean"):
        do_lb = LoadBalancer("Load Balancer")
        
        with Cluster("Kubernetes - Cluster Kubernetes"):
            k8s_cluster = K8SCluster("k8s-cluster")

            with Cluster("Namespace: 'default'"):
                # Detalhando o Deployment com Pods dentro
                with Cluster("Kube-News Deployment"):
                    kube_news_pods = [Pod("pod 1"),
                                      Pod("pod 2"),
                                      Pod("...")]

                kube_news_service = Service("Kube-News Service")
                
                # Detalhando o monitoramento
                with Cluster("Stack de Monitoramento"):
                    prometheus = Prometheus("Prometheus")
                    grafana = Grafana("Grafana")
                    postgres_deployment = Deployment("PostgreSQL")

    # Definindo o fluxo completo com labels nas conexões
    github >> Edge(label="git push\n(aciona a pipeline)") >> github_actions

    github_actions >> Edge(label="build & push da imagem") >> docker_registry

    github_actions >> Edge(label="doctl & kubectl apply\n(deploy dos manifestos)", label_pos="left") >> k8s_cluster
    
    usuario_final >> Edge(label="Requisição HTTPS") >> do_lb >> Edge(label="Porta 8080") >> kube_news_service >> kube_news_pods

    prometheus >> Edge(label="Coleta métricas\n(scrape no /metrics)", style="dotted") >> kube_news_pods
    
    grafana >> Edge(label="Consulta dados\n(query PromQL)") >> prometheus
    
    kube_news_pods >> Edge(label="Conexão com DB") >> postgres_deployment