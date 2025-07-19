# 🚀 Maratona DevOps & IA - Projeto de Implantação Completa

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)

## 📄 Visão Geral do Projeto

Este repositório contém a implementação completa de uma aplicação web full-stack, implantada em um ambiente de nuvem utilizando as práticas e ferramentas mais modernas de DevOps e IA. O projeto foi desenvolvido durante a **Maratona DevOps & IA**, demonstrando um ciclo de vida completo de software, desde a containerização até o deploy automatizado e o monitoramento em produção.

O objetivo é aplicar os pilares fundamentais de DevOps e explorar o uso de IA Generativa para construir uma arquitetura resiliente, escalável e automatizada de forma mais eficiente.

## 🛠️ Tecnologias e Pilares DevOps Demonstrados

| Pilar DevOps | Ferramentas e Conceitos Aplicados |
| :--- | :--- |
| **Containerização** | **Docker** para empacotar a aplicação e suas dependências em imagens portáteis e imutáveis. **Dockerfile** para definir a receita de construção. **Docker Hub** como registro de imagens. |
| **Orquestração** | **Kubernetes (K8s)** para gerenciar e orquestrar os contêineres em produção. Utilização de `Deployments` para garantir o estado desejado e `Services` (`LoadBalancer`) para expor a aplicação. |
| **Infraestrutura como Código (IaC)** | Manifestos **YAML** do Kubernetes para definir declarativamente todos os recursos da aplicação, garantindo consistência e reprodutibilidade do ambiente. |
| **CI/CD (Integração e Deploy Contínuo)**| **GitHub Actions** para criar pipelines automatizadas. **Pipeline de Teste** rodando em branches de feature e **Pipeline de CI/CD** para a branch `main`, que constrói a imagem Docker, publica e faz o deploy automático no cluster. |
| **Automação com IA (AI-driven DevOps)** | **Google Gemini CLI** para geração de código, análise de logs e otimização de scripts de pipeline diretamente no ambiente de desenvolvimento (WSL), acelerando as entregas. |
| **Cloud & Infraestrutura** | **DigitalOcean** como provedor de nuvem, utilizando o serviço gerenciado **DOKS (DigitalOcean Kubernetes Service)**. Gerenciamento de recursos via CLI com **`doctl`**. |
| **Monitoramento & Observabilidade** | **Prometheus** para coletar métricas de saúde e performance da aplicação em tempo real. **Grafana** para visualizar essas métricas em dashboards interativos e intuitivos. |

---

## ✨ Showcase do Projeto

### 🚀 Aplicação em Produção
*A aplicação Kube-News, após o deploy bem-sucedido via pipeline de CI/CD, acessível publicamente através de um Load Balancer.*

<img width="2537" height="1513" alt="Deploy no K8s" src="https://github.com/user-attachments/assets/349be588-2e33-4f9b-bfaf-364c51319287" />

---

<br>

### 🔄 Pipeline de CI/CD em Ação
*O workflow do GitHub Actions mostrando a execução dos jobs de CI e CD sendo concluídos com sucesso após um `git push`.*

<img width="2517" height="934" alt="Pipeline de CD" src="https://github.com/user-attachments/assets/e3a00629-2ea1-4352-b99a-5188ee6c506f" />


<br>

### 📈 Coleta de Métricas (Prometheus)
*Interface do Prometheus exibindo a coleta da métrica `http_request_duration_seconds_count`, demonstrando que a descoberta de serviços está funcionando e os dados da aplicação estão sendo coletados com sucesso.*

<img width="2549" height="1443" alt="Métricas do Prometheus" src="https://github.com/user-attachments/assets/d6c90930-e1a8-457a-b343-7b051ae84660" />


### 📊 Dashboard de Monitoramento (Grafana)
*Dashboard no Grafana exibindo as métricas da aplicação (uso de CPU, memória, latência) coletadas pelo Prometheus em tempo real.*

<img width="2017" height="1429" alt="Dashboard do cluster K8s no Grafana" src="https://github.com/user-attachments/assets/8c2d9f2d-1547-4329-848a-2d27542158ef" />


<br>

### 🤖 Assistente de IA em Ação (Gemini CLI)
*Uso do Gemini CLI no terminal WSL para gerar manifestos do Kubernetes e workflows do GitHub Actions, demonstrando a capacidade de acelerar o desenvolvimento e a análise de configurações.*

<img width="1980" height="1078" alt="gemini-cli" src="https://github.com/user-attachments/assets/4b0870cf-a56b-4b5f-8353-52ffdda50ecb" />


---

## ⚙️ Arquitetura da Solução

O fluxo de trabalho implementado segue as melhores práticas de DevOps:

1.  **Desenvolvimento & IA:** O código da aplicação é alterado e testado localmente com Docker Compose. O **Gemini CLI** é utilizado principalmente para otimizar scripts e manifestos.
2.  **Versionamento:** As alterações são enviadas para o GitHub (`git push`).
3.  **CI (Integração Contínua):** O push dispara um workflow no **GitHub Actions** que:
    * Executa testes automatizados.
    * Constrói uma nova imagem Docker versionada e a envia para o **Docker Hub**.
4.  **CD (Deploy Contínuo):** Após o sucesso da CI, um segundo job:
    * Conecta-se de forma segura ao cluster **Kubernetes** na **DigitalOcean**.
    * Atualiza o `Deployment` para usar a nova imagem recém-construída, realizando um rolling update sem indisponibilidade.
5.  **Monitoramento:** Em produção, o **Prometheus** coleta continuamente métricas da aplicação, que são visualizadas no **Grafana**.
