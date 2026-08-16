# GestãoHub: Agilidade Técnica em Microequipes 🚀

Este repositório contém o código-fonte do **GestãoHub** (Sistema de Gestão de Voluntariado), desenvolvido como estudo de caso prático para o artigo técnico: *"AGILIDADE TÉCNICA EM MICROEQUIPES: O IMPACTO DE FRAMEWORKS BATTERIES-INCLUDED NA REDUÇÃO DO TIME-TO-MARKET DE MVPS"*.

📄 **O artigo completo está disponível na pasta raiz deste repositório (`327_99951767297685.pdf`).**

## 🎯 Sobre o Projeto

O atual cenário de desenvolvimento de software exige validação rápida de hipóteses de negócio. Para desenvolvedores autônomos (*Solo Developers*) e microequipes de TI, os rituais ágeis clássicos (Scrum, SAFe) podem gerar gargalos burocráticos. 

Este projeto demonstra, na prática, como a "Agilidade Técnica" — focada na escolha estratégica de frameworks *Batteries-Included* e na arquitetura de **Monolito Modular** — é capaz de reduzir o tempo de desenvolvimento de MVPs em até **91%**, democratizando a segurança e a escalabilidade de nível corporativo.

## 🛠️ Stack Tecnológica e Arquitetura

*   **Linguagem:** Python 3.12+
*   **Framework Full-Stack:** Django 5.0 (LTS) seguindo o padrão MVT (Model-View-Template).
*   **Frontend Automático (SSR):** Bootstrap 5 integrado via `django-crispy-forms` para design responsivo e acessível sem overhead de bibliotecas JS complexas (React/Angular).
*   **Backoffice Corporativo:** Interface administrativa gerada automaticamente e modernizada com **Django Jazzmin**.
*   **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Produção).

## 📊 Análise de Resultados Técnicos

A aplicação da filosofia *Lean Software Development* na construção deste sistema provou que automatizar componentes de infraestrutura (ORM, proteção CSRF/XSS, validação de formulários) permite o foco exclusivo na regra de negócio.

| Funcionalidade | Desenvolvimento Tradicional | Framework Django | Ganho de Eficiência |
| :--- | :--- | :--- | :--- |
| Configuração de Banco de Dados | 6h | 0,5h (ORM) | **91%** |
| Sistema de Login/Autenticação | 12h | 1h (Auth nativo) | **91%** |
| Painel Administrativo (Backend) | 30h | 0,5h (Admin+Jazzmin) | **98%** |
| Interface de Usuário (Frontend) | 20h | 3h (Bootstrap+Crispy)| **85%** |
| **Tempo Total Estimado** | **78 horas** | **7 horas** | **~91%** |

## 🚀 Como Executar o Projeto Localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/JacksonRicardo/sistema-voluntarios-agil.git
   cd sistema-voluntarios-agil










